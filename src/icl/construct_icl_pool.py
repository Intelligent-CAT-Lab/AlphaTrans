import json
import difflib
import argparse
from tree_sitter import Language, Parser


def get_method_signature(node, source_bytes):
    """Extract method signature from a method invocation node"""
    # Find the method name identifier
    method_name_node = None
    arguments_node = None
    
    for child in node.children:
        if child.type == 'identifier':
            method_name_node = child
        elif child.type == 'argument_list':
            arguments_node = child
    
    if method_name_node:
        method_name = source_bytes[method_name_node.start_byte:method_name_node.end_byte].decode('utf-8')
        
        # Build argument types string (for this example, we'll use simple signatures)
        # In a real implementation, you would need to resolve the actual types
        if arguments_node:
            return f"{method_name}"
        return f"{method_name}"
    
    return None


def extract_method_signatures(node, source_bytes):
    """Extract all method signatures from a node"""
    signatures = []
    
    if node.type == 'method_invocation':
        signature = get_method_signature(node, source_bytes)
        if signature:
            signatures.append(signature)
    
    for child in node.children:
        signatures.extend(extract_method_signatures(child, source_bytes))
        
    return signatures


def extract_complex_statements(node, source_bytes, prefix=''):
    """Recursively extract complex statements with their nested structure"""
    statements = []

    if node.type in ['if_statement', 'for_statement', 'while_statement', 'do_statement', 'switch_statement', 'try', 'try_statement', 'try_with_resources_statement', 'catch', 'catch_clause', 'finally', 'finally_clause', 'enhanced_for_statement']:
        # Get the full text of the statement
        start_byte = node.start_byte
        end_byte = node.end_byte
        code = source_bytes[start_byte:end_byte].decode('utf-8')
        
        node_type = node.type.split('_')[0]
        if node_type == 'enhanced':
            node_type = 'for'

        # Create label based on the type and nesting
        if prefix:
            label = f"{prefix}_{node_type}"
        else:
            label = node_type
        
        signatures = extract_method_signatures(node, source_bytes)

        statements.append({
            'code': code,
            'label': label,
            'signatures': signatures
        })
        
        # Process children with updated prefix
        for child in node.children:
            statements.extend(extract_complex_statements(child, source_bytes, label))
    else:
        # Continue searching in children
        for child in node.children:
            statements.extend(extract_complex_statements(child, source_bytes, prefix))
            
    return statements


def generate_diff(partial: str, manual: str) -> str:
    partial_lines = partial.strip().splitlines()
    manual_lines = manual.strip().splitlines()

    diff = difflib.unified_diff(partial_lines, manual_lines, lineterm='')

    return '\n'.join(diff)


def main(args):

    JAVA_LANGUAGE = Language('misc/parser/my-languages.so', 'java')

    parser = Parser()
    parser.set_language(JAVA_LANGUAGE)

    icl_pool = []
    for project_name in ['commons-cli', 'commons-csv', 'commons-validator', 'commons-fileupload']:

        print(f"Project: {project_name}")

        reserved_tokens = ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip', 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

        partial = {}
        with open(f'data/icl_pool/{project_name}_analysis_results_partial.json', 'r') as f:
            partial = json.load(f)

        manual = {}
        with open(f'data/icl_pool/{project_name}_analysis_results_manual.json', 'r') as f:
            manual = json.load(f)

        api_docs = {}
        with open(f'data/crawl/java.base_module_doc.json', 'r') as f:
            api_docs = json.load(f)

        total_methods = 0
        changed_methods = 0
        added_methods = 0
        no_diff_methods = 0

        for file_path in partial:
            assert file_path in manual, f"File {file_path} not found in manual analysis results"

            for class_name in partial[file_path]:
                assert class_name in manual[file_path], f"Class {class_name} not found in manual analysis results for file {file_path}"

                for method_name in partial[file_path][class_name]:
                    # assert method_name in manual[file_path][class_name], f"Method {method_name} not found in manual analysis results for class {class_name} in file {file_path}"
                    if method_name not in manual[file_path][class_name]: # this is a rare case
                        added_methods += 1
                        # print(f"Method {method_name} not found in manual analysis results for class {class_name} in file {file_path}")
                        continue

                    total_methods += 1

                    diff = generate_diff(
                        '\n'.join(partial[file_path][class_name][method_name]['method_body']),
                        '\n'.join(manual[file_path][class_name][method_name]['method_body'])
                    )

                    if not diff: # No difference, hence correct translation
                        no_diff_methods += 1
                        continue
                    if diff:
                        changed_methods += 1

                    if 'initialize_fields' in method_name: # skip methods created during recomposition since no source code is available
                        continue

                    fragment_type = 'methods'
                    if 'run_static_init' in method_name:
                        fragment_type = 'static_initializers'

                    incorrect_translation = '\n'.join(partial[file_path][class_name][method_name]['method_body'])
                    correct_translation = '\n'.join(manual[file_path][class_name][method_name]['method_body'])

                    schema_name = f'{project_name}.{file_path.replace("/", ".").replace(".py", "")}.json'

                    schema_data = {}
                    with open(f'data/schemas_decomposed_tests/{project_name}/{schema_name}', 'r') as fr:
                        schema_data = json.load(fr)
                    
                    source_code = ''
                    query_method_name = ''
                    for method_ in schema_data['classes'][class_name][fragment_type]:
                        if method_name.endswith('_') and method_name != '__init__':
                            potential_keyword_name = method_name[:-1]
                            if potential_keyword_name in reserved_tokens and potential_keyword_name == method_.split(':')[1]:
                                query_method_name = method_
                                break
                        elif method_.split(':')[1] == method_name:
                            query_method_name = method_
                            break
                        elif method_name == '__init__':
                            if method_.split(':')[1] == class_name:
                                query_method_name = method_
                                break
                        elif 'protected' in schema_data['classes'][class_name][fragment_type][method_]['modifiers']:
                            if f"_{method_.split(':')[1]}" == method_name:
                                query_method_name = method_
                                break
                        elif 'private' in schema_data['classes'][class_name][fragment_type][method_]['modifiers']:
                            if f"__{method_.split(':')[1]}" == method_name:
                                query_method_name = method_
                                break
                        elif method_name.startswith('test') and method_name[4:] == method_.split(':')[1]:
                            query_method_name = method_
                            break
                        else:
                            if method_.split(':')[1] == method_name:
                                source_code = ''.join(schema_data['classes'][class_name][fragment_type][method_]['body'])
                                break

                    if query_method_name == '':
                        all_candidate_methods = []
                        for method_ in schema_data['classes'][class_name][fragment_type]:
                            if f':{method_name}_' in method_:
                                all_candidate_methods.append(method_)
                        
                        if all_candidate_methods == []:
                            temp_method_name = method_name
                            if method_name.startswith('test'):
                                temp_method_name = method_name[4:]

                            for method_ in schema_data['classes'][class_name][fragment_type]:
                                if f':{temp_method_name}_' in method_:
                                    all_candidate_methods.append(method_)

                        if all_candidate_methods == []:
                            continue

                        sorted_candidate_methods = sorted(all_candidate_methods, key=lambda x: int(x.split('_test')[1].split('_')[0]))
                        query_method_name = sorted_candidate_methods[-1]


                    source_code = ''.join(schema_data['classes'][class_name][fragment_type][query_method_name]['body'])
                    
                    assert source_code, f"Source code not found for {method_name} in {class_name} in {file_path}"

                    calls = []

                    if fragment_type == 'methods':
                        calls = schema_data['classes'][class_name]['methods'][query_method_name]['calls']

                    tree = parser.parse(bytes(source_code, 'utf-8'))                    
                    statements = extract_complex_statements(tree.root_node, bytes(source_code, 'utf-8'))

                    # print(file_path)
                    # print(class_name)
                    # print(method_name)
                    # print(incorrect_translation)
                    # print(correct_translation)
                    # print(diff)
                    # print(source_code)
                    # print(calls)
                    # print('-' * 100)

                    available_library_methods = []
                    for call_schema_name, call_class_name, call_method_name in calls:
                        if call_schema_name != 'library':
                            continue

                        if 'java.base' not in call_class_name: # call_class_name could be Assert
                            # exit()
                            continue
                        
                        formatted_package_name = '.'.join(call_class_name.split('/')[1:-1])
                        formatted_class_name = call_class_name.split('/')[-1]

                        for class_ in api_docs['java.base'][formatted_package_name]:

                            if formatted_class_name not in api_docs['java.base'][formatted_package_name][class_]:
                                continue
                            
                            if call_method_name == formatted_class_name:
                                for constructor__ in api_docs['java.base'][formatted_package_name][class_][formatted_class_name]['constructors']:
                                    available_library_methods.append({'signature': constructor__, 'complete_signature': api_docs['java.base'][formatted_package_name][class_][formatted_class_name]['constructors'][constructor__]['signature'].split('\n'), 'description': api_docs['java.base'][formatted_package_name][class_][formatted_class_name]['constructors'][constructor__]['description'].split('\n'), 'notes': api_docs['java.base'][formatted_package_name][class_][formatted_class_name]['constructors'][constructor__]['notes'].split('\n')})
                            else:
                                for method__ in api_docs['java.base'][formatted_package_name][class_][formatted_class_name]['methods']:
                                    if method__ == call_method_name:
                                        available_library_methods.append({'signature': method__, 'complete_signature': api_docs['java.base'][formatted_package_name][class_][formatted_class_name]['methods'][method__]['signature'].split('\n'), 'description': api_docs['java.base'][formatted_package_name][class_][formatted_class_name]['methods'][method__]['description'].split('\n'), 'notes': api_docs['java.base'][formatted_package_name][class_][formatted_class_name]['methods'][method__]['notes'].split('\n')})

                    library_apis = [x[2].split('(')[0] for x in calls if x[0] == 'library']
                    code_constructs = {}
                    print(source_code)
                    for x in statements:
                        print(x['label'])
                        print(x['signatures'])
                        print(x['code'])
                        print('-' * 100)
                        code_constructs.setdefault(x['label'], [])
                        for y in x['signatures']:
                            if y in library_apis and y not in code_constructs[x['label']]:
                                code_constructs[x['label']].append(y)

                    icl_instance = {}
                    icl_instance['project_name'] = project_name
                    icl_instance['source_code'] = source_code.split('\n')
                    icl_instance['code_constructs'] = code_constructs
                    icl_instance['library_calls'] = [x for x in calls if x[0] == 'library']
                    icl_instance['library_api_details'] = available_library_methods
                    icl_instance['target_signature'] = manual[file_path][class_name][method_name]['method_signature']
                    icl_instance['incorrect_translation'] = incorrect_translation.split('\n')
                    icl_instance['correct_translation'] = correct_translation.split('\n')
                    icl_instance['diff'] = diff.split('\n')
                    icl_pool.append(icl_instance)

        print(f"Total methods: {total_methods}")
        print(f"Changed: {changed_methods} ({changed_methods / total_methods * 100:.2f}%)")
        print(f"Added: {added_methods} ({added_methods / total_methods * 100:.2f}%)")
        print(f"No change: {no_diff_methods} ({no_diff_methods / total_methods * 100:.2f}%)")
        print()

    print('total icl examples:', len(icl_pool))
    with open('data/icl_pool/icl_pool.json', 'w') as f:
        json.dump(icl_pool, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate diff between partial and manual analysis results')
    args = parser.parse_args()
    main(args)
