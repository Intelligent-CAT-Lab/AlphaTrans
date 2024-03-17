import argparse
import os
import subprocess
import json

ORIGINAL_DIR = "java_projects/cleaned_final_projects"
OUTPUT_DIR = "java_projects/glue_code"
TRANSLATION_DIR = "data/verified_projects"
DIR_DEPTH = "../../../"

main_paths = {
    "commons-fileupload": "main/java/org/apache/commons/fileupload/",
    "commons-cli": "main/java/org/apache/commons/cli/",
    "commons-codec": "main/java/org/apache/commons/codec/",
    "commons-csv": "main/java/org/apache/commons/csv/",
    "commons-graph": "main/java/org/apache/commons/graph/",
    "commons-pool": "main/java/org/apache/commons/pool/",
    "commons-validator": "main/java/org/apache/commons/validator/",
    "joda-convert": "main/java/org/joda/convert/",
    "joda-money": "main/java/org/joda/money/",
}

def get_destination_path(path, file_name, is_full_path=False, path_to_main=None):
    _path = [OUTPUT_DIR]
    
    # fully qualified path from schema. remove the first 2 directories
    if is_full_path:
        _path += path.split('/')[2:]
        _directories = "/".join(_path[:-1])
    else:
        _path += [path, "src"]
        if path_to_main:
            _path += [path_to_main]
        # print(_path, "/".join(_path))
        _directories = "/".join(_path)
    
    # create the final path if it doesn't exist
    os.makedirs(_directories, exist_ok=True)

    return f"{_directories}/{file_name}.java"

def write_to_file(file, content):
    with open(file, "w") as f:
        f.write(content)

    # format java file
    try:
        subprocess.run(['java', '-jar', 'src/glue_code/google-java-format-1.20.0-all-deps.jar', '-r', file], check=True)
    except Exception as e:
        print(f"Error formatting {file}: {e}")
    return

def get_org_name(project_name):
    paths = main_paths[project_name].split('/')
    # find 'org', return the next segment
    org_name = paths[paths.index('org')+1]
    # return org name if project does not already contain it
    return f"org.{org_name}" if org_name not in project_name.split('-') else "org"

def make_mappings(args, schemas):
    """
    Create mappings for package classes.
    """
    classes_to_map = []
    imports = []
    
    formatted_project_name = args.project_name.replace('-', '.')
    for schema in schemas:
        if args.class_name is not None and not schema.endswith(f'.{args.class_name}.json'):
            continue
        with open(f'data/schemas/{args.project_name}/{schema}') as f:
            data = json.load(f)

        for _class in data['classes']:
            if (
                    not data['classes'][_class]['is_interface'] 
                    and not '/test/' in data['path'] 
                    and not _class.endswith('Exception')
                ):
                if data['classes'][_class]["nested_inside"]:
                    classes_to_map.append(f"{data['classes'][_class]['nested_inside']}.{_class}")
                else:
                    classes_to_map.append(_class)
                
                # link subpackages
                if main_paths[args.project_name] in data['path']:
                    path_tail = data['path'].split(main_paths[args.project_name])[-1]
                    if "/" in path_tail:
                        # remove the last segment
                        path_tail = path_tail[:path_tail.rfind('/')]
                        subproj_name = "." + path_tail.replace('/', '.')
                        imports.append(f"{subproj_name}.{_class}")
                    
    return_string = ""
    for _class in classes_to_map:
        return_string += f".targetTypeMapping(Value.class, {_class}.class, null, (v) -> new {_class}(v))\n"
        
    imports_string = ""
    for _import in imports:
        imports_string += f"import {get_org_name(args.project_name)}.{formatted_project_name}{_import};"

    return return_string + "// TODO: Add other mappings", imports_string

def make_exception_mappings(args, schemas):
    """
    Create mappings for package exception classes.
    """
    package_exception_classes = []
    imports = []

    formatted_project_name = args.project_name.replace('-', '.')
    for schema in schemas:
        if args.class_name is not None and not schema.endswith(f'.{args.class_name}.json'):
            continue
        with open(f'data/schemas/{args.project_name}/{schema}') as f:
            data = json.load(f)
            
        for _class in data['classes']:
            if _class.endswith('Exception'):
                if data['classes'][_class]["nested_inside"]:
                    package_exception_classes.append(f"{data['classes'][_class]['nested_inside']}.{_class}")
                else:
                    package_exception_classes.append(_class)
                
                # link subpackages
                if main_paths[args.project_name] in data['path']:
                    path_tail = data['path'].split(main_paths[args.project_name])[-1]
                    if "/" in path_tail:
                        # remove the last segment
                        path_tail = path_tail[:path_tail.rfind('/')]
                        subproj_name = "." + path_tail.replace('/', '.')
                        imports.append(f"{subproj_name}.{_class}")
                
    return_string = ""
    for _class in package_exception_classes:
        return_string += f"if(exceptionType.equals(\"{_class}\")){{ return new {_class}(exceptionObj);}}\n"
    
    imports_string = ""
    for _import in imports:
        imports_string += f"import {get_org_name(args.project_name)}.{formatted_project_name}{_import};"
        
    return return_string + "// TODO: Add other mappings", imports_string

def main(args):
    if not os.path.exists('data/schemas'):
        raise Exception('Please run from the root directory!')

    schemas = os.listdir(f'data/schemas/{args.project_name}')
    # remove test and partial files
    schemas = [file for file in schemas if 'Test' not in file and not file.endswith('_python_partial.json')]
    
    formatted_proj_name = args.project_name.replace('-', '.')
    
    # Copy original project to glue_code directory
    # skip if already exists
    if not os.path.exists(f"{OUTPUT_DIR}/{args.project_name}"):
        os.makedirs(f"{OUTPUT_DIR}/{args.project_name}")
        subprocess.run(['cp', '-r', f"{ORIGINAL_DIR}/{args.project_name}/.", f"{OUTPUT_DIR}/{args.project_name}"], check=True)
    
    # Add ContextInitializer.java
    ctx_mappings, ctx_imports = make_mappings(args, schemas)
    with open("src/glue_code/misc/ContextInitializer.java") as f:
        write_to_file(get_destination_path(args.project_name, "ContextInitializer", path_to_main=main_paths[args.project_name]), f.read().format(
                project = f"{get_org_name(args.project_name)}.{formatted_proj_name}",
                imports = ctx_imports,
                code_directory = f"{DIR_DEPTH}{TRANSLATION_DIR}/{args.project_name}/src/{main_paths[args.project_name]}",
                package_directory = f"{DIR_DEPTH}{TRANSLATION_DIR}/{args.project_name}/",
                mappings = ctx_mappings
            ))

    # Add ExceptionHandler.java
    exp_mappings, exp_imports = make_exception_mappings(args, schemas)
    with open("src/glue_code/misc/ExceptionHandler.java") as f:
        write_to_file(get_destination_path(args.project_name, "ExceptionHandler", path_to_main=main_paths[args.project_name]), f.read().format(
                project = f"{get_org_name(args.project_name)}.{formatted_proj_name}",
                imports = exp_imports,
                mappings = exp_mappings
            ))
    
    # IntegrationUtils.java
    with open("src/glue_code/misc/IntegrationUtils.java") as f:
        write_to_file(get_destination_path(args.project_name, "IntegrationUtils", path_to_main=main_paths[args.project_name]), f.read().format(
                project = f"{get_org_name(args.project_name)}.{formatted_proj_name}"
            ))

    for schema in schemas:

        # !! specify schema to test !!
        if args.class_name is not None and not schema.endswith(f'.{args.class_name}.json'):
            continue

        with open(f'data/schemas/{args.project_name}/{schema}') as f:
            data = json.load(f)
        
        final_glue_code = ""
        unclosed_brace_count = 0
        
        # find subpackage names (if exist)
        if main_paths[args.project_name] in data['path']:
            path_tail = data['path'].split(main_paths[args.project_name])[-1]
            if "/" in path_tail:
                # remove the last segment
                path_tail = path_tail[:path_tail.rfind('/')]
                subproj_name = "." + path_tail.replace('/', '.')
            else:
                subproj_name = ""
        else:
            subproj_name = ""

        final_glue_code += f"package {get_org_name(args.project_name)}.{formatted_proj_name + subproj_name};\n\n"
        # step 0: add graal imports
        final_glue_code += "import org.graalvm.polyglot.Value;\n"
        final_glue_code += "import org.graalvm.polyglot.PolyglotException;\n"
        final_glue_code += f"import {get_org_name(args.project_name)}.{formatted_proj_name}.ContextInitializer;\n"
        final_glue_code += f"import {get_org_name(args.project_name)}.{formatted_proj_name}.ExceptionHandler;\n"
        final_glue_code += f"import {get_org_name(args.project_name)}.{formatted_proj_name}.IntegrationUtils;\n"

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
                python_file_dir = subproj_name.replace('.', '/')
                python_file_dir = python_file_dir[:-1] if not python_file_dir else python_file_dir
                current_file_name = data["path"].split('/')[-1].split('.')[0]
                python_file = f'"{python_file_dir}/{current_file_name}.py"'
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
                    caller = "this.obj"
                
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
                    final_glue_code += f"    // TODO: Handle {exception_name}\n"
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
        output_file = get_destination_path(data["path"], class_name, is_full_path=True)
        write_to_file(output_file, final_glue_code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate glue code for Java')
    parser.add_argument('--project_name', type=str, dest='project_name', help='name of the project', required=True)
    parser.add_argument('--class', type=str, dest='class_name', help='name of the class', required=False)
    args = parser.parse_args()
    main(args)
