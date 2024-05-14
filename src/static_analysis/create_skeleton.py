import os
import re
import json
import argparse


def split_with_nested_commas(s):
    result = []
    stack = []
    start = 0

    for i, c in enumerate(s):
        if c == ',' and not stack:
            result.append(s[start:i].strip())
            start = i + 1
        elif c == '<':
            stack.append(c)
        elif c == '>':
            stack.pop()

    result.append(s[start:].strip())
    return result


def main(args):

    with open(f'data/type_resolution/universal_type_map_final.json', 'r') as f:
        extracted_types = json.load(f)
    
    extracted_types = {k.split('.')[-1]: v for k, v in extracted_types.items()}

    schemas = os.listdir(f'data/schemas/{args.project_name}')

    for schema_fname in schemas:

        if 'python_partial' in schema_fname:
            continue

        schema_path = f'data/schemas/{args.project_name}/{schema_fname}'

        dependencies = {}
        with open(f'data/dependencies/{args.project_name}/dependencies.json', 'r') as f:
            dependencies = json.load(f)
        
        schema = {}
        with open(schema_path, 'r') as f:
            schema = json.load(f)

        skeleton = ''
        skeleton += '# Imports Begin\n'
        skeleton += '# Imports End\n\n'

        target_schema = schema.copy()

        topological_classes = []
        while len(topological_classes) != len(schema['classes']):
            for class_ in schema['classes']:
                if class_ in topological_classes:
                    continue

                if schema['classes'][class_]['nested_inside'] != []:
                    if schema['classes'][class_]['nested_inside'] not in topological_classes:
                        continue

                topological_classes.append(class_)

        class_dependencies = []
        for class_ in topological_classes:
            main_class = class_
            if schema['classes'][class_]['nested_inside'] != []:
                main_class = schema['classes'][class_]['nested_inside']
                dependencies.setdefault(main_class, [])
                dependencies[main_class].append(main_class)

            dependencies[main_class] += schema['classes'][main_class]['nests']

            if class_ in dependencies:
                class_dependencies.append((schema['path'], dependencies[class_]))
            
            class_name = class_
            if '<' in class_:
                class_name = class_.split('<')[0].replace('new ', '').strip()
            elif '(' in class_:
                class_name = class_.split('(')[0].replace('new ', '').strip()

            if schema['classes'][class_]['extends'] != []:
                schema['classes'][class_]['extends'] = [cls_name.split('<')[0].replace('new ', '').strip() for cls_name in schema['classes'][class_]['extends']]
                schema['classes'][class_]['extends'] = [cls_name.split('(')[0].replace('new ', '').strip() for cls_name in schema['classes'][class_]['extends']]
                if schema['classes'][class_]['is_abstract'] or schema['classes'][class_]['is_interface']:
                    skeleton += 'class ' + class_name + '(' + ', '.join(schema['classes'][class_]['extends'] + ['ABC']) + '):\n\n'
                else:
                    skeleton += 'class ' + class_name + '(' + ', '.join(schema['classes'][class_]['extends']) + '):\n\n'
            elif schema['classes'][class_]['implements'] != []:
                schema['classes'][class_]['implements'] = [cls_name.split('<')[0].replace('new ', '').strip() for cls_name in schema['classes'][class_]['implements']]
                schema['classes'][class_]['implements'] = [cls_name.split('(')[0].replace('new ', '').strip() for cls_name in schema['classes'][class_]['implements']]
                if schema['classes'][class_]['is_abstract'] or schema['classes'][class_]['is_interface']:
                    skeleton += 'class ' + class_name + '(' + ', '.join(schema['classes'][class_]['implements'] + ['ABC']) + '):\n\n'
                else:
                    skeleton += 'class ' + class_name + '(' + ', '.join(schema['classes'][class_]['implements']) + '):\n\n'
            else:
                if schema['classes'][class_]['is_abstract'] or schema['classes'][class_]['is_interface']:
                    skeleton += 'class ' + class_name + '(ABC):\n\n'
                else:
                    skeleton += 'class ' + class_name + ':\n\n'            

            is_empty_class = True
            skeleton += '\t# Class Fields Begin\n'
            for field in sorted(schema['classes'][class_]['fields']):
                is_empty_class = False
                field_name = field.split(':')[1].strip()
                if 'protected' in schema['classes'][class_]['fields'][field]['modifiers']:
                    field_name = '_' + field_name
                elif 'private' in schema['classes'][class_]['fields'][field]['modifiers']:
                    field_name = '__' + field_name
                
                field_type = '<placeholder>'
                assert len(schema['classes'][class_]['fields'][field]['types']) == 1 or len(schema['classes'][class_]['fields'][field]['types']) == 0

                if len(schema['classes'][class_]['fields'][field]['types']) == 1 and schema['classes'][class_]['fields'][field]['types'][0][0] in extracted_types:
                    field_type = extracted_types[schema['classes'][class_]['fields'][field]['types'][0][0]]

                field_body = field_name + f': {field_type} = '
                if '=' not in ''.join(schema['classes'][class_]['fields'][field]['body']):
                    field_body += 'None\n'
                else:
                    field_body += '<placeholder>\n'

                target_schema['classes'][class_]['fields'][field]['partial_translation'] = f'    {field_body}'

                skeleton += f'\t{field_name}: {field_type} = None\n'
            skeleton += '\t# Class Fields End\n\n'

            skeleton += '\t# Class Methods Begin\n'
            for method in schema['classes'][class_]['methods']:
                current_method = []
                method_name = method.split(':')[1].strip()

                if method_name.strip() == '':
                    continue

                if method_name in ['from']:
                    method_name = 'from_'

                is_empty_class = False

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
                    types_ = split_with_nested_commas(schema["classes"][class_]["methods"][method]["signature"][schema["classes"][class_]["methods"][method]["signature"].find('(')+1:schema["classes"][class_]["methods"][method]["signature"].find(')')])
                    parameter_types = []
                    for type_ in types_:
                        if type_.strip() in extracted_types:
                            parameter_types.append(extracted_types[type_.strip()])
                        else:
                            parameter_types.append('<placeholder>')
                    
                    parameters = schema["classes"][class_]["methods"][method]["parameters"]
                    param_types = [(x, y) for x, y in zip(parameters, parameter_types)]
                    param_types = [('in_', y) if x == 'in' else (x, y) for x, y in param_types]
                    param_types = [('from_', y) if x == 'from' else (x, y) for x, y in param_types]

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
                if len(schema['classes'][class_]['methods'][method]['return_types']) == 1 and schema['classes'][class_]['methods'][method]['return_types'][0][0] in extracted_types:
                    return_type = extracted_types[schema['classes'][class_]['methods'][method]['return_types'][0][0]]
                    if return_type == class_:
                        return_type = f'"{class_}"'

                skeleton += f'{return_type}:\n\t\tpass\n\n'
                current_method[-1] = current_method[-1] + f'{return_type}:\n'
                current_method += ['\t\tpass\n\n']
                current_method = [x.replace('\t', '    ') for x in current_method]

                target_schema['classes'][class_]['methods'][method]['partial_translation'] = current_method

                assert '<placeholder>' not in ''.join(current_method)

            skeleton += '\t# Class Methods End\n\n\n'

            if is_empty_class:
                skeleton += '\tpass\n\n'

        python_imports = []

        if 'ABC' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom abc import ABC\n')
            python_imports.append('from abc import ABC')

        if 'configparser' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nimport configparser\n')
            python_imports.append('import configparser')

        if 'Path' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nimport pathlib\n')
            python_imports.append('import pathlib')
        
        if 'IOBase' in skeleton or 'StringIO' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nimport io\n')
            python_imports.append('import io')
        
        if 'Number' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nimport numbers\n')
            python_imports.append('import numbers')
        
        if 'Callable' in skeleton or 'Type' in skeleton or 'Any' in skeleton or 'Iterator' in skeleton or 'Dict' in skeleton or 'List' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nimport typing\n')
            python_imports.append('import typing')
        
        if 'datetime' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nimport datetime\n')
            python_imports.append('import datetime')

        for dependency in class_dependencies:
            for dependent_class in dependency[1]:
                if len(dependent_class) != 2:
                    continue

                path = f'src.main.{dependent_class[1]}'
                if f'from {path} import *' in skeleton:
                    continue
                skeleton = skeleton.replace('# Imports Begin\n', f'# Imports Begin\nfrom {path} import *\n')

        target_schema.setdefault('python_imports', [])
        target_schema['python_imports'] = python_imports

        skeleton = skeleton.replace('\t', '    ')
        formatted_schema_fname = '.'.join(schema_fname.split('.')[:-1])

        os.makedirs(f'data/skeletons/{args.project_name}', exist_ok=True)

        skeleton = skeleton.replace('\t', '    ')

        formatted_schema_fname = '.'.join(schema_fname.split('.')[:-1])
        sub_dir = "/".join(formatted_schema_fname.replace(".", "/").split("/")[1:-1])
        os.makedirs(f'data/skeletons/{args.project_name}/{sub_dir}', exist_ok=True)
        file_path = f"data/skeletons/{args.project_name}/{sub_dir}/{formatted_schema_fname.split('.')[-1].replace('_translation', '')}.py"
        with open(file_path, 'w') as f:
            f.write(skeleton)
        
        os.system(f'python3 -m black {file_path}')

        with open(f'data/schemas/{args.project_name}/{formatted_schema_fname}_python_partial.json', 'w') as f:
            json.dump(target_schema, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a class skeleton')
    parser.add_argument('--project_name', type=str, dest='project_name', help='name of the project')
    args = parser.parse_args()
    main(args)
