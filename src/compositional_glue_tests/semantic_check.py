import argparse
import os
import subprocess
import json
from utils import write_to_file, get_destination_path
from constants import *

def main(args):
    if not os.path.exists('data/schemas'):
        raise Exception('Please run from the root directory!')

    formatted_proj_name = args.project_name.replace('-', '.')
    schemas = os.listdir(f'data/schemas/{args.project_name}')
    
    # if class name was provided, filter out the schemas
    if args.class_name:
        schemas = [s for s in schemas if s.endswith(f"{args.class_name}.json")]
    
    # copy the project to the output directory        
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
    with open("src/compositional_glue_tests/misc/ContextInitializer.java") as f:
        write_to_file(get_destination_path(args.project_name, "ContextInitializer", OUTPUT_DIR, path_to_main=main_paths[args.project_name]), f.read().format(
                project = f"org.apache.{formatted_proj_name}",
                imports = "",
                code_directory = f"{DIR_DEPTH}{SKELETON_DIR}/{args.project_name}/src/{main_paths[args.project_name].replace('/java/', '/')}",
                package_directory = f"{DIR_DEPTH}{SKELETON_DIR}/{args.project_name}/",
                mappings = ""
            ))
        
    # SemanticCheckTest class body
    semantic_check_test_body = ""
    
    for schema in schemas:
        if not schema.endswith('.json') or schema.endswith('_python_partial.json'):
            continue # skip non-schema files and python partial schemas

        if 'src.test.' in schema:
            continue # skip files in test directory
        
        schema_name = schema.split('.')[-2]
        
        with open(f'data/schemas/{args.project_name}/{schema}') as f:
            data = json.load(f)
            
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
        
        python_file_dir = subproj_name.replace('.', '/')
        current_file_name = data["path"].split('/')[-1].split('.')[0]
        python_file = f'"{python_file_dir}/{current_file_name}.py"'

        # iterate over all classes in the file
        for _class in data['classes']:
            
            # iterate over all methods in the class
            methods = data['classes'][_class]['methods'].keys()
            
            # if method name was provided, filter out the methods
            if args.method_name:
                methods = [m for m in methods if args.method_name in m]
            
            for _method in methods:
                is_constructor = data['classes'][_class]['methods'][_method]['is_constructor']
                method_name = _method.split(':', 1)[1].strip() if not is_constructor else "__init__"
                
                # if method is private, take mangling into account
                # except for constructors
                if 'private' in data['classes'][_class]['methods'][_method]['modifiers'] and not is_constructor:
                    method_name = f"_{_class}__{method_name}"
                elif 'protected' in data['classes'][_class]['methods'][_method]['modifiers'] and not is_constructor:
                    method_name = f"_{method_name}"

                test_body = "\n".join([
                    "@Test",
                    f"public void test_{schema_name}_{_class}_{method_name}() {{",
                    "   try{",
                    f"      Value clz = ContextInitializer.getPythonClass({python_file}, \"{_class}\");",
                    f"      Value member = clz.getMember(\"{method_name}\");",
                    f"      assertTrue(\"Member is not executable.\", member != null && member.canExecute());",
                    "   } catch (Exception e) {",
                    "       assertTrue(\"Error while loading class.\", false);",
                    "   }",
                    "}"                    
                ])
                
                semantic_check_test_body += test_body
                    
            # TODO: handle nested classes
            # if not data['classes'][_class]["nests"]:
            #     pass
            # else:
            #     pass

    # write the SemanticCheckTest.java file
    output_file = get_destination_path(
        f"{OUTPUT_DIR}/{args.project_name}/src/{test_paths[args.project_name]}/SemanticCheckTest.java",
        "SemanticCheckTest",
        OUTPUT_DIR,
        is_full_path=True
    )
    with open("src/compositional_glue_tests/misc/SemanticCheckTest.java") as f:
        write_to_file(output_file, f.read().format(
            project = f"org.apache.{formatted_proj_name}",
            test_body=semantic_check_test_body
        ))
        
    # run the test
    subprocess.run(['mvn', 'clean', 'test', '-Drat.skip', '-Dtest=SemanticCheckTest'], cwd=f"{OUTPUT_DIR}/{args.project_name}/", check=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate glue code for Semantic Checking')
    parser.add_argument('--project', type=str, dest='project_name', help='name of the project', required=True)
    parser.add_argument('--class', type=str, dest='class_name', help='name of the class', required=False)
    parser.add_argument('--method', type=str, dest='method_name', help='name of the method', required=False)
    args = parser.parse_args()
    main(args)
