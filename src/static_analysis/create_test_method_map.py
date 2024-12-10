import os
import json
import argparse


def main(args):

    schema_dir = f'data/schemas{args.suffix}'

    os.makedirs(f'data/call_graphs/{args.project_name}', exist_ok=True)

    global_call_graph = {}
    for schema_file in os.listdir(f'{schema_dir}/translations/deepseek-coder-33b-instruct/body/0.0/{args.project_name}'):

        if 'ESTest' in schema_file and not args.evosuite:
            continue

        if 'ESTest' not in schema_file and args.evosuite:
            continue

        data = {}
        with open(f'{schema_dir}/translations/deepseek-coder-33b-instruct/body/0.0/{args.project_name}/{schema_file}', 'r') as f:
            data = json.load(f)
        
        for class_ in data['classes']:

            if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                continue

            global_call_graph.setdefault(class_, {'schema_file': data['path']})

            for method_ in data['classes'][class_]['methods']:
                global_call_graph[class_].setdefault(method_, [])
                for call_ in data['classes'][class_]['methods'][method_]['calls']:
                    if ':' not in call_[2]:
                        continue
                    global_call_graph[class_][method_].append({'schema': call_[0], 'class': call_[1], 'method': call_[2]})

        suffix = '-evosuite' if args.evosuite else ''
        with open(f'data/call_graphs/{args.project_name}/call_graph{suffix}.json', 'w') as f:
            json.dump(global_call_graph, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create call graph for test methods')
    parser.add_argument('--project_name', type=str, help='Name of the project')
    parser.add_argument('--evosuite', action='store_true', help='Use evosuite schemas')
    parser.add_argument('--suffix', type=str, default='', help='Suffix for schema directory')
    args = parser.parse_args()
    main(args)
