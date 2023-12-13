import json
import os
import argparse


def main(args):

    project = 'preprocessed_commons-cli'

    method_call_graph = []
    with open('data/query_outputs/preprocessed_call_graph.txt') as f:
        method_call_graph = f.readlines()
    
    for line in method_call_graph:
        splitted_line = [x.strip() for x in line.split('|') if x.strip() != '']

        if len(splitted_line) != 5:
            continue

        call_location, caller_name, caller_location, callee_name, callee_location = splitted_line

        if call_location == caller_location:
            continue

        if callee_location.endswith(':0:0:0:0') or caller_name in ['<obinit>', '<clinit>'] or callee_name in ['<obinit>', '<clinit>']:
            continue

        callee_path = callee_location[callee_location.find(':')+1:callee_location.find(':', callee_location.find(':')+1)]
        callee_path = callee_path[callee_path.find(project):]

        caller_path = caller_location[caller_location.find(':')+1:caller_location.find(':', caller_location.find(':')+1)]
        caller_path = caller_path[caller_path.find(project):]

        caller_start_line = int(caller_location[caller_location.find(':', caller_location.find(':')+1)+1:].split(':')[0])
        callee_start_line = int(callee_location[callee_location.find(':', callee_location.find(':')+1)+1:].split(':')[0])

        caller_schema_name = caller_path.split('/')[-1].split('.')[0]
        callee_schema_name = callee_path.split('/')[-1].split('.')[0]

        callee_method_class_name, callee_method_key_name = None, None
        callee_schema = {}
        is_available = False
        with open(f'data/schemas/{callee_schema_name}.json') as f:
            callee_schema = json.load(f)
            for class_ in callee_schema['classes']:

                if callee_name == class_ and callee_start_line == callee_schema['classes'][class_]['start']:
                    callee_method_class_name = class_
                    callee_method_key_name = class_
                    is_available = True
                    break

                for method in callee_schema['classes'][class_]['methods']:
                    if callee_name == method.split(':')[1] and callee_start_line == callee_schema['classes'][class_]['methods'][method]['start']:                        
                        callee_method_class_name = class_
                        callee_method_key_name = method
                        is_available = True
                        break

        assert is_available, f'callee is not available: {callee_name}'

        caller_schema = {}
        is_available = False
        with open(f'data/schemas/{caller_schema_name}.json') as f:
            caller_schema = json.load(f)
            for class_ in caller_schema['classes']:

                for method in caller_schema['classes'][class_]['methods']:
                    if caller_name == method.split(':')[1] and caller_start_line == caller_schema['classes'][class_]['methods'][method]['start']:
                        if [callee_schema_name, callee_method_class_name, callee_method_key_name] not in caller_schema['classes'][class_]['methods'][method]['calls']:
                            caller_schema['classes'][class_]['methods'][method]['calls'].append((callee_schema_name, callee_method_class_name, callee_method_key_name))
                        is_available = True
                        break

        assert is_available, f'caller is not available: {caller_name}'

        with open(f'data/schemas/{caller_schema_name}.json', 'w') as f:
            json.dump(caller_schema, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='extract call graph of preprocessed project')
    args = parser.parse_args()
    main(args)
