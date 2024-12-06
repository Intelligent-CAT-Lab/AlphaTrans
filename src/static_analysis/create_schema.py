import os
import json
import argparse


def create_schema(args):
    project = args.project_name
    projects_dir = f'java_projects/cleaned_final_projects{args.suffix}/'
    query_outputs_dir = f'data/query_outputs{args.suffix}'
    os.makedirs(f'data/schemas{args.suffix}/{project}', exist_ok=True)
    schemas = {}

    imports_query_out = f'{query_outputs_dir}/{project}/{project}_imports.txt'
    lines = []
    with open(imports_query_out, 'r') as f:
        lines = f.readlines()

    for line in lines:
        res_row = line.split('|')[1:-1]
        import_name, start = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = projects_dir + path[path.find(project):]

        schemas.setdefault(path, {})

        start_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[0])
        end_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[2])

        import_body = ''
        with open(path, 'r') as f:
            import_body = f.readlines()[start_line-1:end_line]

        schemas[path].setdefault("path", path)
        schemas[path].setdefault("imports", {})
        schemas[path].setdefault("classes", {})
        schemas[path]["imports"].setdefault(f'{start_line}-{end_line}:{import_name}', {"start": start_line,
                                                                                       "end": end_line,
                                                                                       "body": import_body,})

    callables_query_out = f'{query_outputs_dir}/{project}/{project}_class_callables.txt'
    lines = []
    with open(callables_query_out, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        res_row = line.split('|')[1:-1]
        class_name, class_location, callable_name, modifier, return_type, return_type_qualified_name, signature, annotation_location, start, end = [x.strip() for x in res_row]

        if callable_name in ['<clinit>', '<obinit>']:
            continue

        assert '<clinit>' not in callable_name and '<obinit>' not in callable_name

        if start.endswith('0:0:0:0') or end.endswith('0:0:0:0'):
            continue

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = projects_dir + path[path.find(project):]

        schemas.setdefault(path, {})

        start_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[0]) - 1
        end_line = int(end[end.find(':', end.find(':')+1)+1:].split(':')[2])

        class_start_line = int(class_location[class_location.find(':', class_location.find(':')+1)+1:].split(':')[0])
        class_end_line = int(class_location[class_location.find(':', class_location.find(':')+1)+1:].split(':')[2])

        if 'new' not in class_name and '{' not in class_name:
            class_declaration = ''
            with open(path, 'r') as f:
                class_declaration = f.readlines()[class_start_line-1:class_end_line]

            if class_start_line == class_end_line:
                changed = False
                while '{' not in ''.join(class_declaration):
                    class_declaration = ''
                    with open(path, 'r') as f:
                        class_declaration = f.readlines()[class_start_line-1:class_end_line]
                    class_end_line += 1
                    changed = True

                if changed:
                    class_end_line -= 1

        callable_body = ''
        with open(path, 'r') as f:
            callable_body = f.readlines()[start_line-1:end_line]

        start_terminations = ['*/', '@', '}']
        end_terminations = [';', '}', '*/', '{']
        searched = False
        while not (any([callable_body[0].strip().startswith(x) for x in start_terminations]) 
                or any([callable_body[0].strip().endswith(x) for x in end_terminations])):

            searched = True
            
            callable_body = ''
            with open(path, 'r') as f:
                callable_body = f.readlines()[start_line-1:end_line]
            start_line -= 1
        
        if searched:
            start_line += 2

            callable_body = ''
            with open(path, 'r') as f:
                callable_body = f.readlines()[start_line-1:end_line]
            
            for i in range(len(callable_body)):
                if callable_body[i].strip() == '':
                    start_line += 1
                if callable_body[i].strip() != '':
                    break
        else:
            start_line += 1

        callable_body = ''
        with open(path, 'r') as f:
            callable_body = f.readlines()[start_line-1:end_line]

        if start == end:
            while ';' not in ''.join(callable_body) and '{' not in ''.join(callable_body):
                callable_body = ''
                with open(path, 'r') as f:
                    callable_body = f.readlines()[start_line-1:end_line]
                end_line += 1

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
        # schemas[path]["classes"][class_name].setdefault("static_initializers", {})
        pos_callable_name = f'{start_line}-{end_line}:{callable_name}'
        schemas[path]["classes"][class_name].setdefault("methods", {})

        if 'public class' in ''.join(callable_body) or 'public static class' in ''.join(callable_body):
            continue

        already_exists = False
        for method in schemas[path]["classes"][class_name]["methods"].keys():
            if callable_name in method \
                and start_line == schemas[path]["classes"][class_name]["methods"][method]["start"] \
                and end_line != schemas[path]["classes"][class_name]["methods"][method]["end"]:
                
                already_exists = True
                break

        if already_exists:
            continue

        schemas[path]["classes"][class_name]["methods"].setdefault(pos_callable_name, {"start": start_line,
                                                                            "end": end_line,
                                                                            "body": callable_body,
                                                                            "is_constructor": False,
                                                                            "annotations": [],
                                                                            "modifiers": [],
                                                                            "return_types": [],
                                                                            "signature": signature,
                                                                            "parameters": [],
                                                                            "calls": []})

        return_type_qualified = ''
        if 'java' in return_type_qualified_name:
            temp_name = return_type_qualified_name[return_type_qualified_name.find('java'):].replace('/', '.').replace(';', '')
            return_type_qualified = '.'.join(temp_name.split('.')[:-1]) + '.' + return_type
        else:
            return_type_qualified = return_type

        if (return_type, return_type_qualified) not in schemas[path]["classes"][class_name]["methods"][pos_callable_name]["return_types"]:
            schemas[path]["classes"][class_name]["methods"][pos_callable_name]["return_types"].append((return_type, return_type_qualified))

        if modifier not in schemas[path]["classes"][class_name]["methods"][pos_callable_name]["modifiers"] and modifier != 'null':
            schemas[path]["classes"][class_name]["methods"][pos_callable_name]["modifiers"].append(modifier)

        if callable_name == class_name:
            schemas[path]["classes"][class_name]["methods"][pos_callable_name]['is_constructor'] = True
        
        if annotation_location != 'null':
            annotation_path = annotation_location[annotation_location.find(':')+1:annotation_location.find(':', annotation_location.find(':')+1)]
            annotation_start_line = int(annotation_location[annotation_location.find(':', annotation_location.find(':')+1)+1:].split(':')[0])
            annotation_end_line = int(annotation_location[annotation_location.find(':', annotation_location.find(':')+1)+1:].split(':')[2])
            annotation_start_col = int(annotation_location[annotation_location.find(':', annotation_location.find(':')+1)+1:].split(':')[1])
            annotation_end_col = int(annotation_location[annotation_location.find(':', annotation_location.find(':')+1)+1:].split(':')[3])
            annotation_body = ''
            with open(annotation_path, 'r') as f:
                annotation_body = f.readlines()[annotation_start_line-1:annotation_end_line][0]
                annotation_body = annotation_body[annotation_start_col:annotation_end_col]
            schemas[path]["classes"][class_name]["methods"][pos_callable_name]["annotations"].append(annotation_body)

    interfaces_query_out = f'{query_outputs_dir}/{project}/{project}_interfaces.txt'
    lines = []
    with open(interfaces_query_out, 'r') as f:
        lines = f.readlines()

    for line in lines:
        res_row = line.split('|')[1:-1]
        interface_name, interface_loc, callable_name, modifier, return_type, return_type_qualified_name, siganture, start, end = [x.strip() for x in res_row]

        if callable_name in ['<clinit>', '<obinit>']:
            continue

        if callable_name == 'null' and modifier == 'null' and return_type == 'null' and return_type_qualified_name == 'null' and siganture == 'null':
            path = interface_loc[interface_loc.find(':')+1:interface_loc.find(':', interface_loc.find(':')+1)]
            path = projects_dir + path[path.find(project):]
            schemas.setdefault(path, {})
            interface_start_line = int(interface_loc[interface_loc.find(':', interface_loc.find(':')+1)+1:].split(':')[0])
            interface_end_line = int(interface_loc[interface_loc.find(':', interface_loc.find(':')+1)+1:].split(':')[2])
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
            # schemas[path]["classes"][interface_name].setdefault("static_initializers", {})
            schemas[path]["classes"][interface_name].setdefault("methods", {})
            continue

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = projects_dir + path[path.find(project):]

        schemas.setdefault(path, {})

        start_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[0]) - 1
        end_line = int(end[end.find(':', end.find(':')+1)+1:].split(':')[2])

        interface_start_line = int(interface_loc[interface_loc.find(':', interface_loc.find(':')+1)+1:].split(':')[0])
        interface_end_line = int(interface_loc[interface_loc.find(':', interface_loc.find(':')+1)+1:].split(':')[2])

        callable_body = ''
        with open(path, 'r') as f:
            callable_body = f.readlines()[start_line-1:end_line]

        start_terminations = ['*/', '@', '}']
        end_terminations = [';', '}', '*/', '{']
        searched = False
        while not (any([callable_body[0].strip().startswith(x) for x in start_terminations]) 
                or any([callable_body[0].strip().endswith(x) for x in end_terminations])):

            searched = True
            
            callable_body = ''
            with open(path, 'r') as f:
                callable_body = f.readlines()[start_line-1:end_line]
            start_line -= 1
        
        if searched:
            start_line += 2

            callable_body = ''
            with open(path, 'r') as f:
                callable_body = f.readlines()[start_line-1:end_line]
            
            for i in range(len(callable_body)):
                if callable_body[i].strip() == '':
                    start_line += 1
                if callable_body[i].strip() != '':
                    break
        else:
            start_line += 1

        callable_body = ''
        with open(path, 'r') as f:
            callable_body = f.readlines()[start_line-1:end_line]

        if start == end:
            while ';' not in ''.join(callable_body) and '{' not in ''.join(callable_body):
                callable_body = ''
                with open(path, 'r') as f:
                    callable_body = f.readlines()[start_line-1:end_line]
                end_line += 1
        
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
        # schemas[path]["classes"][interface_name].setdefault("static_initializers", {})
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
                                                                                "parameters": [],
                                                                                "calls": []})

        return_type_qualified = ''
        if 'java' in return_type_qualified_name:
            temp_name = return_type_qualified_name[return_type_qualified_name.find('java'):].replace('/', '.').replace(';', '')
            return_type_qualified = '.'.join(temp_name.split('.')[:-1]) + '.' + return_type
        else:
            return_type_qualified = return_type

        if (return_type, return_type_qualified) not in schemas[path]["classes"][interface_name]["methods"][pos_callable_name]["return_types"]:
            schemas[path]["classes"][interface_name]["methods"][pos_callable_name]["return_types"].append((return_type, return_type_qualified))

        if modifier not in schemas[path]["classes"][interface_name]["methods"][pos_callable_name]["modifiers"]:
            schemas[path]["classes"][interface_name]["methods"][pos_callable_name]["modifiers"].append(modifier)

        if callable_name == interface_name:
            schemas[path]["classes"][interface_name]["methods"][pos_callable_name]['is_constructor'] = True

    for path in schemas.keys():
        for class_ in schemas[path]["classes"].keys():
            schemas[path]["classes"][class_].setdefault("fields", {})

    fields_query_out = f'{query_outputs_dir}/{project}/{project}_fields.txt'
    lines = []
    with open(fields_query_out, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        res_row = line.split('|')[1:-1]
        field_name, modifier, return_type, return_type_qualified_name, start, class_name = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = projects_dir + path[path.find(project):]

        schemas.setdefault(path, {})

        start_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[0])
        end_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[2])

        field_body = ''
        with open(path, 'r') as f:
            field_body = f.readlines()[start_line-1:end_line]

        schemas[path]["classes"][class_name].setdefault("fields", {})
        schemas[path]["classes"][class_name]["fields"].setdefault(f'{start_line}-{end_line}:{field_name}', {"start": start_line,
                                                                                                            "end": end_line,
                                                                                                            "body": field_body,
                                                                                                            "modifiers": [],
                                                                                                            "types": []})
        return_type_qualified = ''
        if 'java' in return_type_qualified_name:
            temp_name = return_type_qualified_name[return_type_qualified_name.find('java'):].replace('/', '.').replace(';', '')
            return_type_qualified = '.'.join(temp_name.split('.')[:-1]) + '.' + return_type
        else:
            return_type_qualified = return_type

        if (return_type, return_type_qualified) not in schemas[path]["classes"][class_name]["fields"][f'{start_line}-{end_line}:{field_name}']["types"]:
            schemas[path]["classes"][class_name]["fields"][f'{start_line}-{end_line}:{field_name}']["types"].append((return_type, return_type_qualified))

        if modifier not in schemas[path]["classes"][class_name]["fields"][f'{start_line}-{end_line}:{field_name}']["modifiers"] and modifier != 'null':
            schemas[path]["classes"][class_name]["fields"][f'{start_line}-{end_line}:{field_name}']["modifiers"].append(modifier)

    classes_query_out = f'{query_outputs_dir}/{project}/{project}_superclasses.txt'
    lines = []
    with open(classes_query_out, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        res_row = line.split('|')[1:-1]
        class_name, is_abstract, parent_class, start = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = projects_dir + path[path.find(project):]

        if path.endswith('.class') or 'new' in class_name or '{' in class_name:
            continue

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

    static_initializers_query_out = f'{query_outputs_dir}/{project}/{project}_static_initializers.txt'
    lines = []
    with open(static_initializers_query_out, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        res_row = line.split('|')[1:-1]
        class_name, start = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = projects_dir + path[path.find(project):]

        start_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[0])
        end_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[2])

        static_initializer_body = ''
        with open(path, 'r') as f:
            static_initializer_body = f.readlines()[start_line-1:end_line]

        schemas[path]["classes"][class_name].setdefault("static_initializers", {})
        schemas[path]["classes"][class_name]["static_initializers"].setdefault(f'{start_line}-{end_line}:run_static_init', {"start": start_line,
                                                                                                                            "end": end_line,
                                                                                                                            "body": static_initializer_body})

    nested_classes_query_out = f'{query_outputs_dir}/{project}/{project}_nested_classes.txt'
    lines = []
    with open(nested_classes_query_out, 'r') as f:
        lines = f.readlines()

    for line in lines:
        res_row = line.split('|')[1:-1]
        class_name, start, nested_inside = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = projects_dir + path[path.find(project):]

        schemas[path]["classes"][class_name]["nested_inside"] = nested_inside
        schemas[path]["classes"][nested_inside]["nests"].append(class_name)

    parameters = f'{query_outputs_dir}/{project}/{project}_parameters.txt'
    lines = []
    with open(parameters, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        res_row = line.split('|')[1:-1]
        class_name, method_name, parameter_name, start, end = [x.strip() for x in res_row]

        path = start[start.find(':')+1:start.find(':', start.find(':')+1)]
        path = projects_dir + path[path.find(project):]

        start_line = int(start[start.find(':', start.find(':')+1)+1:].split(':')[0]) - 1
        end_line = int(end[end.find(':', end.find(':')+1)+1:].split(':')[2])

        callable_body = ''
        with open(path, 'r') as f:
            callable_body = f.readlines()[start_line-1:end_line]

        start_terminations = ['*/', '@', '}']
        end_terminations = [';', '}', '*/', '{']
        searched = False
        while not (any([callable_body[0].strip().startswith(x) for x in start_terminations]) 
                or any([callable_body[0].strip().endswith(x) for x in end_terminations])):

            searched = True
            
            callable_body = ''
            with open(path, 'r') as f:
                callable_body = f.readlines()[start_line-1:end_line]
            start_line -= 1
        
        if searched:
            start_line += 2

            callable_body = ''
            with open(path, 'r') as f:
                callable_body = f.readlines()[start_line-1:end_line]
            
            for i in range(len(callable_body)):
                if callable_body[i].strip() == '':
                    start_line += 1
                if callable_body[i].strip() != '':
                    break
        else:
            start_line += 1

        callable_body = ''
        with open(path, 'r') as f:
            callable_body = f.readlines()[start_line-1:end_line]

        if start == end:
            while ';' not in ''.join(callable_body) and '{' not in ''.join(callable_body):
                callable_body = ''
                with open(path, 'r') as f:
                    callable_body = f.readlines()[start_line-1:end_line]
                end_line += 1

        schemas[path]["classes"][class_name]["methods"][f'{start_line}-{end_line}:{method_name}']["parameters"].append(parameter_name)

    for path_ in schemas.copy().keys():
        for class_ in schemas[path_]["classes"].copy().keys():
            for method_ in schemas[path_]["classes"][class_]["methods"].copy().keys():
                if schemas[path_]["classes"][class_]["methods"][method_]["is_constructor"]:
                    if method_ == f'{schemas[path_]["classes"][class_]["start"]}-{schemas[path_]["classes"][class_]["end"]}:{class_}':
                        schemas[path_]["classes"][class_]["methods"].pop(method_)

    for k,v in schemas.items():
        key = k[k.find(project):].replace('/', '.')
        if args.suffix == '_evosuite' and 'ESTest' not in key:
            continue
        key = key.replace('.java', '')
        with open(f'data/schemas{args.suffix}/{project}/{key}.json', 'w') as f:
            json.dump(v, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create schema for the project')
    parser.add_argument('--project_name', type=str, help='Name of the project')
    parser.add_argument('--suffix', type=str, help='suffix')
    args = parser.parse_args()
    create_schema(args)
