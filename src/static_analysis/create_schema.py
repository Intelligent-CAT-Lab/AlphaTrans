import os
import json


def create_schema():
    os.makedirs('schemas', exist_ok=True)
    schemas = {}

    imports_query_out = 'query_outputs/imports.txt'
    lines = []
    with open(imports_query_out, 'r') as f:
        lines = f.readlines()

    for line in lines[2:]:
        res_row = line.split('|')[1:-1]
        import_name, start = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = path[path.find('java_projects'):]

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

    callables_query_out = 'query_outputs/callables.txt'
    lines = []
    with open(callables_query_out, 'r') as f:
        lines = f.readlines()
    
    for line in lines[2:]:
        res_row = line.split('|')[1:-1]
        class_name, class_location, callable_name, annotation, start, end = [x.strip() for x in res_row]

        if start == end:
            continue

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = path[path.find('java_projects'):]

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
        schemas[path]["classes"][class_name].setdefault("parent_class_interface", [])        
        pos_callable_name = f'{start_line}-{end_line}:{callable_name}'
        schemas[path]["classes"][class_name].setdefault("methods", {})
        schemas[path]["classes"][class_name]["methods"].setdefault(pos_callable_name, {"start": start_line,
                                                                            "end": end_line,
                                                                            "body": callable_body,
                                                                            "is_constructor": False,
                                                                            "annotations": [] if annotation == 'null' else [annotation]})

        if callable_name == class_name:
            schemas[path]["classes"][class_name]["methods"][pos_callable_name]['is_constructor'] = True

    interfaces_query_out = 'query_outputs/interfaces.txt'
    lines = []
    with open(interfaces_query_out, 'r') as f:
        lines = f.readlines()

    for line in lines[2:]:
        res_row = line.split('|')[1:-1]
        interface_name, interface_loc, callable_name, start = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = path[path.find('java_projects'):]

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
        schemas[path]["classes"][interface_name].setdefault("parent_class_interface", [])        
        pos_callable_name = f'{start_line}-{end_line}:{callable_name}'
        schemas[path]["classes"][interface_name].setdefault("methods", {})
        schemas[path]["classes"][interface_name]["methods"].setdefault(pos_callable_name, {"start": start_line,
                                                                                "end": end_line,
                                                                                "body": callable_body,
                                                                                "is_constructor": False,
                                                                                "annotations": []})
        
        if callable_name == interface_name:
            schemas[path]["classes"][interface_name]["methods"][pos_callable_name]['is_constructor'] = True

    for path in schemas.keys():
        for class_ in schemas[path]["classes"].keys():
            schemas[path]["classes"][class_].setdefault("fields", {})

    fields_query_out = 'query_outputs/fields.txt'
    lines = []
    with open(fields_query_out, 'r') as f:
        lines = f.readlines()
    
    for line in lines[2:]:
        res_row = line.split('|')[1:-1]
        field_name, start, class_name = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = path[path.find('java_projects'):]

        schemas.setdefault(path, {})

        start_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[0])
        end_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[2])

        import_body = ''
        with open(path, 'r') as f:
            import_body = f.readlines()[start_line-1:end_line]

        schemas[path]["classes"][class_name].setdefault("fields", {})
        schemas[path]["classes"][class_name]["fields"].setdefault(f'{start_line}-{end_line}:{field_name}', {"start": start_line,
                                                                                                 "end": end_line,
                                                                                                 "body": import_body,})

    classes_query_out = 'query_outputs/classes.txt'
    lines = []
    with open(classes_query_out, 'r') as f:
        lines = f.readlines()
    
    for line in lines[2:]:
        res_row = line.split('|')[1:-1]
        class_name, is_abstract, parent_class, start = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = path[path.find('java_projects'):]

        schemas[path]["classes"][class_name]["is_abstract"] = True if is_abstract == 'true' else False

        if parent_class == 'Object':
            continue

        schemas[path]["classes"][class_name]["parent_class_interface"].append(parent_class)

    nested_classes_query_out = 'query_outputs/nested_classes.txt'
    lines = []
    with open(nested_classes_query_out, 'r') as f:
        lines = f.readlines()

    for line in lines[2:]:
        res_row = line.split('|')[1:-1]
        class_name, start, nested_inside = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = path[path.find('java_projects'):]

        schemas[path]["classes"][class_name]["nested_inside"] = nested_inside

    for k,v in schemas.items():
        key = k.split('/')[-1].split('.')[0]
        with open(f'schemas/{key}.json', 'w') as f:
            json.dump(v, f, indent=4)


if __name__ == '__main__':
    create_schema()
