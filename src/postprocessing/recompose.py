import argparse
import json
import os


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

    translation_files = os.listdir(f'data/translations/{args.project_name}')

    total_fragments = 0
    total_unsuccessful = 0

    for translation_file in translation_files:

        fragment_translations = {}
        with open(f'data/translations/{args.project_name}/{translation_file}') as f:
            fragment_translations = json.load(f)
        
        dependencies = {}
        with open(f'data/dependencies/{args.project_name}/dependencies.json', 'r') as f:
            dependencies = json.load(f)
        
        skeleton = ''
        skeleton += '# Imports Begin\n'
        skeleton += '# Imports End\n\n'

        class_dependencies = []
        for class_ in fragment_translations['classes']:

            main_class = class_
            while fragment_translations['classes'][main_class]['nested_inside'] != []:
                main_class = fragment_translations['classes'][main_class]['nested_inside']

            # if fragment_translations['classes'][class_]['nested_inside'] != []:
            #     main_class = fragment_translations['classes'][class_]['nested_inside']
            #     dependencies[main_class].append(main_class)

            # dependencies[main_class] += fragment_translations['classes'][main_class]['nests']

            if class_ in dependencies:
                class_dependencies.append((fragment_translations['path'], dependencies[class_]))

            if fragment_translations['classes'][class_]['extends'] != []:
                if fragment_translations['classes'][class_]['is_abstract'] or fragment_translations['classes'][class_]['is_interface']:
                    skeleton += 'class ' + class_ + '(' + ', '.join(fragment_translations['classes'][class_]['extends'] + ['ABC']) + '):\n\n'
                else:
                    skeleton += 'class ' + class_ + '(' + ', '.join(fragment_translations['classes'][class_]['extends']) + '):\n\n'
            elif fragment_translations['classes'][class_]['implements'] != []:
                if fragment_translations['classes'][class_]['is_abstract'] or fragment_translations['classes'][class_]['is_interface']:
                    skeleton += 'class ' + class_ + '(' + ', '.join(fragment_translations['classes'][class_]['implements'] + ['ABC']) + '):\n\n'
                else:
                    skeleton += 'class ' + class_ + '(' + ', '.join(fragment_translations['classes'][class_]['implements']) + '):\n\n'
            else:
                if fragment_translations['classes'][class_]['is_abstract'] or fragment_translations['classes'][class_]['is_interface']:
                    skeleton += 'class ' + class_ + '(ABC):\n\n'
                else:
                    skeleton += 'class ' + class_ + ':\n\n'
            
            if 'src.test' in translation_file:
                if f'class {class_}(' in skeleton:
                    skeleton = skeleton.replace(f'class {class_}(', f'class {class_}(unittest.TestCase, ')
                else:
                    skeleton = skeleton.replace(f'class {class_}:', f'class {class_}(unittest.TestCase):')

            if fragment_translations['classes'][class_]['fields'] == {} and fragment_translations['classes'][class_]['methods'] == {}:
                skeleton += '\tpass\n\n'
                continue

            skeleton += '\t# Class Fields Begin\n'
            for field in sorted(fragment_translations['classes'][class_]['fields']):

                field_name = field.split(':')[1].strip()
                if 'protected' in fragment_translations['classes'][class_]['fields'][field]['modifiers']:
                    field_name = '_' + field_name
                elif 'private' in fragment_translations['classes'][class_]['fields'][field]['modifiers']:
                    field_name = '__' + field_name
                
                field_type = '<placeholder>'
                assert len(fragment_translations['classes'][class_]['fields'][field]['types']) == 1 or len(fragment_translations['classes'][class_]['fields'][field]['types']) == 0

                if len(fragment_translations['classes'][class_]['fields'][field]['types']) == 1 and fragment_translations['classes'][class_]['fields'][field]['types'][0][0] in extracted_types:
                    field_type = extracted_types[fragment_translations['classes'][class_]['fields'][field]['types'][0][0]]

                field_body = field_name + f': {field_type} = '
                if '=' not in ''.join(fragment_translations['classes'][class_]['fields'][field]['body']):
                    field_body += 'None\n'
                else:
                    field_body += '"" # LLM could not translate field\n'

                    selected_translation = 1
                    for i in range(args.num_translations):
                        if fragment_translations['classes'][class_]['fields'][field][f'translation_{i + 1}'] != None:
                            selected_translation = i
                            break
                    
                    try:
                        field_body_translation = fragment_translations['classes'][class_]['fields'][field][f'translation_{selected_translation + 1}']
                        if field_body_translation == None:
                            raise TypeError
                        field_body = '\n'.join([x for x in field_body_translation if x.strip() != '']).strip() + '\n'
                    except TypeError:
                        total_unsuccessful += 1
                
                total_fragments += 1

                skeleton += f'\t{field_body}'
            skeleton += '\t# Class Fields End\n\n'

            skeleton += '\t# Class Methods Begin\n'
            for method in fragment_translations['classes'][class_]['methods']:

                current_method = []
                method_name = method.split(':')[1].strip()
                method_signature = ''

                is_static = False
                if 'static' in fragment_translations['classes'][class_]['methods'][method]['modifiers']:
                    is_static = True
                    method_signature += '\t@staticmethod\n'
                    current_method += ['\t@staticmethod\n']

                updated_method_name = method_name
                if 'protected' in fragment_translations['classes'][class_]['methods'][method]['modifiers']:
                    updated_method_name = '_' + method_name
                elif 'private' in fragment_translations['classes'][class_]['methods'][method]['modifiers']:
                    updated_method_name = '__' + method_name

                if len(fragment_translations["classes"][class_]["methods"][method]["parameters"]) == 0:
                    if class_ == method_name:
                        method_signature += '\tdef __init__(self) -> '
                        current_method += ['\tdef __init__(self) -> ']
                    else:
                        if not is_static:
                            method_signature += '\tdef ' + updated_method_name + '(self) -> '
                            current_method += ['\tdef ' + updated_method_name + '(self) -> ']
                        else:
                            method_signature += '\tdef ' + updated_method_name + '() -> '
                            current_method += ['\tdef ' + updated_method_name + '() -> ']
                else:
                    types_ = split_with_nested_commas(fragment_translations["classes"][class_]["methods"][method]["signature"][fragment_translations["classes"][class_]["methods"][method]["signature"].find('(')+1:fragment_translations["classes"][class_]["methods"][method]["signature"].find(')')])
                    parameter_types = []
                    for type_ in types_:
                        if type_.strip() in extracted_types:
                            parameter_types.append(extracted_types[type_.strip()])
                        else:
                            parameter_types.append('<placeholder>')
                    
                    parameters = fragment_translations["classes"][class_]["methods"][method]["parameters"]
                    param_types = [(x, y) for x, y in zip(parameters, parameter_types)]

                    if class_ == method_name:
                        method_signature += '\tdef __init__(self, ' + ', '.join([x + f': {y.strip()}' for x, y in param_types]) + ') -> '
                        current_method += ['\tdef __init__(self, ' + ', '.join([x + f': {y.strip()}' for x, y in param_types]) + ') -> ']
                    else:
                        if not is_static:
                            method_signature += '\tdef ' + updated_method_name + '(self, ' + ', '.join([x + f': {y.strip()}' for x, y in param_types]) + ') -> '
                            current_method += ['\tdef ' + updated_method_name + '(self, ' + ', '.join([x + f': {y.strip()}' for x, y in param_types]) + ') -> ']
                        else:
                            method_signature += '\tdef ' + updated_method_name + '(' + ', '.join([x + f': {y.strip()}' for x, y in param_types]) + ') -> '
                            current_method += ['\tdef ' + updated_method_name + '(' + ', '.join([x + f': {y.strip()}' for x, y in param_types]) + ') -> ']

                assert len(fragment_translations['classes'][class_]['methods'][method]['return_types']) == 1 or len(fragment_translations['classes'][class_]['methods'][method]['return_types']) == 0

                return_type = '<placeholder>'
                if len(fragment_translations['classes'][class_]['methods'][method]['return_types']) == 1 and fragment_translations['classes'][class_]['methods'][method]['return_types'][0][0] in extracted_types:
                    return_type = extracted_types[fragment_translations['classes'][class_]['methods'][method]['return_types'][0][0]]

                selected_translation = 1
                for i in range(args.num_translations):
                    if fragment_translations['classes'][class_]['methods'][method][f'translation_{i + 1}'] != None:
                        selected_translation = i
                        break
                
                method_body = ['', '\t\tpass # LLM could not translate method body']

                try:
                    method_body = fragment_translations['classes'][class_]['methods'][method][f'translation_{selected_translation + 1}']
                    if method_body == None:
                        method_body = ['', '\t\tpass # LLM could not translate method body']
                        raise TypeError
                    method_body = [x for x in method_body if x.strip() != '']
                    method_signature = current_method[-1].split('(')[0].strip()
                    for i in range(len(method_body)):
                        if method_body[i].strip().startswith(method_signature.strip()):
                            method_body = method_body[i+1:]
                            break
                    
                    # indent if not already indented
                    if method_body[0].strip() != '' and method_body[0].strip()[0] != '\t':
                        method_body = ['\t' + x for x in method_body]

                except TypeError:
                    total_unsuccessful += 1

                total_fragments += 1
                current_method[-1] = current_method[-1] + f'{return_type}:\n'
                current_method += method_body
                skeleton += '\n'.join(current_method) + '\n\n'

                assert '<placeholder>' not in ''.join(current_method)

            skeleton += '\t# Class Methods End\n\n\n'

        if 'ABC' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nfrom abc import ABC\n')

        if 'Path' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nimport pathlib\n')
        
        if 'IOBase' in skeleton or 'StringIO' in skeleton or 'BytesIO' in skeleton or 'TextIOWrapper' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nimport io\n')
        
        if 'Number' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nimport numbers\n')
        
        if 'Callable' in skeleton or 'Type' in skeleton or 'Any' in skeleton or 'Iterator' in skeleton or 'Dict' in skeleton or 'List' in skeleton or 'typing.IO' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nimport typing\nfrom typing import *\n')
        
        if 'datetime' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nimport datetime\n')
        
        if 'unittest.TestCase' in skeleton:
            skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\nimport unittest\n')
        
        for element in ['assertEquals', 'assertTrue', 'assertFalse', 'assertRaises', 'assertIsNone', 'assertIsNotNone', 'assertIn', 'assertNotIn', 'assertIsInstance', 'assertNotIsInstance']:
            skeleton = skeleton.replace(f'{element}(', f'self.{element}(')
            if f'self.self.{element}(' in skeleton:
                skeleton = skeleton.replace(f'self.self.{element}(', f'self.{element}(')

        for dependency in class_dependencies:
            for dependent_class in dependency[1]:
                path = f'src.main.{dependent_class[1]}'
                if f'from {path} import *' in skeleton:
                    continue
                skeleton = skeleton.replace('# Imports Begin\n', f'# Imports Begin\nfrom {path} import *\n')

        skeleton = skeleton.replace('\t', '    ')

        formatted_schema_fname = '.'.join(translation_file.split('.')[:-1])
        sub_dir = "/".join(formatted_schema_fname.replace(".", "/").split("/")[1:-1])
        os.makedirs(f'data/recomposed_projects/{args.project_name}/{sub_dir}', exist_ok=True)
        file_path = f"data/recomposed_projects/{args.project_name}/{sub_dir}/{formatted_schema_fname.split('.')[-1].replace('_translation', '')}.py"
        with open(file_path, 'w') as f:
            f.write(skeleton)
        
        os.system(f'python3 -m black {file_path}')

    # add __init__.py files for each subdirectory
    for translation_file in translation_files:
        formatted_schema_fname = '.'.join(translation_file.split('.')[:-1])
        sub_dir = "/".join(formatted_schema_fname.replace(".", "/").split("/")[1:-1])
        os.makedirs(f'data/recomposed_projects/{args.project_name}/{sub_dir}', exist_ok=True)

        sub_dirs = sub_dir.split('/')
        for i in range(len(sub_dirs)):
            current_sub_dir = '/'.join(sub_dirs[:i+1])
            with open(f'data/recomposed_projects/{args.project_name}/{current_sub_dir}/__init__.py', 'w') as f:
                f.write('')

        file_path = f"data/recomposed_projects/{args.project_name}/{sub_dir}/__init__.py"
        with open(file_path, 'w') as f:
            f.write('')

    # print(f'total fragments: {total_fragments}, total unsuccessful: {total_unsuccessful}')
    # print(f'percentage unsuccessful: {total_unsuccessful / total_fragments * 100}%')


if __name__ == '__main__':
    parser_ = argparse.ArgumentParser(description='Translate java types to python types')
    parser_.add_argument('--project_name', type=str, dest='project_name', help='project name to translate')
    parser_.add_argument('--num_translations', type=int, dest='num_translations', help='number of translations to generate per request')
    args = parser_.parse_args()
    main(args)
