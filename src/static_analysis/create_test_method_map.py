import os
import json
import argparse


def main(args):

    schema_dir = f'data/schemas'
    for project_name in os.listdir(schema_dir):

        os.makedirs(f'data/call_graphs/{project_name}', exist_ok=True)

        global_call_graph = {}
        for schema_file in os.listdir(f'{schema_dir}/{project_name}'):

            if not schema_file.endswith('_python_partial.json'):
                continue

            data = {}
            with open(f'{schema_dir}/{project_name}/{schema_file}', 'r') as f:
                data = json.load(f)
            
            for class_ in data['classes']:

                if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                    continue

                global_call_graph.setdefault(class_, {'schema_file': data['path']})

                for method_ in data['classes'][class_]['methods']:
                    global_call_graph[class_].setdefault(method_, [])
                    for call_ in data['classes'][class_]['methods'][method_]['calls']:
                        global_call_graph[class_][method_].append({'schema': call_[0], 'class': call_[1], 'method': call_[2]})

            with open(f'data/call_graphs/{project_name}/call_graph.json', 'w') as f:
                json.dump(global_call_graph, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create call graph for test methods')
    args = parser.parse_args()
    main(args)
