import os
import json
import argparse


def main(args):
    all_types = []
    all_classes = []
    filenames = os.listdir(f'data/schemas{args.suffix}/{args.project_name}')

    for filename in filenames:
        data = {}
        with open(f'data/schemas{args.suffix}/{args.project_name}/{filename}', 'r') as f:
            data = json.load(f)

        for class_ in data['classes']:
            all_classes.append(class_)

            for field in data['classes'][class_]['fields']:
                # print(data['classes'][class_]['fields'][field]['types'])
                all_types.append(data['classes'][class_]['fields'][field]['types'][0][1])

            for method in data['classes'][class_]['methods']:
                # print(data['classes'][class_]['methods'][method]['return_types'])
                all_types.append(data['classes'][class_]['methods'][method]['return_types'][0][1])

                # signature = data['classes'][class_]['methods'][method]['signature'][data['classes'][class_]['methods'][method]['signature'].find('(')+1:data['classes'][class_]['methods'][method]['signature'].find(')')]
                # signature_types = [x.strip() for x in signature.split(',') if x.strip() != '']
                # all_types += signature_types

    types_query_output = []
    with open(f'data/query_outputs{args.suffix}/{args.project_name}/{args.project_name}_types.txt', 'r') as f:
        types_query_output = f.readlines()

    for type_ in types_query_output:
        out = [x.strip() for x in type_.split('|') if x.strip() != '']
        type_name, qualified_name = out

        if 'java' in qualified_name:
            new_name = qualified_name[1:-1].split('/')[:-1]
            all_types.append('.'.join(new_name) + '.' + type_name)
        else:
            all_types.append(type_name)

    print('total types:', len(all_types + all_classes))
    all_classes = list(set(all_classes))
    all_types = set([x for x in all_classes + all_types if '...' not in x])
    print('total unique types:', len(all_types))

    formatted_project_name = args.project_name.replace('-', '_')
    os.makedirs(f'data/custom_types/{formatted_project_name}', exist_ok=True)
    os.makedirs(f'data/type_resolution/{args.project_name}', exist_ok=True)
    os.makedirs(f'data/templates/{args.project_name}', exist_ok=True)
    
    templates_content = ''

    type_dct = {}
    for type_ in all_types:
        type_dct.setdefault(type_, '')
        if type_ in all_classes:
            type_dct[type_] = type_
            templates_content += f'from data.custom_types.{formatted_project_name}.{type_} import {type_}\n'
            with open(f'data/custom_types/{formatted_project_name}/{type_}.py', 'w') as f:
                f.write(f'class {type_}:\n    pass\n')

    templates_content += "\n".join(["from typing import *", "import collections", "import typing", "import sqlalchemy", "import builtins", "import io", "import sys", "import itertools", 
                                    "import urllib", "import copy", "import datetime", "import functools", "import os", "import pickle", "import numbers", "from numbers import *", "import re", 
                                    "import decimal", "import enum", "import uuid", "import math", "import threading", "import ipaddress", "import socket", "import http", "import random",
                                    "import idna", "import locale", "import weakref", "import concurrent", "import asyncio", "def main(a: <placeholder>):", "    pass"])
    templates_content += "\n"

    with open(f'data/templates/{args.project_name}/template.py', 'w') as f:
        f.write(templates_content)

    total_app_type_resolved = 0
    for type_ in type_dct:
        if type_dct[type_] != '':
            total_app_type_resolved += 1
    print('total resolved:', total_app_type_resolved)
    print('-'*50)
    with open(f'data/type_resolution/{args.project_name}/s1_input.json', 'w') as f:
        json.dump(type_dct, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract types from schemas')
    parser.add_argument('--project_name', type=str, help='Name of the project')
    parser.add_argument('--suffix', type=str, help='Suffix for the project')
    args = parser.parse_args()
    main(args)
