from collections import defaultdict
import subprocess
import os
import json
from constants import *

default_type_value = defaultdict(lambda: "null")
default_type_value.update({
    "int": "0",
    "boolean": "false",
    "float": "0",
    "double": "0",
    "long": "0",
})

def fetch_class_schemas(schema_directory, project_name, class_lst):
    project_schemas = os.listdir(f'{schema_directory}/{project_name}')
    schemas = []
    
    # return all schemas if class_lst is empty
    if class_lst is None or len(class_lst) == 0:
        schemas = [file for file in project_schemas if 'Test' not in file and not file.endswith('_python_partial.json')]
        return schemas

    for class_name in class_lst:
        schemas = ([s for s in project_schemas if s.endswith(f'.{class_name}.json')])
    return schemas

def fetch_all_class_names(schema_directory, project_name):
    project_schemas = os.listdir(f'{schema_directory}/{project_name}')
    class_names = []
    for schema in project_schemas:
        if schema.endswith('.json'):
            with open(f'{schema_directory}/{project_name}/{schema}') as f:
                data = json.load(f)
            class_names += data['classes'].keys()
    return class_names

def init_project(args, formatted_proj_name, schemas):
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

def get_destination_path(path, file_name, output_dir, is_full_path=False, path_to_main=None):
    _path = [output_dir]
    
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
        subprocess.run(['java', '-jar', 'src/compositional_glue_tests/google-java-format-1.20.0-all-deps.jar', '--skip-removing-unused-imports', '-r', file], check=True)
    except Exception as e:
        print(f"Error formatting {file}: {e}")
    return

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
        imports_string += f"import org.apache.{formatted_project_name}{_import};"

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
        imports_string += f"import org.apache.{formatted_project_name}{_import};"
        
    return return_string + "// TODO: Add other mappings", imports_string
