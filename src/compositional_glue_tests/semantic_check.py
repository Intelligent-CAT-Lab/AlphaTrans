import argparse
import os
import subprocess
import json
from utils import write_to_file, get_destination_path
from constants import (
    main_paths,
    test_paths,
    ORIGINAL_DIR,
    OUTPUT_DIR,
    SKELETON_DIR,
    DIR_DEPTH
)

def main(args, test_classes=False):
    if not os.path.exists('data/schemas'):
        raise Exception('Please run from the root directory!')

    # if test_class is True, generate semantic tests for test classes
    package_path = (
        test_paths[args.project_name]
        if test_classes
        else main_paths[args.project_name]
    )
    print(f"Generating semantic tests for {args.project_name} {'test classes' if test_classes else 'main classes'}...")


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
    else:
        raise Exception('Please fix the pom.xml file and run again! (Check Java version and Graal dependency.)')
            
    # check whether the tests use junit-jupiter
    test_package = 'junit'
    if 'org.junit.jupiter' in pom_contents:
        test_package = 'junit-jupiter'
        
    # decide which imports to make for 'assertTrue' and 'Test'
    if test_package == 'junit':
        test_imports = "import static org.junit.Assert.assertTrue;\nimport org.junit.Test;"
    elif test_package == 'junit-jupiter':
        test_imports = "import static org.junit.jupiter.api.Assertions.assertTrue;\nimport org.junit.jupiter.api.Test;"
    
    # Add ContextInitializer.java
    with open("src/compositional_glue_tests/misc/ContextInitializer.java") as f:
        write_to_file(get_destination_path(args.project_name, "ContextInitializer", OUTPUT_DIR, path_to_main=main_paths[args.project_name]), f.read().format(
                project = f"org.apache.{formatted_proj_name}",
                imports = "",
                code_directory = f"{DIR_DEPTH}{SKELETON_DIR}/{args.project_name}/src/{package_path.replace('/java/', '/')}",
                package_directory = f"{DIR_DEPTH}{SKELETON_DIR}/{args.project_name}/",
                mappings = ""
            ))
        
    # SemanticCheckTest class body
    semantic_check_test_body = ""
    
    for schema in schemas:
        if not schema.endswith('.json') or schema.endswith('_python_partial.json'):
            continue # skip non-schema files and python partial schemas

        schema_substring = 'src.test.' if test_classes else 'src.main.'
        if schema_substring not in schema:
            continue # skip files that are not in the main directory
        
        # split on '.' and get second last and third last elements
        schema_name = schema.split('.')[-3] + '_' + schema.split('.')[-2]
        
        with open(f'data/schemas/{args.project_name}/{schema}') as f:
            data = json.load(f)
            
        # find subpackage names (if exist)
        if package_path in data['path']:
            path_tail = data['path'].split(package_path)[-1]
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
            class_name = _class
            is_anonymous = False
            
            # check if the class is anonymous
            if _class.startswith('new ') and _class.endswith('(...) { ... }'): # for now we stick to this pattern
                is_anonymous = True
                
                # extract the class name
                i = 4
                while _class[i].isalnum() or _class[i] == '_':
                    i += 1
                class_name = _class[4:i]
            
            # iterate over all methods in the class
            methods = data['classes'][_class]['methods'].keys()
            
            # if method name was provided, filter out the methods
            if args.method_name:
                methods = [m for m in methods if args.method_name in m]
                
            # collect methods to be tested
            methods_to_test = []            
            for _method in methods:
                is_constructor = data['classes'][_class]['methods'][_method]['is_constructor']
                method_name = _method.split(':', 1)[1].strip() if not is_constructor else "__init__"
                
                if not method_name:
                    continue # skip empty method names. This may happen for anonymous classes.
                
                # if method is private, take mangling into account
                # except for constructors
                if 'private' in data['classes'][_class]['methods'][_method]['modifiers'] and not is_constructor:
                    method_name = f"_{class_name}__{method_name}"
                elif 'protected' in data['classes'][_class]['methods'][_method]['modifiers'] and not is_constructor:
                    method_name = f"_{method_name}"
                
                # if method is 'from' or 'to', add an underscore at the end
                if method_name in ['from']:
                    method_name += "_"
                    
                methods_to_test.append(method_name)
                
            # remove all instances of duplicate methods
            methods_to_test = [m for m in methods_to_test if methods_to_test.count(m) == 1]
            
            # now create the test bodies
            for method_name in methods_to_test:                    
                def create_assert_args(msg: str, condition: str):
                    if test_package == 'junit':
                        return f"\"{msg}\", {condition}"
                    elif test_package == 'junit-jupiter':
                        return f"{condition}, \"{msg}\""

                test_body = "\n".join([
                    "@Test",
                    f"public void test_{schema_name}_{class_name}_{method_name}() {{",
                    "   try{",
                    f"      Value clz = ContextInitializer.getPythonClass({python_file}, \"{class_name}\");", # there is no nesting in the python code!
                    f"      Value member = clz.getMember(\"{method_name}\");",
                    f"      assertTrue({create_assert_args('Member is not executable.', 'member != null && member.canExecute()')});",
                    "   } catch (Exception e) {",
                    f"       assertTrue({create_assert_args('Error while loading class.', 'false')});",
                    "   }",
                    "}"
                ])
                
                semantic_check_test_body += test_body
    
    # write the SemanticCheckTest.java file
    output_file = get_destination_path(
        f"{OUTPUT_DIR}/{args.project_name}/src/{test_paths[args.project_name]}/SemanticCheckTest.java",
        "SemanticCheckTest",
        OUTPUT_DIR,
        is_full_path=True
    )    
    with open("src/compositional_glue_tests/misc/SemanticCheckTest.java") as f:
        write_to_file(output_file, f.read().format(
            project=f"org.apache.{formatted_proj_name}",
            imports=test_imports,
            test_body=semantic_check_test_body
        ))
        
    # run the test
    subprocess.run(['mvn', 'clean', 'test', '-Drat.skip', '-Dtest=SemanticCheckTest'], cwd=f"{OUTPUT_DIR}/{args.project_name}/", check=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate glue code for Semantic Checking')
    parser.add_argument('--project', type=str, dest='project_name', help='name of the project', required=True)
    parser.add_argument('--class', type=str, dest='class_name', help='name of the class', required=False)
    parser.add_argument('--method', type=str, dest='method_name', help='name of the method', required=False)
    parser.add_argument('--all', action='store_true', help='run for all classes and methods (including test classes)')
    args = parser.parse_args()
    main(args)
    if args.all:
        main(args, test_classes=True)
