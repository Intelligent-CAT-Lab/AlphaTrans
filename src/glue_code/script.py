import argparse
import os
import json

def main(args):
    schemas = os.listdir(f'../../data/schemas/{args.project_name}')
    
    # TODO: Add ContextInitializer.java, IntegrationUtils.java, ExceptionHandler.java

    for schema in schemas:
        if schema.endswith('_python_partial.json'):
            continue

        # !! specify schema to test !!
        if not schema.endswith('.OptionGroup.json'):
            continue

        with open(f'../../data/schemas/{args.project_name}/{schema}') as f:
            data = json.load(f)
        
        final_glue_code = ""
        unclosed_brace_count = 0

        formatted_proj_name = args.project_name.replace('-', '.')

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
            with open("../../" + data['path'], 'r') as current_f:
                lst = current_f.readlines()
            class_declaration = lst[data['classes'][_class]['start']-1:data['classes'][_class]['end']]
            final_glue_code += "".join(class_declaration)

            for _field in data['classes'][_class]['fields']:
                line = "".join(data['classes'][_class]['fields'][_field]['body'])
                if '=' not in line:
                    continue
                final_glue_code += line
            
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

            for _methods in data['classes'][_class]['methods']:
                method_body = "".join(data['classes'][_class]['methods'][_methods]['body'])
                method_name = _methods.split(':', 1)[1].strip()
                
                # TODO: handle constructors
                if data['classes'][_class]['methods'][_methods]['is_constructor']:
                    continue
                
                method_signature = method_body[:method_body.find('{')+1]
                method_content = method_body[method_body.find('{')+1:method_body.rfind('}')]
                
                # comment out the original method contents
                commented_content = "".join([f"// {line.strip()}\n" for line in method_content.split('\n')])
                
                final_content = commented_content
                
                # construct call to Python
                if "static" in data['classes'][_class]['methods'][_methods]['modifiers']:
                    caller = "clz"
                else:
                    caller = "obj"
                args_buildup = ", ".join(data['classes'][_class]['methods'][_methods]['parameters'])
                python_call = f"{caller}.invokeMember(\"{method_name}\"{', ' + args_buildup if args_buildup else ''})"
                
                if 'void' in method_signature:
                    final_content += f"\n{python_call};\n"
                else:
                    return_type = data['classes'][_class]['methods'][_methods]['return_types'][0][0] # taking the first return type for now (TODO: verify this)
                    
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

        # TODO: change to structured writing - projects/filenames
        # write to java file
        with open('dump.java', 'w') as _f:
            _f.write(final_glue_code)

        # todo: add shell command to format java file
        os.system('java -jar google-java-format-1.20.0-all-deps.jar -r dump.java')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate glue code for Java')
    parser.add_argument('--project_name', type=str, dest='project_name', help='name of the project')
    args = parser.parse_args()
    main(args)