import argparse
import os
import subprocess
import json

OUTPUT_DIR = "src/glue_code/output"

def get_destination_path(project_name, file_name):
    project_dirs = [x for x in project_name.split("-") if x != ""]

    package_path = "/".join(["org", "apache"] + project_dirs)
    final_path = f"{OUTPUT_DIR}/{project_name}/src/main/java/{package_path}"

    # create the package directory if it doesn't exist
    os.makedirs(final_path, exist_ok=True)

    return f"{final_path}/{file_name}.java"

def write_to_file(file, content):
    with open(file, "w") as f:
        f.write(content)

    # format java file
    try:
        subprocess.run(['java', '-jar', 'src/glue_code/google-java-format-1.20.0-all-deps.jar', '-r', file], check=True)
    except Exception as e:
        print(f"Error formatting {file}: {e}")
    return

def make_mappings(args, schemas):
    """
    Create mappings for package classes.
    """
    classes_to_map = [] 
    for schema in schemas:
        if args.class_name is not None and not schema.endswith(f'.{args.class_name}.json'):
            continue
        with open(f'data/schemas/{args.project_name}/{schema}') as f:
            data = json.load(f)

        for _class in data['classes']:      
            if not data['classes'][_class]['is_interface']:
                if data['classes'][_class]["nested_inside"]:
                    classes_to_map.append(f"{data['classes'][_class]['nested_inside']}.{_class}")
                else:
                    classes_to_map.append(_class)
                    
    return_string = ""
    for _class in classes_to_map:
        return_string += f".targetTypeMapping(Value.class, {_class}.class, (v) -> new {_class}(v))\n" 

    return return_string + "// TODO: Add other mappings"

def make_exception_mappings(args, schemas):
    """
    Create mappings for package exception classes.
    """
    package_exception_classes = []
    for schema in schemas:
        if args.class_name is not None and not schema.endswith(f'.{args.class_name}.json'):
            continue
        with open(f'data/schemas/{args.project_name}/{schema}') as f:
            data = json.load(f)
            
        for _class in data['classes']:
            if _class.endswith('Exception'):
                package_exception_classes.append(_class)
                
    return_string = ""
    for _class in package_exception_classes:
        return_string += f"if(exceptionType.equals(\"{_class}\")){{ return new {_class}(message);}}\n"
        
    return return_string + "// TODO: Add other mappings"

def main(args):
    if not os.path.exists('data/schemas'):
        raise Exception('Please run from the root directory!')

    schemas = os.listdir(f'data/schemas/{args.project_name}')
    # remove test and partial files
    schemas = [file for file in schemas if 'Test' not in file and not file.endswith('_python_partial.json')]
    
    formatted_proj_name = args.project_name.replace('-', '.')
    
    # Add ContextInitializer.java
    with open("src/glue_code/misc/ContextInitializer.java") as f:
        write_to_file(get_destination_path(args.project_name, "ContextInitializer"), f.read().format(
                project = f"org.apache.{formatted_proj_name}",
                code_directory = "<placeholder>", # TODO: replace with actual path
                package_directory = "<placeholder>",
                mappings = make_mappings(args, schemas)
            ))
            
    # Add ExceptionHandler.java
    with open("src/glue_code/misc/ExceptionHandler.java") as f:
        write_to_file(get_destination_path(args.project_name, "ExceptionHandler"), f.read().format(
                project = f"org.apache.{formatted_proj_name}",
                mappings = make_exception_mappings(args, schemas)
            ))
    
    # TODO: IntegrationUtils.java

    for schema in schemas:

        # !! specify schema to test !!
        if args.class_name is not None and not schema.endswith(f'.{args.class_name}.json'):
            continue

        with open(f'data/schemas/{args.project_name}/{schema}') as f:
            data = json.load(f)
        
        final_glue_code = ""
        unclosed_brace_count = 0

        final_glue_code += f"package org.apache.{formatted_proj_name};\n\n"
        # step 0: add graal imports
        final_glue_code += "import org.graalvm.polyglot.Value;\n"
        final_glue_code += "import org.graalvm.polyglot.PolyglotException;\n"
        final_glue_code += f"import org.apache.{formatted_proj_name}.ContextInitializer;\n"

        # add existing imports
        for _import in data['imports']:
            final_glue_code += "".join(data['imports'][_import]["body"])

        # add class definition
        for _class in data['classes']:            
            lst = []
            with open(data['path'], 'r') as current_f:
                lst = current_f.readlines()
            class_declaration = lst[data['classes'][_class]['start']-1:data['classes'][_class]['end']]
            final_glue_code += "".join(class_declaration)

            for _field in data['classes'][_class]['fields']:
                line = "".join(data['classes'][_class]['fields'][_field]['body'])
                if '=' not in line:
                    continue
                final_glue_code += line
            
            if not data['classes'][_class]['is_interface']:
                # add graal attributes
                python_file = f'"<placeholder>"'
                class_name = f'"{_class}"'
                final_glue_code += f"    private static Value clz = ContextInitializer.getPythonClass({python_file}, {class_name});\n"
                final_glue_code += "    private Value obj;\n"

                # add value constructor
                final_glue_code += f"    public {_class}(Value obj) {{\n"
                final_glue_code += "        this.obj = obj;\n"
                final_glue_code += "    }\n"

                # add getPythonObject()
                final_glue_code += f"    public Value getPythonObject() {{\n"
                final_glue_code += "        return obj;\n"
                final_glue_code += "    }\n"

            for _method in data['classes'][_class]['methods']:
                is_constructor = data['classes'][_class]['methods'][_method]['is_constructor']
                method_body = "".join(data['classes'][_class]['methods'][_method]['body'])
                method_name = _method.split(':', 1)[1].strip() if not is_constructor else "__init__"
                
                if method_body.strip()[-1] != '}':
                    # method is not implemented
                    final_glue_code += method_body
                    
                    # add semi-colon if not present
                    if method_body.strip()[-1] != ';':
                        final_glue_code += ';'                    
                    continue
                
                method_signature = method_body[:method_body.find('{')+1]
                method_content = method_body[method_body.find('{')+1:method_body.rfind('}')]
                
                # comment out the original method contents
                commented_content = "".join([f"// {line.strip()}\n" for line in method_content.split('\n')])
                
                final_content = commented_content
                
                # construct call to Python
                if "static" in data['classes'][_class]['methods'][_method]['modifiers'] or is_constructor:
                    caller = "clz"
                else:
                    caller = "obj"
                
                args_buildup = ", ".join(data['classes'][_class]['methods'][_method]['parameters'])
                python_call = f"{caller}.invokeMember(\"{method_name}\"{', ' + args_buildup if args_buildup else ''})"
                
                if is_constructor:
                    final_content += f"\nthis.obj = {python_call};\n"
                elif 'void' in method_signature:
                    final_content += f"\n{python_call};\n"
                else:
                    return_type = data['classes'][_class]['methods'][_method]['return_types'][0][0] # taking the first return type for now (TODO: verify this)
                    
                    # return <...> from the return type if any
                    return_type = return_type[:return_type.find('<')].strip() if '<' in return_type else return_type.strip()                    
                    
                    final_content += "\n\n// TODO: Check the type mapping below!"
                    final_content += f"\nreturn {python_call}.as({return_type}.class);\n"               

                # TODO: add comments for dev hints
                if 'throws' in method_body:
                    exception_name = method_body[method_body.find('throws')+6:method_body.find('{')].strip()

                    final_glue_code += method_signature + "\n"
                    final_glue_code += "try {\n"
                    final_glue_code += final_content
                    final_glue_code += "} catch (PolyglotException e) {\n"
                    final_glue_code += f"    throw ({exception_name}) ExceptionHandler.handle(e, \"{_class}.{method_name}\");\n"
                    final_glue_code += "}\n"
                    final_glue_code += "}\n"

                else:
                    final_glue_code += method_signature + "\n"
                    final_glue_code += final_content
                    final_glue_code += "}\n"
                    
            # add nested classes
            if not data['classes'][_class]["nests"]:
                final_glue_code += "}\n"
            else:
                unclosed_brace_count += 1
                
        final_glue_code += "}\n" * unclosed_brace_count

        class_name = schema.split('.')[-2] # get the class name preceding '.json'
        output_file = get_destination_path(args.project_name, class_name)
        write_to_file(output_file, final_glue_code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate glue code for Java')
    parser.add_argument('--project_name', type=str, dest='project_name', help='name of the project', required=True)
    parser.add_argument('--class', type=str, dest='class_name', help='name of the class', required=False)
    args = parser.parse_args()
    main(args)
