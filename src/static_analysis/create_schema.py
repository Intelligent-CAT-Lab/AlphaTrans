import os
import json
import sys


def create_schema():
    project = sys.argv[1]
    os.makedirs('data/schemas', exist_ok=True)
    schemas = {}

    imports_query_out = 'data/query_outputs/imports.txt'
    lines = []
    with open(imports_query_out, 'r') as f:
        lines = f.readlines()

    for line in lines[2:]:
        res_row = line.split('|')[1:-1]
        import_name, start = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = path[path.find(f'preprocessed_{project}'):]

        schemas.setdefault(path, {})

        start_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[0])
        end_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[2])

        import_body = ''
        with open(path, 'r') as f:
            import_body = f.readlines()[start_line-1:end_line]

        schemas[path].setdefault("path", path)
        schemas[path].setdefault("imports", {})
        schemas[path]["imports"].setdefault(f'{start_line}-{end_line}:{import_name}', {"start": start_line,
                                                                                       "end": end_line,
                                                                                       "body": import_body,})

    callables_query_out = 'data/query_outputs/class_callables.txt'
    lines = []
    with open(callables_query_out, 'r') as f:
        lines = f.readlines()
    
    for line in lines[2:]:
        res_row = line.split('|')[1:-1]
        class_name, class_location, callable_name, modifier, return_type, signature, annotation, start, end = [x.strip() for x in res_row]

        if callable_name in ['<clinit>', '<obinit>']:
            continue

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = path[path.find(f'preprocessed_{project}'):]

        schemas.setdefault(path, {})

        start_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[0])
        end_line = int(end[end.find(':', end.find(':')+1)+1:].split(':')[2])

        class_start_line = int(class_location[class_location.find(':', class_location.find(':')+1)+1:].split(':')[0])
        class_end_line = int(class_location[class_location.find(':', class_location.find(':')+1)+1:].split(':')[2])

        callable_body = ''
        with open(path, 'r') as f:
            callable_body = f.readlines()[start_line-1:end_line]

        schemas[path].setdefault("path", path)
        schemas[path].setdefault("imports", {})
        schemas[path].setdefault("classes", {})
        schemas[path]["classes"].setdefault(class_name, {})
        schemas[path]["classes"][class_name].setdefault("start", class_start_line)
        schemas[path]["classes"][class_name].setdefault("end", class_end_line)
        schemas[path]["classes"][class_name].setdefault("is_abstract", False)
        schemas[path]["classes"][class_name].setdefault("is_interface", False)
        schemas[path]["classes"][class_name].setdefault("nested_inside", [])
        schemas[path]["classes"][class_name].setdefault("nests", [])
        schemas[path]["classes"][class_name].setdefault("implements", [])
        schemas[path]["classes"][class_name].setdefault("extends", [])
        pos_callable_name = f'{start_line}-{end_line}:{callable_name}'
        schemas[path]["classes"][class_name].setdefault("methods", {})

        if 'public class' in ''.join(callable_body) or 'public static class' in ''.join(callable_body):
            continue

        schemas[path]["classes"][class_name]["methods"].setdefault(pos_callable_name, {"start": start_line,
                                                                            "end": end_line,
                                                                            "body": callable_body,
                                                                            "is_constructor": False,
                                                                            "annotations": [] if annotation == 'null' else [annotation],
                                                                            "modifiers": [],
                                                                            "return_types": [],
                                                                            "signature": signature,
                                                                            "parameters": []})

        if return_type not in schemas[path]["classes"][class_name]["methods"][pos_callable_name]["return_types"]:
            schemas[path]["classes"][class_name]["methods"][pos_callable_name]["return_types"].append(return_type)

        if modifier not in schemas[path]["classes"][class_name]["methods"][pos_callable_name]["modifiers"] and modifier != 'null':
            schemas[path]["classes"][class_name]["methods"][pos_callable_name]["modifiers"].append(modifier)

        if callable_name == class_name:
            schemas[path]["classes"][class_name]["methods"][pos_callable_name]['is_constructor'] = True

    interfaces_query_out = 'data/query_outputs/interfaces.txt'
    lines = []
    with open(interfaces_query_out, 'r') as f:
        lines = f.readlines()

    for line in lines[2:]:
        res_row = line.split('|')[1:-1]
        interface_name, interface_loc, callable_name, modifier, return_type, siganture, start = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = path[path.find(f'preprocessed_{project}'):]

        schemas.setdefault(path, {})

        start_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[0])
        end_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[2])

        interface_start_line = int(interface_loc[interface_loc.find(':', interface_loc.find(':')+1)+1:].split(':')[0])
        interface_end_line = int(interface_loc[interface_loc.find(':', interface_loc.find(':')+1)+1:].split(':')[2])

        callable_body = ''
        with open(path, 'r') as f:
            callable_body = f.readlines()[start_line-1:end_line]

        schemas[path].setdefault("path", path)
        schemas[path].setdefault("imports", {})
        schemas[path].setdefault("classes", {})
        schemas[path]["classes"].setdefault(interface_name, {})
        schemas[path]["classes"][interface_name].setdefault("start", interface_start_line)
        schemas[path]["classes"][interface_name].setdefault("end", interface_end_line)
        schemas[path]["classes"][interface_name].setdefault("is_abstract", False)
        schemas[path]["classes"][interface_name].setdefault("is_interface", True)
        schemas[path]["classes"][interface_name].setdefault("nested_inside", [])
        schemas[path]["classes"][interface_name].setdefault("nests", [])        
        schemas[path]["classes"][interface_name].setdefault("implements", [])
        schemas[path]["classes"][interface_name].setdefault("extends", [])
        pos_callable_name = f'{start_line}-{end_line}:{callable_name}'
        schemas[path]["classes"][interface_name].setdefault("methods", {})
        schemas[path]["classes"][interface_name]["methods"].setdefault(pos_callable_name, {"start": start_line,
                                                                                "end": end_line,
                                                                                "body": callable_body,
                                                                                "is_constructor": False,
                                                                                "annotations": [],
                                                                                "modifiers": [],
                                                                                "return_types": [],
                                                                                "signature": siganture,
                                                                                "parameters": []})

        if return_type not in schemas[path]["classes"][interface_name]["methods"][pos_callable_name]["return_types"]:
            schemas[path]["classes"][interface_name]["methods"][pos_callable_name]["return_types"].append(return_type)

        if modifier not in schemas[path]["classes"][interface_name]["methods"][pos_callable_name]["modifiers"]:
            schemas[path]["classes"][interface_name]["methods"][pos_callable_name]["modifiers"].append(modifier)

        if callable_name == interface_name:
            schemas[path]["classes"][interface_name]["methods"][pos_callable_name]['is_constructor'] = True

    for path in schemas.keys():
        for class_ in schemas[path]["classes"].keys():
            schemas[path]["classes"][class_].setdefault("fields", {})

    fields_query_out = 'data/query_outputs/fields.txt'
    lines = []
    with open(fields_query_out, 'r') as f:
        lines = f.readlines()
    
    for line in lines[2:]:
        res_row = line.split('|')[1:-1]
        field_name, modifer, return_type, start, class_name = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = path[path.find(f'preprocessed_{project}'):]

        schemas.setdefault(path, {})

        start_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[0])
        end_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[2])

        import_body = ''
        with open(path, 'r') as f:
            import_body = f.readlines()[start_line-1:end_line]

        schemas[path]["classes"][class_name].setdefault("fields", {})
        schemas[path]["classes"][class_name]["fields"].setdefault(f'{start_line}-{end_line}:{field_name}', {"start": start_line,
                                                                                                            "end": end_line,
                                                                                                            "body": import_body,
                                                                                                            "modifiers": [],
                                                                                                            "types": []})
        if return_type not in schemas[path]["classes"][class_name]["fields"][f'{start_line}-{end_line}:{field_name}']["types"]:
            schemas[path]["classes"][class_name]["fields"][f'{start_line}-{end_line}:{field_name}']["types"].append(return_type)

        if modifer not in schemas[path]["classes"][class_name]["fields"][f'{start_line}-{end_line}:{field_name}']["modifiers"]:
            schemas[path]["classes"][class_name]["fields"][f'{start_line}-{end_line}:{field_name}']["modifiers"].append(modifer)

    classes_query_out = 'data/query_outputs/superclasses.txt'
    lines = []
    with open(classes_query_out, 'r') as f:
        lines = f.readlines()
    
    for line in lines[2:]:
        res_row = line.split('|')[1:-1]
        class_name, is_abstract, parent_class, start = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = path[path.find(f'preprocessed_{project}'):]

        schemas[path]["classes"][class_name]["is_abstract"] = True if is_abstract == 'true' else False

        if parent_class == 'Object':
            continue

        class_start_line = schemas[path]["classes"][class_name]["start"]
        class_end_line = schemas[path]["classes"][class_name]["end"]

        with open(path, 'r') as f:
            file_lines = f.readlines()
            class_declaration = file_lines[class_start_line-1:class_end_line][0].split('{')[0]
        
        if 'extends' in class_declaration:
            schemas[path]["classes"][class_name]["extends"].append(parent_class)
        elif 'implements' in class_declaration:
            schemas[path]["classes"][class_name]["implements"].append(parent_class)

    nested_classes_query_out = 'data/query_outputs/nested_classes.txt'
    lines = []
    with open(nested_classes_query_out, 'r') as f:
        lines = f.readlines()

    for line in lines[2:]:
        res_row = line.split('|')[1:-1]
        class_name, start, nested_inside = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = path[path.find(f'preprocessed_{project}'):]

        schemas[path]["classes"][class_name]["nested_inside"] = nested_inside
        schemas[path]["classes"][nested_inside]["nests"].append(class_name)

    parameters = 'data/query_outputs/parameters.txt'
    lines = []
    with open(parameters, 'r') as f:
        lines = f.readlines()
    
    for line in lines[2:]:
        res_row = line.split('|')[1:-1]
        class_name, method_name, parameter_name, start, end = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = path[path.find(f'preprocessed_{project}'):]

        start_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[0])
        end_line = int(end[end.find(':', end.find(':')+1)+1:].split(':')[2])

        schemas[path]["classes"][class_name]["methods"][f'{start_line}-{end_line}:{method_name}']["parameters"].append(parameter_name)

    for k,v in schemas.items():
        key = k.split('/')[-1].split('.')[0]
        with open(f'data/schemas/{key}.json', 'w') as f:
            json.dump(v, f, indent=4)


if __name__ == '__main__':
    create_schema()
