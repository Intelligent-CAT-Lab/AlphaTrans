import argparse
import json
import os


def main(args):

    translation_files = os.listdir(f'data/translations/{args.model_name}/{args.project_name}')

    total_fragments = 0
    total_unsuccessful = 0

    for translation_file in translation_files:

        if not translation_file.endswith('.json'):
            continue

        data = {}
        with open(f'data/translations/{args.model_name}/{args.project_name}/{translation_file}') as f:
            data = json.load(f)

        recomposed_file = '\n'.join(data['python_imports'])
        recomposed_file += '\n\n\n'

        class_order = []
        while len(class_order) != len(data['classes']):
            for class_ in data['classes']:
                if class_ in class_order:
                    continue

                if not set(data['classes'][class_]['extends']).issubset(set(class_order)) and all([x in data['classes'].keys() for x in data['classes'][class_]['extends']]):
                    continue
                
                if not set(data['classes'][class_]['implements']).issubset(set(class_order)) and all([x in data['classes'].keys() for x in data['classes'][class_]['implements']]):
                    continue                                                                                                                       
                
                if data['classes'][class_]['nests'] == []:
                    class_order.append(class_)
                    continue

                if all([x in class_order for x in data['classes'][class_]['nests']]):
                    class_order.append(class_)
        
        for class_ in class_order:

            if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                continue

            recomposed_file += data['classes'][class_]['python_class_declaration']

            if data['classes'][class_]['fields'] == {} and data['classes'][class_]['methods'] == {}:
                recomposed_file += '    pass\n\n'
                continue

            for field in data['classes'][class_]['fields']:

                # if data['classes'][class_]['fields'][field]['translation'] == None:
                #     recomposed_file += '\n'.join([''] + data['classes'][class_]['fields'][field]['partial_translation']).replace('pass', 'pass # LLM could not translate this field')
                #     total_unsuccessful += 1

                total_fragments += 1
                if type(data['classes'][class_]['fields'][field]['translation']) == str:
                    recomposed_file += data['classes'][class_]['fields'][field]['translation']
                    continue
                recomposed_file += '\n'.join(data['classes'][class_]['fields'][field]['translation'])
            
            for method in data['classes'][class_]['methods']:
                if data['classes'][class_]['methods'][method]['translation'] == None:
                    recomposed_file += '\n'.join([''] + data['classes'][class_]['methods'][method]['partial_translation']).replace('pass', 'pass # LLM could not translate this method')
                    total_unsuccessful += 1
                    continue
                recomposed_file += '\n'.join(data['classes'][class_]['methods'][method]['translation'])
                total_fragments += 1

        import_map = {'urllib': 'import urllib\n', 'sys': 'import sys\n'}

        python_imports = data['python_imports']
        for key in import_map:
            if key in recomposed_file and import_map[key] not in recomposed_file:
                recomposed_file = recomposed_file.replace('from __future__ import annotations\n', 'from __future__ import annotations\n' + import_map[key])
                python_imports.append(import_map[key].strip())

        formatted_schema_fname = '.'.join(translation_file.split('.')[:-1])
        sub_dir = "/".join(formatted_schema_fname.replace(".", "/").split("/")[1:-1])
        os.makedirs(f'data/recomposed_projects/{args.model_name}/{args.project_name}/{sub_dir}', exist_ok=True)
        file_path = f"data/recomposed_projects/{args.model_name}/{args.project_name}/{sub_dir}/{formatted_schema_fname.split('.')[-1].replace('_translation', '')}.py"
        with open(file_path, 'w') as f:
            f.write(recomposed_file)
        
        os.system(f'python3 -m black {file_path}')

    # add __init__.py files for each subdirectory
    for translation_file in translation_files:
        formatted_schema_fname = '.'.join(translation_file.split('.')[:-1])
        sub_dir = "/".join(formatted_schema_fname.replace(".", "/").split("/")[1:-1])
        os.makedirs(f'data/recomposed_projects/{args.model_name}/{args.project_name}/{sub_dir}', exist_ok=True)

        sub_dirs = sub_dir.split('/')
        for i in range(len(sub_dirs)):
            current_sub_dir = '/'.join(sub_dirs[:i+1])
            with open(f'data/recomposed_projects/{args.model_name}/{args.project_name}/{current_sub_dir}/__init__.py', 'w') as f:
                f.write('')

        file_path = f"data/recomposed_projects/{args.model_name}/{args.project_name}/{sub_dir}/__init__.py"
        with open(file_path, 'w') as f:
            f.write('')

    print(f'total fragments: {total_fragments}, total unsuccessful: {total_unsuccessful}')
    print(f'percentage unsuccessful: {total_unsuccessful / total_fragments * 100}%')
    print(f'percentage successful: {100 - total_unsuccessful / total_fragments * 100}%')


if __name__ == '__main__':
    parser_ = argparse.ArgumentParser(description='Translate java types to python types')
    parser_.add_argument('--project_name', type=str, dest='project_name', help='project name to translate')
    parser_.add_argument('--model_name', type=str, dest='model_name', help='model name to translate')
    args = parser_.parse_args()
    main(args)
