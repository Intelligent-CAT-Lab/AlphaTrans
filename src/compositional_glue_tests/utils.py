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
