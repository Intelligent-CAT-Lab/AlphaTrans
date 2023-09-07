import os
import json
import argparse


def main(args):

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

    skeletons['java'] = skeleton
    skeleton = ''

    skeleton += '# Imports Begin\n'
    skeleton += '<placeholder>\n'
    skeleton += '# Imports End\n\n'

    class_dependencies = []

    for class_ in schema['classes']:

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
            skeleton += '\t' + field_name + ': <placeholder> = <placeholder>\n'
        skeleton += '\t# Class Fields End\n\n'

        overloaded_methods = {}

        for method in sorted(schema['classes'][class_]['methods']):
            method_name = method.split(':')[1].strip()
            overloaded_methods.setdefault(method_name, []).append(method)
        
        overloaded_method_names = [x for x in overloaded_methods if len(overloaded_methods[x]) > 1]

        skeleton += '\t# Class Methods Begin\n'
        for method in schema['classes'][class_]['methods']:
            method_name = method.split(':')[1].strip()
            if method_name in overloaded_method_names:
                if 'static' in schema['classes'][class_]['methods'][method]['modifiers']:
                    skeleton += '\t@staticmethod\n'
                
                updated_method_name = method_name
                if 'protected' in schema['classes'][class_]['methods'][method]['modifiers']:
                    updated_method_name = '_' + method_name
                elif 'private' in schema['classes'][class_]['methods'][method]['modifiers']:
                    updated_method_name = '__' + method_name
                
                skeleton += '\t@dispatch(<placeholder>)\n'

                if len(schema["classes"][class_]["methods"][method]["parameters"]) == 0:
                    if class_ == method_name:
                        skeleton += '\tdef __init__(self) -> <placeholder>:\n\t\tpass\n\n'
                    else:
                        skeleton += '\tdef ' + updated_method_name + '(self) -> <placeholder>:\n\t\tpass\n\n'
                else:
                    if class_ == method_name:
                        skeleton += '\tdef __init__(self, ' + ', '.join([x + ': <placeholder>' for x in schema["classes"][class_]["methods"][method]["parameters"]]) + ') -> <placeholder>:\n\t\tpass\n\n'
                    else:
                        skeleton += '\tdef ' + updated_method_name + '(self, ' + ', '.join([x + ': <placeholder>' for x in schema["classes"][class_]["methods"][method]["parameters"]]) + ') -> <placeholder>:\n\t\tpass\n\n'

            elif method_name not in overloaded_method_names:
                if 'static' in schema['classes'][class_]['methods'][method]['modifiers']:
                    skeleton += '\t@staticmethod\n'

                updated_method_name = method_name
                if 'protected' in schema['classes'][class_]['methods'][method]['modifiers']:
                    updated_method_name = '_' + method_name
                elif 'private' in schema['classes'][class_]['methods'][method]['modifiers']:
                    updated_method_name = '__' + method_name

                if len(schema["classes"][class_]["methods"][method]["parameters"]) == 0:
                    if class_ == method_name:
                        skeleton += '\tdef __init__(self) -> <placeholder>:\n\t\tpass\n\n'
                    else:
                        skeleton += '\tdef ' + updated_method_name + '(self) -> <placeholder>:\n\t\tpass\n\n'
                else:
                    if class_ == method_name:
                        skeleton += '\tdef __init__(self, ' + ', '.join([x + ': <placeholder>' for x in schema["classes"][class_]["methods"][method]["parameters"]]) + ') -> <placeholder>:\n\t\tpass\n\n'
                    else:
                        skeleton += '\tdef ' + updated_method_name + '(self, ' + ', '.join([x + ': <placeholder>' for x in schema["classes"][class_]["methods"][method]["parameters"]]) + ') -> <placeholder>:\n\t\tpass\n\n'

        skeleton += '\t# Class Methods End\n\n\n'

    if '@dispatch' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom multipledispatch import dispatch\n')
    if 'ABC' in skeleton:
        skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom abc import ABC\n')
    
    for dependency in class_dependencies:
        path = dependency[0]
        prefix = path.split('/')
        prefix[-1] = prefix[-1].split('.')[0]
        prefix = '.'.join(prefix[2:-1])
        for dependent_class in dependency[1]:
            skeleton = skeleton.replace('# Imports Begin\n', f'# Imports Begin\nfrom {prefix}.{dependent_class} import {dependent_class}\n')

    skeletons['python'] = skeleton

    os.makedirs('data/skeletons', exist_ok=True)
    with open(f'data/skeletons/{class_name}.json', 'w') as f:
        json.dump(skeletons, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a class skeleton')
    parser.add_argument('--class_name', type=str, dest='class_name', help='name of the class')
    args = parser.parse_args()
    main(args)
