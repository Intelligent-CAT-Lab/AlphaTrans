import argparse
import os
import subprocess
import json
import xml.etree.ElementTree as ET
 
from utils import default_type_value, make_mappings, make_exception_mappings, \
    write_to_file, get_destination_path, fetch_class_schemas, fetch_all_class_names
from constants import *

def main(args):
    if not os.path.exists('data/schemas'):
        raise Exception('Please run from the root directory!')
    
    # load type handling information
    with open('src/compositional_glue_tests/type_handling.json') as f:
        type_handling = json.load(f)

    formatted_proj_name = args.project_name.replace('-', '.')
    schemas = fetch_class_schemas(f'data/schemas', args.project_name, args.class_name)
    classes_to_translate = args.class_name if args.class_name else fetch_all_class_names(f'data/schemas', args.project_name)

    if schemas is None or len(schemas) == 0:
        raise Exception(f"Schemas for {args.class_name} not found!")
   
    """
        Copy original project to glue_code directory
        but first check if pom.xml exists in the output directory and
        and if it does, store its contents
        """
            
    pom_contents = None
    if os.path.exists(f"{OUTPUT_DIR}/{args.project_name}/pom.xml"):
        with open(f"{OUTPUT_DIR}/{args.project_name}/pom.xml") as f:
            pom_contents = f.read()
    
    if not os.path.exists(f"{OUTPUT_DIR}/{args.project_name}/"):
        os.makedirs(f"{OUTPUT_DIR}/{args.project_name}/")
    subprocess.run(['cp', '-r', f"{ORIGINAL_DIR}/{args.project_name}/.", f"{OUTPUT_DIR}/{args.project_name}/"], check=True)
    
    # if pom.xml existed, write it back
    if pom_contents:
        with open(f"{OUTPUT_DIR}/{args.project_name}/pom.xml", "w") as f:
            f.write(pom_contents)
    
    # Add ContextInitializer.java
    ctx_mappings, ctx_imports = make_mappings(args, schemas)
    with open("src/compositional_glue_tests/misc/ContextInitializer.java") as f:
        write_to_file(get_destination_path(args.project_name, "ContextInitializer", OUTPUT_DIR, path_to_main=main_paths[args.project_name]), f.read().format(
                project = f"org.apache.{formatted_proj_name}",
                imports = ctx_imports,
                code_directory = f"{DIR_DEPTH}{TRANSLATION_DIR}/{args.project_name}/src/{main_paths[args.project_name].replace('/java/', '/')}",
                package_directory = f"{DIR_DEPTH}{TRANSLATION_DIR}/{args.project_name}/",
                mappings = ctx_mappings
            ))

    # Add ExceptionHandler.java
    exp_mappings, exp_imports = make_exception_mappings(args, schemas)
    with open("src/compositional_glue_tests/misc/ExceptionHandler.java") as f:
        write_to_file(get_destination_path(args.project_name, "ExceptionHandler", OUTPUT_DIR, path_to_main=main_paths[args.project_name]), f.read().format(
                project = f"org.apache.{formatted_proj_name}",
                imports = exp_imports,
                mappings = exp_mappings
            ))
    
    # IntegrationUtils.java
    with open("src/compositional_glue_tests/misc/IntegrationUtils.java") as f:
        write_to_file(get_destination_path(args.project_name, "IntegrationUtils", OUTPUT_DIR, path_to_main=main_paths[args.project_name]), f.read().format(
                project = f"org.apache.{formatted_proj_name}"
            ))
        
    # copy java_handler.py to the translated project
    subprocess.run(['cp', 'src/compositional_glue_tests/misc/java_handler.py', f"{TRANSLATION_DIR}/{args.project_name}/src/{main_paths[args.project_name].replace('/java/', '/')}/"], check=True)

    for schema in schemas:
        with open(f'data/schemas/{args.project_name}/{schema}') as f:
            data = json.load(f)
        
        # dict with the mapping { class: <method>}
        methods_under_test = {}
        
        for _class in data['classes']:
            # check if the class is an interface and if so, quit
            if data['classes'][_class]['is_interface']:
                print(f"{_class} is an interface. No compositional tests will be generated.")
                continue
            
            if args.method_name is not None:
                methods_under_test[_class] = [args.method_name]
            else:
                methods_under_test[_class] = []
                for _method in data['classes'][_class]['methods']:
                    is_constructor = data['classes'][_class]['methods'][_method]['is_constructor']
                    method_body = "".join(data['classes'][_class]['methods'][_method]['body'])
                    method_name = _method.split(':', 1)[1].strip() if not is_constructor else "__init__"
                    methods_under_test[_class].append(method_name)
        
            # print(f"Methods under test: {methods_under_test}")
        
        final_glue_code = ""
        unclosed_brace_count = 0
            
        # sync() and revsync() method bodies
        sync_method_body = "    private void sync() {\n"
        revsync_method_body = "    private void revsync() {\n"
        
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

        final_glue_code += f"package org.apache.{formatted_proj_name + subproj_name};\n\n"
        # step 0: add graal imports
        final_glue_code += "import org.graalvm.polyglot.Value;\n"
        final_glue_code += "import org.graalvm.polyglot.PolyglotException;\n"
        final_glue_code += f"import org.apache.{formatted_proj_name}.ContextInitializer;\n"
        final_glue_code += f"import org.apache.{formatted_proj_name}.ExceptionHandler;\n"
        final_glue_code += f"import org.apache.{formatted_proj_name}.IntegrationUtils;\n"

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
            
            unitialized_fields = []

            for _field in data['classes'][_class]['fields']:
                line = "".join(data['classes'][_class]['fields'][_field]['body'])
                
                if _class in classes_to_translate:
                    # if field is 'final', remove the 'final' keyword
                    if 'final' in data['classes'][_class]['fields'][_field]['modifiers']:
                        line = line.replace(' final', '', 1)
                    
                    # add field to sync() method
                    field_name = _field.split(':')[1].strip()
                    
                    if 'private' in data['classes'][_class]['fields'][_field]['modifiers']:
                        python_field_name = f"_{_class}__{field_name}"
                    else:
                        python_field_name = field_name
                        
                    field_type = data['classes'][_class]['fields'][_field]['types'][0][0]
                    field_from_python = type_handling[field_type].format("this.obj.getMember(\"" + python_field_name + "\")")                
                        
                    sync_method_body += f"{field_name} = ({field_type}) {field_from_python};\n"
                    revsync_method_body += f"this.obj.putMember(\"{python_field_name}\", IntegrationUtils.mapToPython({field_name}));\n"

                final_glue_code += line
                
                # check if this field was not initialized
                if '=' not in line:
                    unitialized_fields.append(_field)
            
            if not data['classes'][_class]['is_interface'] and _class in classes_to_translate:
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

                # add a new empty constructor
                final_glue_code += f"public {_class}() {{this.obj = clz.newInstance();}}\n"

            if _class in data['classes'][_class]['extends']:
                # This will take care of the super class constructor when
                # the super class is defined in the same file
                
                # add empty constructor for super class
                final_glue_code += f"    public {_class}() {{\n"
                
                # initialize all uninitialized fields inside the constructor
                for _field in unitialized_fields:
                    field_name = _field.split(':')[1].strip()
                    field_type = data['classes'][_class]['fields'][_field]['types'][0][0]
                    
                    final_glue_code += f"        {field_name} = {default_type_value[field_type]};\n"
                    
                final_glue_code += "    }\n"                
            
            if _class in classes_to_translate:
                # add sync() method
                sync_method_body += "    }\n"
                revsync_method_body += "    }\n"
                
                final_glue_code += sync_method_body
                final_glue_code += revsync_method_body

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

                # not our target method
                if method_name not in methods_under_test[_class] or _class not in classes_to_translate:
                    final_glue_code += method_signature + "\n" + method_content + "}\n"
                    continue
                
                # comment out the original method contents if method is not a constructor, else leave it as it is
                if is_constructor:
                    final_content = method_content
                else:
                    commented_content = "".join([f"// {line.strip()}\n" for line in method_content.split('\n')])
                    final_content = commented_content
                
                # construct call to Python
                if "static" in data['classes'][_class]['methods'][_method]['modifiers'] or is_constructor:
                    caller = "clz"
                else:
                    caller = "this.obj"
                
                args_buildup = ", ".join(data['classes'][_class]['methods'][_method]['parameters'])
                
                if is_constructor:
                    python_call = f"clz.newInstance({args_buildup})"
                else:
                    python_call = f"{caller}.invokeMember(\"{method_name}\"{', ' + args_buildup if args_buildup else ''})"
                
                if is_constructor:
                    final_content += f"\nthis.obj = {python_call};\nsync();\n"
                elif 'void' in method_signature:
                    if 'static' in data['classes'][_class]['methods'][_method]['modifiers']:
                        final_content += f"\n{python_call};\n" # no need to sync for static methods
                    else:                    
                        final_content += f"\nrevsync();\n{python_call};\nsync();\n"
                else:
                    return_type = data['classes'][_class]['methods'][_method]['return_types'][0][0] # taking the first return type for now (TODO: check if this is OK)

                    return_type_casted = type_handling[return_type].format(python_call)
                    final_content += f"\nrevsync();\n" if 'static' not in data['classes'][_class]['methods'][_method]['modifiers'] else '' # no need to sync for static methods
                    final_content += f"{return_type} val = ({return_type}) {return_type_casted};\n"
                    final_content += "sync();\n" if 'static' not in data['classes'][_class]['methods'][_method]['modifiers'] else '' # no need to sync for static methods
                    final_content += f"return val;\n"               

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
            
            # If the super class is not defined in the same file, we handle it separately
            # note that a class can only extend at most one class
            
            # We have assumed (for now) that the parent class will have a file of its own
            if data['classes'][_class]['extends']:
                super_class = data['classes'][_class]['extends'][0]
                if super_class not in data['classes']:
                    # find the schema where the super class is defined
                    super_schema = [s for s in schemas if s.endswith(f'.{super_class}.json')][0]
                    
                    # get the path to the super class
                    with open(f'data/schemas/{args.project_name}/{super_schema}') as f:
                        super_data = json.load(f)
                        
                    super_file_path = get_destination_path(super_data["path"], super_class, OUTPUT_DIR, is_full_path=True)
                    
                    # read the super class file
                    with open(super_file_path) as f:
                        super_class_file = f.read()
                        
                    # add the empty constructor for the super class
                    unitialized_fields = []
                    for _field in super_data['classes'][super_class]['fields']:
                        line = "".join(super_data['classes'][super_class]['fields'][_field]['body'])
                        
                        if '=' not in line:
                            unitialized_fields.append(_field)
                            
                    new_constructor_code = f"    public {super_class}() {{\n"
                    
                    # initialize all uninitialized fields inside the constructor
                    for _field in unitialized_fields:
                        field_name = _field.split(':')[1].strip()
                        field_type = super_data['classes'][super_class]['fields'][_field]['types'][0][0]
                        
                        new_constructor_code += f"        {field_name} = {default_type_value[field_type]};\n"
                        
                    new_constructor_code += "    }\n"
                    
                    # note: parent class has a file of its own
                    
                    # add the new constructor to the super class file
                    super_class_file = super_class_file[:super_class_file.rfind('}')]
                    super_class_file += new_constructor_code
                    super_class_file += "}\n"
                    
                    # write the super class file back
                    write_to_file(super_file_path, super_class_file)

            class_name = schema.split('.')[-2] # get the class name preceding '.json'
            output_file = get_destination_path(data["path"], class_name, OUTPUT_DIR, is_full_path=True)
            write_to_file(output_file, final_glue_code)
            
            # run the test
            for mut in methods_under_test[_class]:
                class_name = schema.split('.')[-2]
                print("Method currently under test:", f"{class_name}#{mut}")
                try:
                    subprocess.run(['mvn', 'clean', 'test', '-Drat.skip', '-q'], cwd=f"{OUTPUT_DIR}/{args.project_name}/", stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, check=True)
                except Exception as e:
                    print(f"Error running test for {args.project_name}.")
                    continue

                # get the test results
                failed_tests = []
                
                # first get all XML files in the target/surefire-reports directory
                for report_file in [f for f in os.listdir(f"{OUTPUT_DIR}/{args.project_name}/target/surefire-reports/") if f.endswith('.xml')]:
                    test_class_name = report_file.split('.')[0]
                    root = ET.parse(f"{OUTPUT_DIR}/{args.project_name}/target/surefire-reports/{report_file}").getroot()
                    
                    # get the <testsuite> element
                    if not  root.find('testsuite'):
                        continue

                    testsuite = root.find('testsuite')
                    
                    # iterate over all testcase elements
                    for testcase in testsuite.findall('testcase'):
                        # does the testcase have an error element?
                        error = testcase.find('error')
                        
                        if error is not None:
                            failed_tests.append(f"{test_class_name}#{testcase.get('name')}")
                            
                if failed_tests:
                    print("Test failures were found.")
                    print(*failed_tests, sep='\n')
                else:
                    print("All tests passed!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate glue code for Compositional Testing.')
    parser.add_argument('--project', type=str, dest='project_name', help='<Required> name of the project', required=True)
    parser.add_argument('--class', type=str, dest='class_name', nargs="+", help='list of class name(s)', required=False)
    parser.add_argument('--method', type=str, dest='method_name', help='name of the method', required=False)
    args = parser.parse_args()
    main(args)
