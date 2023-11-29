import os
import json
import argparse


def main(args):

    with open('data/types.json', 'r') as f:
        extracted_types = json.load(f)

    class_name = args.class_name
    schema_path = f'data/schemas/{class_name}.json'

    dependencies = {}
    with open('data/dependencies/dependencies.json', 'r') as f:
        dependencies = json.load(f)
    
    skeletons = {}
    schema = {}
    with open(schema_path, 'r') as f:
        schema = json.load(f)

    skeleton = '// Imports Begin\n'
    for import_ in sorted(schema['imports']):
        skeleton += ''.join(schema['imports'][import_]['body'])
    skeleton += '// Imports End\n\n'

    added_classes = []

    for class_ in schema['classes']:

        if class_ in added_classes:
            continue

        file_lines = ''
        with open(schema['path'], 'r') as f:
            file_lines = f.readlines()
        
        class_start_line = schema['classes'][class_]['start']
        class_end_line = schema['classes'][class_]['end']

        class_declaration = file_lines[class_start_line-1:class_end_line][0].split('{')[0]
        skeleton += class_declaration + ' {\n\n'

        if schema['classes'][class_]['nests'] != '':

            for nested_class in schema['classes'][class_]['nests']:

                nested_class_start_line = schema['classes'][nested_class]['start']
                nested_class_end_line = schema['classes'][nested_class]['end']

                nested_class_declaration = file_lines[nested_class_start_line-1:nested_class_end_line][0].split('{')[0]
                skeleton += '\t' + nested_class_declaration.strip() + ' {\n\n'

                skeleton += '\t\t// Class Fields Begin\n'
                for field in sorted(schema['classes'][nested_class]['fields']):
                    skeleton += '\t\t' + ''.join(schema['classes'][nested_class]['fields'][field]['body']).strip() + '\n'
                skeleton += '\t\t// Class Fields End\n\n'

                skeleton += '\t\t// Class Methods Begin\n'
                for method in sorted(schema['classes'][nested_class]['methods']):
                    if schema['classes'][nested_class]['is_interface']:
                        skeleton += '\t\t' + ''.join(schema['classes'][nested_class]['methods'][method]['body']).strip().split('{')[0] + '\n'
                    else:
                        skeleton += '\t\t' + ''.join(schema['classes'][nested_class]['methods'][method]['body']).strip().split('{')[0] + '{}\n'
                skeleton += '\t\t// Class Methods End\n'

                skeleton += '\t}\n\n'

                added_classes.append(nested_class)

        skeleton += '\t// Class Fields Begin\n'
        for field in sorted(schema['classes'][class_]['fields']):
            skeleton += '\t' + ''.join(schema['classes'][class_]['fields'][field]['body']).strip() + '\n'
        skeleton += '\t// Class Fields End\n\n'

        skeleton += '\t// Class Methods Begin\n'
        for method in sorted(schema['classes'][class_]['methods']):
            if schema['classes'][class_]['is_interface']:
                skeleton += '\t' + ''.join(schema['classes'][class_]['methods'][method]['body']).strip().split('{')[0] + '\n'
            else:
                skeleton += '\t' + ''.join(schema['classes'][class_]['methods'][method]['body']).strip().split('{')[0] + '{}\n'
        skeleton += '\t// Class Methods End\n'

        skeleton += '}'

    skeleton = skeleton.replace('\t', '    ')
    skeletons['java'] = skeleton

    skeleton = ''
    skeleton += '# Imports Begin\n'
    skeleton += '# Imports End\n\n'

    target_schema = schema.copy()

    class_dependencies = []
    for class_ in schema['classes']:

        main_class = class_
        if schema['classes'][class_]['nested_inside'] != []:
            main_class = schema['classes'][class_]['nested_inside']
            dependencies[main_class].append(main_class)

        dependencies[main_class] += schema['classes'][main_class]['nests']

        if class_ in dependencies:
            class_dependencies.append((schema['path'], dependencies[class_]))

        if schema['classes'][class_]['extends'] != []:
            if schema['classes'][class_]['is_abstract'] or schema['classes'][class_]['is_interface']:
                skeleton += 'class ' + class_ + '(' + ', '.join(schema['classes'][class_]['extends'] + ['ABC']) + '):\n\n'
            else:
                skeleton += 'class ' + class_ + '(' + ', '.join(schema['classes'][class_]['extends']) + '):\n\n'
        elif schema['classes'][class_]['implements'] != []:
            if schema['classes'][class_]['is_abstract'] or schema['classes'][class_]['is_interface']:
                skeleton += 'class ' + class_ + '(' + ', '.join(schema['classes'][class_]['implements'] + ['ABC']) + '):\n\n'
            else:
                skeleton += 'class ' + class_ + '(' + ', '.join(schema['classes'][class_]['implements']) + '):\n\n'
        else:
            if schema['classes'][class_]['is_abstract'] or schema['classes'][class_]['is_interface']:
                skeleton += 'class ' + class_ + '(ABC):\n\n'
            else:
                skeleton += 'class ' + class_ + ':\n\n'            

        skeleton += '\t# Class Fields Begin\n'
        for field in sorted(schema['classes'][class_]['fields']):
            field_name = field.split(':')[1].strip()
            if 'protected' in schema['classes'][class_]['fields'][field]['modifiers']:
                field_name = '_' + field_name
            elif 'private' in schema['classes'][class_]['fields'][field]['modifiers']:
                field_name = '__' + field_name
            
            field_type = '<placeholder>'
            assert len(schema['classes'][class_]['fields'][field]['types']) == 1 or len(schema['classes'][class_]['fields'][field]['types']) == 0

            if len(schema['classes'][class_]['fields'][field]['types']) == 1 and schema['classes'][class_]['fields'][field]['types'][0] in extracted_types:
                field_type = extracted_types[schema['classes'][class_]['fields'][field]['types'][0]]

            field_body = field_name + f': {field_type} = '
            if '=' not in ''.join(schema['classes'][class_]['fields'][field]['body']):
                field_body += 'None\n'
            else:
                field_body += '<placeholder>\n'

            target_schema['classes'][class_]['fields'][field]['partial_translation'] = field_body

            skeleton += '\t' + field_body
        skeleton += '\t# Class Fields End\n\n'

        skeleton += '\t# Class Methods Begin\n'
        for method in schema['classes'][class_]['methods']:
            current_method = []
            method_name = method.split(':')[1].strip()

            is_static = False
            if 'static' in schema['classes'][class_]['methods'][method]['modifiers']:
                is_static = True
                skeleton += '\t@staticmethod\n'
                current_method += ['\t@staticmethod\n']

            updated_method_name = method_name
            if 'protected' in schema['classes'][class_]['methods'][method]['modifiers']:
                updated_method_name = '_' + method_name
            elif 'private' in schema['classes'][class_]['methods'][method]['modifiers']:
                updated_method_name = '__' + method_name

            if len(schema["classes"][class_]["methods"][method]["parameters"]) == 0:
                if class_ == method_name:
                    skeleton += '\tdef __init__(self) -> '
                    current_method += ['\tdef __init__(self) -> ']
                else:
                    if not is_static:
                        skeleton += '\tdef ' + updated_method_name + '(self) -> '
                        current_method += ['\tdef ' + updated_method_name + '(self) -> ']
                    else:
                        skeleton += '\tdef ' + updated_method_name + '() -> '
                        current_method += ['\tdef ' + updated_method_name + '() -> ']
            else:
                types_ = schema["classes"][class_]["methods"][method]["signature"][schema["classes"][class_]["methods"][method]["signature"].find('(')+1:schema["classes"][class_]["methods"][method]["signature"].find(')')].split(',')
                parameter_types = []
                for type_ in types_:
                    if type_.strip() in extracted_types:
                        parameter_types.append(extracted_types[type_.strip()])
                    else:
                        parameter_types.append('<placeholder>')

                parameters = schema["classes"][class_]["methods"][method]["parameters"]
                param_types = [(x, y) for x, y in zip(parameters, parameter_types)]

                if class_ == method_name:
                    skeleton += '\tdef __init__(self, ' + ', '.join([x + f': {y.strip()}' for x, y in param_types]) + ') -> '
                    current_method += ['\tdef __init__(self, ' + ', '.join([x + f': {y.strip()}' for x, y in param_types]) + ') -> ']
                else:
                    if not is_static:
                        skeleton += '\tdef ' + updated_method_name + '(self, ' + ', '.join([x + f': {y.strip()}' for x, y in param_types]) + ') -> '
                        current_method += ['\tdef ' + updated_method_name + '(self, ' + ', '.join([x + f': {y.strip()}' for x, y in param_types]) + ') -> ']
                    else:
                        skeleton += '\tdef ' + updated_method_name + '(' + ', '.join([x + f': {y.strip()}' for x, y in param_types]) + ') -> '
                        current_method += ['\tdef ' + updated_method_name + '(' + ', '.join([x + f': {y.strip()}' for x, y in param_types]) + ') -> ']

            assert len(schema['classes'][class_]['methods'][method]['return_types']) == 1 or len(schema['classes'][class_]['methods'][method]['return_types']) == 0

            return_type = '<placeholder>'
            if len(schema['classes'][class_]['methods'][method]['return_types']) == 1 and schema['classes'][class_]['methods'][method]['return_types'][0] in extracted_types:
                return_type = extracted_types[schema['classes'][class_]['methods'][method]['return_types'][0]]

            skeleton += f'{return_type}:\n\t\tpass\n\n'
            current_method[-1] = current_method[-1] + f'{return_type}:\n'
            current_method += ['\t\tpass\n\n']
            current_method = [x.replace('\t', '    ') for x in current_method]

            target_schema['classes'][class_]['methods'][method]['partial_translation'] = current_method

        skeleton += '\t# Class Methods End\n\n\n'

    python_imports = []

    if 'ABC' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom abc import ABC\n')
        python_imports.append('from abc import ABC')
    
    if 'List[' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom typing import List\n')
        python_imports.append('from typing import List')
    
    if 'Dict[' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom typing import Dict\n')
        python_imports.append('from typing import Dict')
    
    if 'Iterator[' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom typing import Iterator\n')
        python_imports.append('from typing import Iterator')
        
    if '[Any]' in skeleton or 'Any' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom typing import Any\n')
        python_imports.append('from typing import Any')
    
    if 'StringIO' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom io import StringIO\n')
        python_imports.append('from io import StringIO')
    
    if 'Type[' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom typing import Type\n')
        python_imports.append('from typing import Type')
    
    if 'Path' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom pathlib import Path\n')
        python_imports.append('from pathlib import Path')
    
    if 'IOBase' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom io import IOBase\n')
        python_imports.append('from io import IOBase')
    
    if 'Number' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom numbers import Number\n')
        python_imports.append('from numbers import Number')
    
    if 'Callable[' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom typing import Callable\n')
        python_imports.append('from typing import Callable')
    
    if 'date' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom datetime import date\n')
        python_imports.append('from datetime import date')

    for dependency in class_dependencies:
        path = dependency[0]
        prefix = path.split('/')
        prefix[-1] = prefix[-1].split('.')[0]
        prefix = '.'.join(prefix[2:-1])
        for dependent_class in dependency[1]:
            skeleton = skeleton.replace('# Imports Begin\n', f'# Imports Begin\nfrom {prefix}.{dependent_class} import {dependent_class}\n')

    target_schema.setdefault('python_imports', [])
    target_schema['python_imports'] = python_imports

    skeleton = skeleton.replace('\t', '    ')
    skeletons['python'] = skeleton

    os.makedirs('data/skeletons', exist_ok=True)
    with open(f'data/skeletons/{class_name}.json', 'w') as f:
        json.dump(skeletons, f, indent=4)

    with open(f'data/schemas/{class_name}_python_partial.json', 'w') as f:
        json.dump(target_schema, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a class skeleton')
    parser.add_argument('--class_name', type=str, dest='class_name', help='name of the class')
    args = parser.parse_args()
    main(args)
