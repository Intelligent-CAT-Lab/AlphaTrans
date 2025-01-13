import os
import json
import argparse
from collections import defaultdict
import keyword


def topological_sort(graph: list[tuple[str, str]]) -> list[str]:
    """
    Provides a topological sort of the graph.

    Args:
        graph: A list of tuples where each tuple contains two strings representing the source and target nodes.

    Returns:
        A list of strings representing the nodes in topological order.
    """
    # create a dictionary with the nodes as keys and their dependencies as values
    graph_dict = {}
    for edge in graph:
        if edge[0] not in graph_dict:
            graph_dict[edge[0]] = []
        graph_dict[edge[0]].append(edge[1])

    # create a dictionary with the nodes as keys and their indegree as values
    indegree_dict = {}
    for edge in graph:
        if edge[1] not in indegree_dict:
            indegree_dict[edge[1]] = 0
        if edge[0] not in indegree_dict:
            indegree_dict[edge[0]] = 0
        indegree_dict[edge[1]] += 1

    # create a list of nodes with indegree 0
    zero_indegree = [node for node in indegree_dict if indegree_dict[node] == 0]

    # create a list to store the sorted nodes
    sorted_nodes = []

    # loop over the nodes with indegree 0
    while zero_indegree:
        node = zero_indegree.pop()
        sorted_nodes.append(node)

        # loop over the nodes that depend on the current node
        if node in graph_dict:
            for dependent_node in graph_dict[node]:
                indegree_dict[dependent_node] -= 1
                if indegree_dict[dependent_node] == 0:
                    zero_indegree.append(dependent_node)

    return sorted_nodes


def get_class_order(schema_data):
        """
        Get the order of classes in the schema based on inheritance.
        """
        dependency_graph = set() # set of (dependent, dependency) pairs
        
        for class_ in schema_data['classes']:
            if schema_data['classes'][class_]['extends']:
                if schema_data['classes'][class_]['extends'][0] in schema_data['classes']:
                    dependency_graph.add((class_, schema_data['classes'][class_]['extends'][0]))
                
            if schema_data['classes'][class_]['implements']:
                for interface in schema_data['classes'][class_]['implements']:
                    if interface in schema_data['classes']:
                        dependency_graph.add((class_, interface))
            
            if schema_data['classes'][class_]['nested_inside']:
                dependency_graph.add((class_, schema_data['classes'][class_]['nested_inside']))
                
        class_list = topological_sort(dependency_graph)[::-1]
        
        # check for any classes that were not included in the dependency graph
        class_list += [clz for clz in schema_data['classes'] if clz not in class_list]

        return class_list


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


def get_dependency_path(dependent_class, project_name, suffix):

    src_fname = f'java_projects/cleaned_final_projects{suffix}/{project_name}/src/main/java/' + dependent_class.replace('.', '/') + '.java'
    test_fname = f'java_projects/cleaned_final_projects{suffix}/{project_name}/src/test/java/' + dependent_class.replace('.', '/') + '.java'

    if os.path.exists(src_fname):
        return f'src.main.{dependent_class}'
    elif os.path.exists(test_fname):
        return f'src.test.{dependent_class}'
    else:
        return f'src.main.{dependent_class}'


def remove_duplicate_methods(schema):
    duplicate_methods = {}
    for class_ in schema['classes']:
        duplicate_methods.setdefault(class_, {})
        for method in schema['classes'][class_]['methods']:
            schema['classes'][class_]['methods'][method]['is_overload'] = False
            method_name = method.split(':')[1].strip()
            duplicate_methods[class_].setdefault(method_name, [])
            duplicate_methods[class_][method_name].append(method)

    for class_ in duplicate_methods:
        for method_name in duplicate_methods[class_]:
            if len(duplicate_methods[class_][method_name]) > 1:
                for k in duplicate_methods[class_][method_name]:
                    schema['classes'][class_]['methods'][k]['is_overload'] = True
    
    return schema


def get_dependency_cycle(dependencies):
    adjacency_list = defaultdict(list)
    class_path = {}
    for key, value in dependencies.items():
        for pair in value:
            # if pair[0] == '':
            #     continue
            adjacency_list[key].append(pair[0])
            class_path[pair[0]] = pair[1]

    cycles = []
    for k,v in adjacency_list.copy().items():
        for dependency in v:
            if k in adjacency_list[dependency] and (dependency, k) not in cycles:
                cycles.append((k, dependency))

    return cycles, class_path


def has_child_parent_dept(dependent_files, class_path, project_name, suffix):
    verified_dependent_files = []
    for class_1, class_2 in dependent_files:
        class_1_path = get_dependency_path(class_path[class_1], project_name, suffix)
        class_2_path = get_dependency_path(class_path[class_2], project_name, suffix)

        class_1_schema_name = f'data/schemas{suffix}/{project_name}/{project_name}.{class_1_path}.json'
        class_2_schema_name = f'data/schemas{suffix}/{project_name}/{project_name}.{class_2_path}.json'

        class_1_schema = {}
        with open(class_1_schema_name, 'r') as f:
            class_1_schema = json.load(f)
        
        class_2_schema = {}
        with open(class_2_schema_name, 'r') as f:
            class_2_schema = json.load(f)
        
        for schema_class in class_2_schema['classes']:
            if class_1 in [class_.split('<')[0].replace('new ', '').strip() for class_ in class_2_schema['classes'][schema_class]['extends']]:
                verified_dependent_files.append((class_1, class_1_schema_name, class_2, class_2_schema_name, 0)) if (class_1, class_1_schema_name, class_2, class_2_schema_name, 0) not in verified_dependent_files else None
                continue
            if class_1 in [class_.split('<')[0].replace('new ', '').strip() for class_ in class_2_schema['classes'][schema_class]['implements']]:
                verified_dependent_files.append((class_1, class_1_schema_name, class_2, class_2_schema_name, 0)) if (class_1, class_1_schema_name, class_2, class_2_schema_name, 0) not in verified_dependent_files else None
                continue
        
        for schema_class in class_1_schema['classes']:
            if class_2 in [class_.split('<')[0].replace('new ', '').strip() for class_ in class_1_schema['classes'][schema_class]['extends']]:
                verified_dependent_files.append((class_1, class_1_schema_name, class_2, class_2_schema_name, 1)) if (class_1, class_1_schema_name, class_2, class_2_schema_name, 1) not in verified_dependent_files else None
                continue

            if class_2 in [class_.split('<')[0].replace('new ', '').strip() for class_ in class_1_schema['classes'][schema_class]['implements']]:
                verified_dependent_files.append((class_1, class_1_schema_name, class_2, class_2_schema_name, 1)) if (class_1, class_1_schema_name, class_2, class_2_schema_name, 1) not in verified_dependent_files else None
                continue

    return verified_dependent_files


def main(args):

    with open(f'data/type_resolution/universal_type_map_final.json', 'r') as f:
        extracted_types = json.load(f)
    
    reserved_tokens = dir(__builtins__) + keyword.kwlist
    
    extracted_types = {k.split('.')[-1]: v for k, v in extracted_types.items()}

    schemas = os.listdir(f'data/schemas{args.suffix}/{args.project_name}')

    dependencies_dir = f'data/dependencies{args.suffix}'

    dependencies = {}
    with open(f'{dependencies_dir}/{args.project_name}/dependencies.json', 'r') as f:
        dependencies = json.load(f)

    dependent_files, class_path = get_dependency_cycle(dependencies)
    verified_dependent_files = has_child_parent_dept(dependent_files, class_path, args.project_name, args.suffix)

    for schema_fname in schemas:

        if args.suffix == '_evosuite' and not schema_fname.endswith('ESTest.json'):
            continue

        if args.suffix != '_evosuite' and 'ESTest' in schema_fname:
            continue

        schema_path = f'data/schemas{args.suffix}/{args.project_name}/{schema_fname}'
        
        schema = {}
        with open(schema_path, 'r') as f:
            schema = json.load(f)
        
        schema = remove_duplicate_methods(schema)

        skeleton = 'from __future__ import annotations\n'
        skeleton += '# Imports Begin\n'
        skeleton += '# Imports End\n\n'

        target_schema = schema.copy()
        python_imports = []
        python_imports.append('from __future__ import annotations')
        class_order = get_class_order(schema)

        class_dependencies = []
        for class_ in class_order:

            if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                continue

            source_class_declaration = ''
            with open(schema['path'], 'r') as f:
                source_class_declaration = ''.join(f.readlines()[schema['classes'][class_]['start']-1:schema['classes'][class_]['end']])
            
            if 'enum' in source_class_declaration:
                schema['classes'][class_]['is_enum'] = True
            else:
                schema['classes'][class_]['is_enum'] = False

            dependencies.setdefault(class_, [])

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

            class_declaration = ''
            exceptional_superclasses = {'typing.', 'Comparator', 'Queue', 'Comparable', 'threading.RLock', 'Closeable', 'Enum', 'Iterator', 'Iterable', 'scaffolding', 'Supplier', 'Runnable'}
            if schema['classes'][class_]['extends'] != []:
                schema['classes'][class_]['extends'] = [cls_name.split('<')[0].replace('new ', '').strip() for cls_name in schema['classes'][class_]['extends']]
                schema['classes'][class_]['extends'] = [cls_name.split('(')[0].replace('new ', '').strip() for cls_name in schema['classes'][class_]['extends']]
                schema['classes'][class_]['extends'] = [extracted_types[cls_name] if cls_name in extracted_types and cls_name not in class_path else cls_name for cls_name in schema['classes'][class_]['extends']]
                schema['classes'][class_]['extends'] = [cls_name for cls_name in schema['classes'][class_]['extends'] if not any(substring in cls_name for substring in exceptional_superclasses) and cls_name != class_name]
                if schema['classes'][class_]['is_abstract'] or schema['classes'][class_]['is_interface']:
                    class_declaration = 'class ' + class_name + '(' + ', '.join(schema['classes'][class_]['extends'] + ['ABC']) + '):\n\n'
                else:
                    class_declaration = 'class ' + class_name + '(' + ', '.join(schema['classes'][class_]['extends']) + '):\n\n'
            elif schema['classes'][class_]['implements'] != []:
                schema['classes'][class_]['implements'] = [cls_name.split('<')[0].replace('new ', '').strip() for cls_name in schema['classes'][class_]['implements']]
                schema['classes'][class_]['implements'] = [cls_name.split('(')[0].replace('new ', '').strip() for cls_name in schema['classes'][class_]['implements']]
                schema['classes'][class_]['implements'] = [extracted_types[cls_name] if cls_name in extracted_types and cls_name not in class_path else cls_name for cls_name in schema['classes'][class_]['implements']]
                schema['classes'][class_]['implements'] = [cls_name for cls_name in schema['classes'][class_]['implements'] if not any(substring in cls_name for substring in exceptional_superclasses) and cls_name != class_name]
                if schema['classes'][class_]['is_abstract'] or schema['classes'][class_]['is_interface']:
                    class_declaration = 'class ' + class_name + '(' + ', '.join(schema['classes'][class_]['implements'] + ['ABC']) + '):\n\n'
                else:
                    class_declaration = 'class ' + class_name + '(' + ', '.join(schema['classes'][class_]['implements']) + '):\n\n'
            else:
                if schema['classes'][class_]['is_abstract'] or schema['classes'][class_]['is_interface']:
                    class_declaration = 'class ' + class_name + '(ABC):\n\n'
                else:
                    class_declaration = 'class ' + class_name + ':\n\n'

            is_test_class = False
            for method_ in schema['classes'][class_]['methods']:
                if 'Test' in [x.split('(')[0] for x in schema['classes'][class_]['methods'][method_]['annotations']]:
                    is_test_class = True
                    break

            if 'src.test' in schema_fname and is_test_class:
                if '):' not in class_declaration:
                    class_declaration = class_declaration.replace(':', '(unittest.TestCase):')
                elif '():' in class_declaration:
                    class_declaration = class_declaration.replace('():', '(unittest.TestCase):')
                elif '):' in class_declaration and 'unittest.TestCase' not in class_declaration:
                    class_declaration = class_declaration.replace('):', ', unittest.TestCase):')
                # else:
                #     class_declaration = class_declaration.replace('):', ', unittest.TestCase):')
            if 'src.test' in schema_fname and 'import unittest' not in python_imports:
                python_imports.append('import unittest')
            if 'src.test' in schema_fname and 'import pytest' not in python_imports:
                python_imports.append('import pytest')
            
            # if schema['classes'][class_]['is_enum']:
            #     if '):' not in class_declaration:
            #         class_declaration = class_declaration.replace(':', '(enum.Enum):')
            #     elif '():' in class_declaration:
            #         class_declaration = class_declaration.replace('():', '(enum.Enum):')
            #     else:
            #         class_declaration = class_declaration.replace('):', ', enum.Enum):')
            
            skeleton += class_declaration

            target_schema['classes'][class_]['python_class_declaration'] = class_declaration

            if 'static_initializers' in target_schema['classes'][class_]:
                for static_initializer_se in target_schema['classes'][class_]['static_initializers']:
                    target_schema['classes'][class_]['static_initializers'][static_initializer_se]['partial_translation'] = []
                    target_schema['classes'][class_]['static_initializers'][static_initializer_se]['translation'] = []
                    target_schema['classes'][class_]['static_initializers'][static_initializer_se]['translation_status'] = 'pending'
                    target_schema['classes'][class_]['static_initializers'][static_initializer_se]['syntactic_validation'] = 'pending'
                    target_schema['classes'][class_]['static_initializers'][static_initializer_se]['field_exercise'] = 'pending'
                    target_schema['classes'][class_]['static_initializers'][static_initializer_se]['graal_validation'] = 'pending'
                    target_schema['classes'][class_]['static_initializers'][static_initializer_se]['test_execution'] = 'pending'
                    target_schema['classes'][class_]['static_initializers'][static_initializer_se]['elapsed_time'] = 0
                    target_schema['classes'][class_]['static_initializers'][static_initializer_se]['generation_timestamp'] = 0
                    target_schema['classes'][class_]['static_initializers'][static_initializer_se]['model_name'] = args.model_name if args.model_name else 'deepseek-coder-33b-instruct'
                    target_schema['classes'][class_]['static_initializers'][static_initializer_se]['include_implementation'] = True if args.type == 'body' else False

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
                    if field_type == 'str' and 'char' in [y for x in schema['classes'][class_]['fields'][field]['types'] for y in x]:
                        field_body += "'\\u0000'\n"
                    elif field_type == 'str':
                        field_body += "''\n"
                    elif field_type == 'int':
                        field_body += '0\n'
                    elif field_type == 'float':
                        field_body += '0.0\n'
                    elif field_type == 'bool':
                        field_body += 'False\n'
                    elif field_type == 'List':
                        field_body += '[]\n'
                    elif field_type == 'Dict':
                        field_body += '{}\n'
                    else:
                        field_body += 'None\n'

                elif '=' in ''.join(schema['classes'][class_]['fields'][field]['body']) and (field_type.startswith('typing.List') or field_type.startswith('List')):
                    if 'new ArrayList' in ''.join(schema['classes'][class_]['fields'][field]['body']):
                        field_body += '[]\n'
                    elif 'new LinkedList' in ''.join(schema['classes'][class_]['fields'][field]['body']):
                        field_body += '[]\n'
                    else:
                        field_body += '<placeholder>\n'

                elif '=' in ''.join(schema['classes'][class_]['fields'][field]['body']) and (field_type.startswith('typing.Dict') or field_type.startswith('Dict')):
                    if 'new LinkedHashMap' in ''.join(schema['classes'][class_]['fields'][field]['body']):
                        field_body += '{}\n'
                    elif 'new HashMap' in ''.join(schema['classes'][class_]['fields'][field]['body']):
                        field_body += '{}\n'
                    elif 'new EnumMap' in ''.join(schema['classes'][class_]['fields'][field]['body']):
                        field_body += '{}\n'
                    else:
                        field_body += '<placeholder>\n'

                else:
                    field_body += '<placeholder>\n'

                target_schema['classes'][class_]['fields'][field]['partial_translation'] = f'    {field_body}'.split('\n')
                target_schema['classes'][class_]['fields'][field]['translation'] = []
                target_schema['classes'][class_]['fields'][field]['translation_status'] = 'pending'
                target_schema['classes'][class_]['fields'][field]['syntactic_validation'] = 'pending'
                target_schema['classes'][class_]['fields'][field]['field_exercise'] = 'pending'
                target_schema['classes'][class_]['fields'][field]['graal_validation'] = 'pending'
                target_schema['classes'][class_]['fields'][field]['test_execution'] = 'pending'
                target_schema['classes'][class_]['fields'][field]['elapsed_time'] = 0
                target_schema['classes'][class_]['fields'][field]['generation_timestamp'] = 0
                target_schema['classes'][class_]['fields'][field]['model_name'] = args.model_name if args.model_name else 'deepseek-coder-33b-instruct'
                target_schema['classes'][class_]['fields'][field]['include_implementation'] = True if args.type == 'body' else False

                skeleton += f'\t{field_name}: {field_type} = None\n'
            skeleton += '\t# Class Fields End\n\n'

            skeleton += '\t# Class Methods Begin\n'
            for method in schema['classes'][class_]['methods']:
                current_method = []
                method_name = method.split(':')[1].strip()

                if method_name.strip() == '':
                    continue

                if method_name in reserved_tokens:
                    method_name = f'{method_name}_'

                is_empty_class = False

                is_static = False
                if 'static' in schema['classes'][class_]['methods'][method]['modifiers']:
                    is_static = True
                    skeleton += '\t@staticmethod\n'
                    current_method += ['\t@staticmethod\n']

                updated_method_name = method_name
                if 'protected' in schema['classes'][class_]['methods'][method]['modifiers']:
                    updated_method_name = '_' + method_name if method_name not in ['setUp', 'tearDown'] else method_name
                elif 'private' in schema['classes'][class_]['methods'][method]['modifiers']:
                    updated_method_name = '__' + method_name if method_name not in ['setUp', 'tearDown'] else method_name

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
                    param_types = [(f'{x}_', y) if x in reserved_tokens else (x, y) for x, y in param_types]

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

                if 'src.test' in schema_fname:
                    has_setup_method = False
                    setup_method = ''
                    for m in schema['classes'][class_]['methods']:
                        if 'Before' in [x.split('(')[0] for x in schema['classes'][class_]['methods'][m]['annotations']]:
                            has_setup_method = True
                            setup_method = m
                            break
                    
                    if has_setup_method:
                        schema['classes'][class_]['methods'][method]['calls'].append([schema_fname.replace('.json', ''), class_, setup_method])

                skeleton += f'{return_type}:\n\t\tpass\n\n'
                current_method[-1] = current_method[-1] + f'{return_type}:\n'
                current_method += ['\t\tpass\n\n']
                current_method = [x.replace('\t', '    ') for x in current_method]

                target_schema['classes'][class_]['methods'][method]['partial_translation'] = current_method
                target_schema['classes'][class_]['methods'][method]['translation'] = []
                target_schema['classes'][class_]['methods'][method]['translation_status'] = 'pending'
                target_schema['classes'][class_]['methods'][method]['syntactic_validation'] = 'pending'
                target_schema['classes'][class_]['methods'][method]['field_exercise'] = 'pending'
                target_schema['classes'][class_]['methods'][method]['graal_validation'] = 'pending'
                target_schema['classes'][class_]['methods'][method]['test_execution'] = 'pending'
                target_schema['classes'][class_]['methods'][method]['elapsed_time'] = 0
                target_schema['classes'][class_]['methods'][method]['generation_timestamp'] = 0
                target_schema['classes'][class_]['methods'][method]['model_name'] = args.model_name if args.model_name else 'deepseek-coder-33b-instruct'
                target_schema['classes'][class_]['methods'][method]['include_implementation'] = True if args.type == 'body' else False

                assert '<placeholder>' not in ''.join(current_method)

            skeleton += '\t# Class Methods End\n\n\n'

            if is_empty_class:
                skeleton += '\tpass\n\n'

        import_map = {'ABC': 'from abc import ABC\n', 'Path': 'import pathlib\n', 'IOBase': 'import io\n', 'StringIO': 'import io\n', 'io': 'import io\n', 'threading': 'import threading\n',
                      'BytesIO': 'import io\n', 'TextIOWrapper': 'import io\n', 'Number': 'import numbers\n', 'Callable': 'import typing\nfrom typing import *\n', 'enum': 'import enum\n',
                      'Type': 'import typing\nfrom typing import *\n', 'Any': 'import typing\nfrom typing import *\n', 'Iterator': 'import typing\nfrom typing import *\n', 'decimal': 'import decimal\n',
                      'Dict': 'import typing\nfrom typing import *\n', 'List': 'import typing\nfrom typing import *\n', 'Union': 'import typing\nfrom typing import *\n', 'datetime': 'import datetime\n', 
                      'os': 'import os\n', 'pickle': 'import pickle\n', 'itertools': 'import itertools\n', 'sys': 'import sys\n', 'collections': 'import collections\n', 
                      'unittest.TestCase': 'import unittest\n', 'uuid': 'import uuid\n', 'tempfile': 'import tempfile\n', 'typing': 'import typing\n', 'BytesIO': 'from io import BytesIO\n',
                      'configparser': 'import configparser\n', 'StringIO': 'from io import StringIO\n', 'IOBase': 'from io import IOBase\n', 'Number': 'import numbers\n', 'zoneinfo': 'import zoneinfo\n',
                      'urllib': 'import urllib\n', 'logging': 'import logging\n', 'Enum': 'import enum\n'}

        for key in import_map:
            if key in skeleton and import_map[key] not in skeleton:
                skeleton = skeleton.replace('# Imports Begin\n', '# Imports Begin\n' + import_map[key])
                python_imports.append(import_map[key].strip())
                
        for dependency in class_dependencies:
            for dependent_class in dependency[1]:
                if len(dependent_class) != 2:
                    continue

                path = get_dependency_path(dependent_class[1], args.project_name, args.suffix)
                skip = False
                for class_1, class_1_schema_name, class_2, class_2_schema_name, is_child in verified_dependent_files:
                    if is_child == 1 and schema_fname == class_2_schema_name.split('/')[-1] and class_1 in path:
                        skip = True
                        break
                    if is_child == 0 and schema_fname == class_1_schema_name.split('/')[-1] and class_2 in path:
                        skip = True
                        break
                
                if skip:
                    continue

                if f'from {path} import *' in skeleton:
                    continue
                python_imports.append(f'from {path} import *')
                skeleton = skeleton.replace('# Imports Begin\n', f'# Imports Begin\nfrom {path} import *\n')

        target_schema.setdefault('python_imports', [])

        skeleton = skeleton.replace('\t', '    ')
        skeleton_lines = skeleton.split('\n')
        for i in range(len(skeleton_lines)):
            current_line = skeleton_lines[i]
            for exceptional_import in ['commons.io', 'commons.logging', 'opentest4j', 'com.google', 'org.evosuite', 'scaffolding']:
                if exceptional_import in current_line:
                    skeleton_lines[i] = f'# {current_line}'
                    if current_line in python_imports:
                        python_imports[python_imports.index(current_line)] = f'# {current_line}'
                if 'joda.convert' in current_line and args.project_name == 'joda-money': # resolving these dependencies later
                    skeleton_lines[i] = f'# {current_line}'
                    for import_ in python_imports:
                        if 'joda.convert' in import_ and '#' not in import_:
                            python_imports[python_imports.index(import_)] = f'# {import_}'

        target_schema['python_imports'] = python_imports

        skeleton = '\n'.join(skeleton_lines)
        formatted_schema_fname = '.'.join(schema_fname.split('.')[:-1])

        os.makedirs(f'data/skeletons/{args.project_name}', exist_ok=True)

        formatted_schema_fname = '.'.join(schema_fname.split('.')[:-1])
        sub_dir = "/".join(formatted_schema_fname.replace(".", "/").split("/")[1:-1])
        os.makedirs(f'data/skeletons/{args.project_name}/{sub_dir}', exist_ok=True)
        file_path = f"data/skeletons/{args.project_name}/{sub_dir}/{formatted_schema_fname.split('.')[-1]}.py"
        with open(file_path, 'w') as f:
            f.write(skeleton)
        
        os.system(f'python3 -m black {file_path}') # check for syntactical errors

        # add __init__.py files for each subdirectory
        sub_dirs = sub_dir.split('/')
        for i in range(len(sub_dirs)):
            current_sub_dir = '/'.join(sub_dirs[:i+1])
            with open(f'data/skeletons/{args.project_name}/{current_sub_dir}/__init__.py', 'w') as f:
                f.write('')

        fp = f"data/skeletons/{args.project_name}/{sub_dir}/__init__.py"
        with open(fp, 'w') as f:
            f.write('')

        os.makedirs(f'data/schemas{args.suffix}/translations/{args.model_name}/{args.type}/{args.temperature}/{args.project_name}', exist_ok=True)
        with open(f'data/schemas{args.suffix}/translations/{args.model_name}/{args.type}/{args.temperature}/{args.project_name}/{formatted_schema_fname}_python_partial.json', 'w') as f:
            json.dump(target_schema, f, indent=4)

    # find all .py files in a given directory
    def find_files(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    yield os.path.join(root, file)
    
    # run black on all files in the directory
    for file in find_files(f'data/skeletons/{args.project_name}'):
        print(f'checking {file} for runtime errors...')
        os.system(f'python3 {file}')
    os.system(f'find ./data/skeletons -name "__pycache__" -type d -exec rm -rf {{}} +')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a class skeleton')
    parser.add_argument('--project_name', type=str, dest='project_name', help='name of the project')
    parser.add_argument('--model_name', type=str, dest='model_name', help='name of the model')
    parser.add_argument('--type', type=str, dest='type', help='prompt type signature/body')
    parser.add_argument('--suffix', type=str, dest='suffix', help='suffix')
    parser.add_argument('--temperature', type=float, dest='temperature', help='temperature')
    args = parser.parse_args()
    
    main(args)
