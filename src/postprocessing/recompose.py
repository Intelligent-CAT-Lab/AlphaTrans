import argparse
import json
import os


def main(args):

    schema_files = os.listdir(f'data/schemas/{args.project_name}')

    total_fragments = 0
    total_unsuccessful = 0

    for schema in schema_files:

        if not schema.endswith('_python_partial.json'):
            continue

        data = {}
        with open(f'data/schemas/{args.project_name}/{schema}') as f:
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
        
        class_initialize_methods = []
        for class_ in class_order:

            if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                continue

            if 'src.test' in schema and class_.endswith('Test'):
                recomposed_file = recomposed_file.replace('from __future__ import annotations\n', 'from __future__ import annotations\nimport unittest\nimport pytest\n') if 'import unittest\nimport pytest' not in recomposed_file else recomposed_file
                if '):' not in data['classes'][class_]['python_class_declaration']:
                    recomposed_file += data['classes'][class_]['python_class_declaration'].replace(':', '(unittest.TestCase):')
                else:
                    recomposed_file += data['classes'][class_]['python_class_declaration'].replace('):', ', unittest.TestCase):')
            else:
                recomposed_file += data['classes'][class_]['python_class_declaration']

            if data['classes'][class_]['fields'] == {} and data['classes'][class_]['methods'] == {}:
                recomposed_file += '    pass\n\n'
                continue

            field_val = {}
            for field in data['classes'][class_]['fields']:
                if data['classes'][class_]['fields'][field]['translation'] == None:
                    data['classes'][class_]['fields'][field]['translation'] = data['classes'][class_]['fields'][field]['partial_translation'].replace('<placeholder>', 'None # LLM could not translate this field')
                translation = '\n'.join(data['classes'][class_]['fields'][field]['translation']).strip()
                field_name = translation[:translation.find(':')].strip()
                field_value = ''.join(translation.split('=')[1:]).strip()
                field_val[field_name] = {'value': field_value, 'key': field}

            field_order = []
            dependent_fields = []
            for field in field_val:
                found_dependency = False
                for token in field_val[field]['value'].split():
                    if token in field_val:
                        dependent_fields.append(field_val[field]['key'])
                        found_dependency = True
                        break
                
                if found_dependency:
                    continue
                field_order.append(field_val[field]['key'])
            
            field_order += dependent_fields

            intialize_later_fields = []
            for field in field_order:

                total_fragments += 1
                if data['classes'][class_]['fields'][field]['translation'] == None:
                    recomposed_file += '\n'.join([''] + data['classes'][class_]['fields'][field]['partial_translation']).replace('<placeholder>', 'None # LLM could not translate this field')
                    total_unsuccessful += 1
                    continue

                if type(data['classes'][class_]['fields'][field]['translation']) == str:
                    recomposed_file += data['classes'][class_]['fields'][field]['translation']
                    continue

                field_translation = '\n'.join(data['classes'][class_]['fields'][field]['translation'])

                found = False
                for a_class in class_order:
                    if f'{a_class}(' in field_translation:
                        intialize_later_fields.append((field, field_translation.split('=')[0].strip(), field_translation.split('=')[1].strip()))
                        recomposed_file += data['classes'][class_]['fields'][field]['partial_translation'].replace('<placeholder>', f'None')
                        found = True
                
                if found:
                    continue

                recomposed_file += '\n'.join(data['classes'][class_]['fields'][field]['translation'])
            
            # create static method for field initialization
            if intialize_later_fields != []:
                recomposed_file += f'\n\n    @staticmethod\n    def initialize_fields() -> None:\n'
                for field, field_name, field_value in intialize_later_fields:
                    recomposed_file += '    ' + data['classes'][class_]['fields'][field]['partial_translation'].replace(f'{field_name}', f'{class_}.{field_name}').replace('<placeholder>', f'{field_value}\n')
                class_initialize_methods.append(f'{class_}.initialize_fields()')
            
            for method in data['classes'][class_]['methods']:

                if 'Ignore' in data['classes'][class_]['methods'][method]['annotations']:
                    recomposed_file += '\n    @pytest.mark.skip(reason="Ignore")\n'

                if data['classes'][class_]['methods'][method]['translation'] == None:
                    recomposed_file += '\n'.join([''] + data['classes'][class_]['methods'][method]['partial_translation']).replace('pass', 'pass # LLM could not translate this method')
                    total_unsuccessful += 1
                    continue
                recomposed_file += '\n'.join(data['classes'][class_]['methods'][method]['translation'])
                total_fragments += 1

        for initialize_method in class_initialize_methods:
            recomposed_file += f'\n\n{initialize_method}'

        import_map = {'urllib': 'import urllib\n', 'sys': 'import sys\n', 'mock': 'import mock\n', 'cmp_to_key': 'from functools import cmp_to_key\n', 'field': 'from dataclasses import field\n'}

        python_imports = data['python_imports']
        for key in import_map:
            if key in recomposed_file and import_map[key] not in recomposed_file:
                recomposed_file = recomposed_file.replace('from __future__ import annotations\n', 'from __future__ import annotations\n' + import_map[key])
                python_imports.append(import_map[key].strip())
        
        exception_map = {'IllegalArgumentException': 'ValueError', 'RuntimeException': 'RuntimeError', 'UnsupportedOperationException': 'NotImplementedError',
                         'CloneNotSupportedError': 'NotImplementedError', 'IllegalStateException': 'RuntimeError'}
        
        for key in exception_map:
            if key in recomposed_file:
                recomposed_file = recomposed_file.replace(key, exception_map[key])

        formatted_schema_fname = '.'.join(schema.split('.')[:-1])
        sub_dir = "/".join(formatted_schema_fname.replace(".", "/").split("/")[1:-1])
        os.makedirs(f'data/recomposed_projects/{args.model_name}/{args.project_name}/{sub_dir}', exist_ok=True)
        file_path = f"data/recomposed_projects/{args.model_name}/{args.project_name}/{sub_dir}/{formatted_schema_fname.split('.')[-1].replace('_python_partial', '')}.py"
        with open(file_path, 'w') as f:
            f.write(recomposed_file)
        
        os.system(f'python3 -m black {file_path}')

    # add __init__.py files for each subdirectory
    for schema in schema_files:
        formatted_schema_fname = '.'.join(schema.split('.')[:-1])
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
    
    with open(f'data/recomposed_projects/{args.model_name}/{args.project_name}/pytest.ini', 'w') as f:
        f.write('# pytest.ini\n\n[pytest]\n# Require at least this version of pytest\nminversion = 8.2.1\n\n# Add options to control the pytest output\naddopts = -ra -q --continue-on-collection-errors --tb=no --junitxml=pytest-report.xml\n\n# Define directories to look for tests\ntestpaths = src/test\n\npython_files = *.py\n\npython_classes = *Test\n\npython_functions = test*')
    
    with open(f'data/recomposed_projects/{args.model_name}/{args.project_name}/run.sh', 'w') as f:
        f.write('python3 -m pytest\nxmllint --format pytest-report.xml -o pytest-report.xml')

    print(f'total fragments: {total_fragments}, total unsuccessful: {total_unsuccessful}')
    print(f'percentage unsuccessful: {total_unsuccessful / total_fragments * 100}%')
    print(f'percentage successful: {100 - total_unsuccessful / total_fragments * 100}%')


if __name__ == '__main__':
    parser_ = argparse.ArgumentParser(description='Translate java types to python types')
    parser_.add_argument('--project_name', type=str, dest='project_name', help='project name to translate')
    parser_.add_argument('--model_name', type=str, dest='model_name', help='model name to translate')
    args = parser_.parse_args()
    main(args)
