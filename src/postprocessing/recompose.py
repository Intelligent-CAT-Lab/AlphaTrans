import argparse
import json
import os


def has_test_method(methods):
    for method in methods:
        if 'Test' in [x.split('(')[0] for x in methods[method]['annotations']]:
            return True
    return False


def main(args):

    total_fragments = 0
    total_unsuccessful = 0

    translation_dir = f'data/schemas/translations/{args.model_name}/{args.type}/{args.project_name}'

    for schema in os.listdir(translation_dir):

        if not schema.endswith('_python_partial.json'):
            continue

        if args.file_name != None and f'.{args.file_name}_python_partial.json' not in schema:
            continue

        if args.recompose_evosuite and 'ESTest' not in schema:
            continue

        if not args.recompose_evosuite and 'ESTest' in schema:
            continue

        data = {}
        with open(f'{translation_dir}/{schema}') as f:
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

            recomposed_file += data['classes'][class_]['python_class_declaration']

            if data['classes'][class_]['fields'] == {} and data['classes'][class_]['methods'] == {}:
                recomposed_file += '    pass\n\n'
                continue

            field_val = {}
            for field in data['classes'][class_]['fields']:
                if data['classes'][class_]['fields'][field]['translation'] == []:
                    data['classes'][class_]['fields'][field]['translation'] = '\n'.join(data['classes'][class_]['fields'][field]['partial_translation']).replace('<placeholder>', 'None # LLM could not translate this field').split('\n')
                translation = '\n'.join(data['classes'][class_]['fields'][field]['translation']).strip()
                field_name = translation[:translation.find(':')].strip()
                field_value = ''.join(translation.split('=')[1:]).strip()
                field_val[field_name] = {'value': field_value, 'key': field}
            
            field_dependencies = {}
            for field in field_val:
                field_dependencies.setdefault(field, [])
                for field_ in field_val:
                    if field == field_:
                        continue
                    if field_ in field_val[field]['value']:
                        field_dependencies[field].append(field_)

            field_order = []
            while len(field_order) != len(field_val):
                for field in field_val:
                    if field in field_order:
                        continue
                    if all([x in field_order for x in field_dependencies[field]]):
                        field_order.append(field)

            assert len(field_order) == len(field_val)

            field_order = [field_val[x]['key'] for x in field_order]

            intialize_later_fields = []
            for field in field_order:

                total_fragments += 1
                if data['classes'][class_]['fields'][field]['translation'] == []:
                    recomposed_file += '\n'.join([''] + data['classes'][class_]['fields'][field]['partial_translation']).replace('<placeholder>', 'None # LLM could not translate this field')
                    recomposed_file += '\n'
                    total_unsuccessful += 1
                    continue

                field_translation = ''
                for l in data['classes'][class_]['fields'][field]['translation']:
                    field_translation += l[:l.find('#')].replace('\\', '') if '#' in l else l.replace('\\', '')
                
                found = False

                static_methods = []
                for method in data['classes'][class_]['methods']:
                    if 'static' in data['classes'][class_]['methods'][method]['modifiers']:
                        if 'private' in data['classes'][class_]['methods'][method]['modifiers']:
                            static_methods.append(f'__{method.split(":")[1]}')
                        elif 'protected' in data['classes'][class_]['methods'][method]['modifiers']:
                            static_methods.append(f'_{method.split(":")[1]}')
                        else:
                            static_methods.append(method.split(":")[1])

                for method in static_methods:
                    field_translation = field_translation.replace(f'self.{method}', method)
                    if f'{method}(' in field_translation.split('=')[1].strip() or \
                        f'({method}' in field_translation.split('=')[1].strip() or \
                        f'{method})' in field_translation.split('=')[1].strip() or \
                        f'{method},' in field_translation.split('=')[1].strip() or \
                        f',{method}' in field_translation.split('=')[1].strip():

                        intialize_later_fields.append((field, field_translation.split('=')[0].strip(), '='.join(field_translation.split('=')[1:]).strip().replace(f'{method}', f'{class_}.{method}' if f'{class_}.{method}' not in field_translation.split('=')[1].strip() else f'{method}')))
                        recomposed_file += ''.join(data['classes'][class_]['fields'][field]['partial_translation']).replace('<placeholder>', f'None')
                        recomposed_file += '\n'
                        found = True
                
                if found:
                    continue

                for a_class in class_order:
                    if f'{a_class}.' in field_translation or \
                        f'{a_class}(' in field_translation or \
                        f'({a_class}' in field_translation or \
                        f'{a_class})' in field_translation or \
                        f'{a_class},' in field_translation or \
                        f',{a_class}' in field_translation or \
                        f'{a_class}' in field_translation.split('=')[1].strip():

                        intialize_later_fields.append((field, field_translation.split('=')[0].strip(), '='.join(field_translation.split('=')[1:]).strip()))
                        recomposed_file += ''.join(data['classes'][class_]['fields'][field]['partial_translation']).replace('<placeholder>', f'None')
                        recomposed_file += '\n'
                        found = True
                
                if found:
                    continue

                if '='.join(field_translation.split('=')[1:]).strip() == 'self':
                    continue

                recomposed_file += '\n'.join(data['classes'][class_]['fields'][field]['translation'])
                recomposed_file += '\n'

            if 'static_initializers' in data['classes'][class_]:
                for static_initializer in data['classes'][class_]['static_initializers']:
                    recomposed_file += '\n'.join(data['classes'][class_]['static_initializers'][static_initializer]['translation'])
                    recomposed_file += '\n'
                class_initialize_methods.append(f'{class_}.run_static_init()')

            # create static method for field initialization
            if intialize_later_fields != []:
                if len(intialize_later_fields) == 1 and intialize_later_fields[0][2] == 'self':
                    pass
                else:
                    recomposed_file += f'\n\n    @staticmethod\n    def initialize_fields() -> None:\n'
                    for field, field_name, field_value in intialize_later_fields:
                        if field_value == 'self':
                            continue
                        recomposed_file += '    ' + ''.join(data['classes'][class_]['fields'][field]['partial_translation']).replace(f'{field_name}', f'{class_}.{field_name}').replace('<placeholder>', f'{field_value}\n')
                        recomposed_file += '\n'
                    class_initialize_methods.append(f'{class_}.initialize_fields()')
                        
            for method in data['classes'][class_]['methods']:

                # ignore constructors in test files
                # if data['classes'][class_]['methods'][method]['is_constructor'] and 'src.test' in schema and has_test_method(data['classes'][class_]['methods']):
                #     continue

                if 'Ignore' in [x.split('(')[0] for x in data['classes'][class_]['methods'][method]['annotations']] or 'ParameterizedTest' in [x.split('(')[0] for x in data['classes'][class_]['methods'][method]['annotations']]:
                    recomposed_file += '\n    @pytest.mark.skip(reason="Ignore")\n'

                # if 'Test' in [x.split('(')[0] for x in data['classes'][class_]['methods'][method]['annotations']]:
                #     recomposed_file += '\n    @pytest.mark.test\n'
                
                # if 'Before' in [x.split('(')[0] for x in data['classes'][class_]['methods'][method]['annotations']]:
                #     recomposed_file += '\n    @pytest.mark.before\n'
                
                # if 'After' in [x.split('(')[0] for x in data['classes'][class_]['methods'][method]['annotations']]:
                #     recomposed_file += '\n    @pytest.mark.after\n'

                if data['classes'][class_]['methods'][method]['translation'] == [] and 'ESTest' in schema and not args.recompose_evosuite:
                    continue

                if data['classes'][class_]['methods'][method]['translation'] == []:
                    recomposed_file += '\n'.join([''] + data['classes'][class_]['methods'][method]['partial_translation']).replace('pass', 'pass # LLM could not translate this method')
                    recomposed_file += '\n'
                    total_unsuccessful += 1
                    continue

                recomposed_file += '\n'.join(data['classes'][class_]['methods'][method]['translation']).replace('_setUp(', 'setUp(').replace('_tearDown(', 'tearDown(')
                recomposed_file += '\n'
                total_fragments += 1

                if 'Test' in [x.split('(')[0] for x in data['classes'][class_]['methods'][method]['annotations']]:
                    if 'test' not in method:
                        recomposed_file = recomposed_file.replace(f'def {method.split(":")[1]}', f'def test{method.split(":")[1]}')

        for initialize_method in class_initialize_methods:
            recomposed_file += f'\n\n{initialize_method}'

        import_map = {'ABC': 'from abc import ABC\n', 'Path': 'import pathlib\n', 'IOBase': 'import io\n', 'StringIO': 'import io\n', 'io': 'import io\n', 'threading': 'import threading\n',
                      'BytesIO': 'import io\n', 'TextIOWrapper': 'import io\n', 'Number': 'import numbers\n', 'Callable': 'import typing\nfrom typing import *\n', 'enum': 'import enum\n',
                      'Type': 'import typing\nfrom typing import *\n', 'Any': 'import typing\nfrom typing import *\n', 'Iterator': 'import typing\nfrom typing import *\n', 'decimal': 'import decimal\n',
                      'Dict': 'import typing\nfrom typing import *\n', 'List': 'import typing\nfrom typing import *\n', 'Union': 'import typing\nfrom typing import *\n', 'datetime': 'import datetime\n', 
                      'os': 'import os\n', 'pickle': 'import pickle\n', 'itertools': 'import itertools\n', 'sys': 'import sys\n', 'collections': 'import collections\n', 
                      'unittest.TestCase': 'import unittest\n', 'uuid': 'import uuid\n', 'tempfile': 'import tempfile\n', 'typing': 'import typing\n', 'BytesIO': 'from io import BytesIO\n',
                      'configparser': 'import configparser\n', 'StringIO': 'from io import StringIO\n', 'IOBase': 'from io import IOBase\n', 'Number': 'import numbers\n', 'zoneinfo': 'import zoneinfo\n',
                      'urllib': 'import urllib\n', 'logging': 'import logging\n', 'mock': 'import mock\n', 'cmp_to_key': 'from functools import cmp_to_key\n', 'random': 'import random\n',
                      're': 'import re\n', 'locale': 'import locale\n', 'copy': 'import copy\n', 'traceback': 'import traceback\n', 'inspect': 'import inspect\n', 'time': 'import time\n',
                      'sqrt': 'from math import *\n', 'math': 'import math\n'}

        python_imports = data['python_imports']
        for key in import_map:
            if key in recomposed_file and import_map[key] not in recomposed_file:
                recomposed_file = recomposed_file.replace('from __future__ import annotations\n', 'from __future__ import annotations\n' + import_map[key])
                python_imports.append(import_map[key].strip())
        
        exception_map = {'IllegalArgumentException': 'ValueError', 'RuntimeException': 'RuntimeError', 'UnsupportedOperationException': 'NotImplementedError',
                         'CloneNotSupportedError': 'NotImplementedError', 'IllegalStateException': 'RuntimeError', 'UnsupportedEncodingException': 'ValueError',
                         'UnsupportedEncodingError': 'ValueError', 'NullPointerException': 'RuntimeError', 'NoSuchElementException': 'RuntimeError',
                         'NumberFormatException': 'ValueError', 'ClassCastException': 'TypeError', 'ArrayIndexOutOfBoundsException': 'IndexError',
                         'UnsupportedCharsetException': 'ValueError', 'SecurityException': 'PermissionError', 'SecurityError': 'PermissionError',}
        
        for key in exception_map:
            if key in recomposed_file:
                recomposed_file = recomposed_file.replace(key, exception_map[key])
        
        constant_map = {'Byte.SIZE': '8', 'Byte.MAX_VALUE': '127', 'Byte.MIN_VALUE': '-128', 'DateFormat.SHORT': '3', 'Integer.MIN_VALUE': '-2147483648', 'Integer.SIZE': '32',
                        'Short.SIZE': '16', 'Long.SIZE': '64', 'Short.MAX_VALUE': '32767', 'Short.MIN_VALUE': '-32768', 'Long.MAX_VALUE': '9223372036854775807', 'Integer.MAX_VALUE': '2147483647',
                        'Long.MIN_VALUE': '-9223372036854775808', 'Character.SIZE': '16', 'Character.MAX_VALUE': '65535', 'Character.MIN_VALUE': '0', 'Float.SIZE': '32', 'Float.MAX_VALUE': '3.4028235E38',}

        for key in constant_map:
            if key in recomposed_file:
                recomposed_file = recomposed_file.replace(key, constant_map[key])

        formatted_schema_fname = '.'.join(schema.split('.')[:-1])
        sub_dir = "/".join(formatted_schema_fname.replace(".", "/").split("/")[1:-1])
        os.makedirs(f'{args.output_dir}/{args.model_name}/{args.type}/{args.project_name}/{sub_dir}', exist_ok=True)
        os.makedirs(f'{args.output_dir}/{args.model_name}/{args.type}/{args.project_name}/evosuite-test/{sub_dir}', exist_ok=True)

        if args.recompose_evosuite:
            file_path = f"{args.output_dir}/{args.model_name}/{args.type}/{args.project_name}/evosuite-test/{sub_dir}/{formatted_schema_fname.split('.')[-1].replace('_python_partial', '')}.py"
        else:
            file_path = f"{args.output_dir}/{args.model_name}/{args.type}/{args.project_name}/{sub_dir}/{formatted_schema_fname.split('.')[-1].replace('_python_partial', '')}.py"

        recomposed_file = recomposed_file.replace('\u0000', '\\u0000')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(recomposed_file)
        
        os.system(f'python3 -m black {file_path}')

    # add __init__.py files for each subdirectory
    for schema in os.listdir(translation_dir):
        formatted_schema_fname = '.'.join(schema.split('.')[:-1])
        sub_dir = "/".join(formatted_schema_fname.replace(".", "/").split("/")[1:-1])
        os.makedirs(f'{args.output_dir}/{args.model_name}/{args.type}/{args.project_name}/{sub_dir}', exist_ok=True)

        sub_dirs = sub_dir.split('/')
        for i in range(len(sub_dirs)):
            current_sub_dir = '/'.join(sub_dirs[:i+1])
            with open(f'{args.output_dir}/{args.model_name}/{args.type}/{args.project_name}/{current_sub_dir}/__init__.py', 'w') as f:
                f.write('')

        file_path = f"{args.output_dir}/{args.model_name}/{args.type}/{args.project_name}/{sub_dir}/__init__.py"
        with open(file_path, 'w') as f:
            f.write('')
    
    with open(f'{args.output_dir}/{args.model_name}/{args.type}/{args.project_name}/pytest.ini', 'w') as f:
        f.write('# pytest.ini\n\n[pytest]\n# Require at least this version of pytest\nminversion = 8.2.1\n\n# Add options to control the pytest output\naddopts = -ra -q --continue-on-collection-errors --tb=native --junitxml=pytest-report.xml\n\n# Define directories to look for tests\n;testpaths = evosuite-test\ntestpaths = src/test\n\npython_files = *.py\n\npython_classes = *Test\n\npython_functions = test*\n')
    
    with open(f'{args.output_dir}/{args.model_name}/{args.type}/{args.project_name}/run.sh', 'w') as f:
        f.write('CURRENT_DIR=$(pwd)\nexport PYTHONPATH=$CURRENT_DIR\npython3 -m pytest\nxmllint --format pytest-report.xml -o pytest-report.xml')

    with open(f'{args.output_dir}/{args.model_name}/{args.type}/{args.project_name}/conftest.py', 'w') as f:
        f.write("""
# conftest.py
import pytest
import inspect
from abc import ABC

def pytest_collection_modifyitems(config, items):
    def is_abstract_class(item):
        # Check if the class of the item is a subclass of ABC (abstract base class)
        if inspect.isclass(item.cls):
            # Check if the class is actually abstract
            return ABC in item.cls.__bases__
        return False

    # Filter out items that belong to abstract classes
    items[:] = [item for item in items if not is_abstract_class(item)]
""")

    # print(f'total fragments: {total_fragments}, total unsuccessful: {total_unsuccessful}')
    # print(f'percentage unsuccessful: {total_unsuccessful / total_fragments * 100}%')
    # print(f'percentage successful: {100 - total_unsuccessful / total_fragments * 100}%')


if __name__ == '__main__':
    parser_ = argparse.ArgumentParser(description='Translate java types to python types')
    parser_.add_argument('--project_name', type=str, dest='project_name', help='project name to translate')
    parser_.add_argument('--model_name', type=str, dest='model_name', help='model name to translate')
    parser_.add_argument('--output_dir', type=str, dest='output_dir', help='directory to store recomposed projects')
    parser_.add_argument('--type', type=str, dest='type', help='prompting type signature/body')
    parser_.add_argument('--file_name', type=str, dest='file_name', help='file name to recompose')
    parser_.add_argument('--recompose_evosuite', action='store_true', dest='recompose_evosuite', help='recompose evosuite tests')
    args = parser_.parse_args()
    main(args)
