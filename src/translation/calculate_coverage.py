import os
import ast
import xml.etree.ElementTree as ET
import json


def calculate_method_coverage(args, project_root):
    """
    Calculate the number of covered methods based on the coverage report.
    """

    reserved_tokens = ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip', 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

    py_file_paths = []
    for root, _, files in os.walk(project_root):
        for file in files:
            if file.endswith('.py'):
                py_file_paths.append(os.path.join(root, file))
    
    covered_methods = []
    for py_file_path in py_file_paths:

        with open(py_file_path, "r") as source_file:
            tree = ast.parse(source_file.read(), filename=py_file_path)
            methods = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]

        covered_lines = get_covered_lines(f'{args.project_name}-{args.model_name}-coverage.xml', py_file_path)
        for method in methods:
            method_lines = range(method.lineno + 1, method.end_lineno + 1)
            if any(line in covered_lines for line in method_lines):
                if method.name in ['initialize_fields', 'run_static_init']:
                    continue
                class_name = None
                for class_ in classes:
                    if class_.lineno <= method.lineno and class_.end_lineno >= method.end_lineno:
                        class_name = class_.name
                        break

                assert class_name is not None

                covered_method_schema_data = {}
                with open(f'{args.translation_dir}/{py_file_path[py_file_path.index(args.project_name):].replace(".py", "").replace("/", ".")}_python_partial.json', 'r') as f:
                    covered_method_schema_data = json.load(f)
                
                method_name = method.name
                if method.name == '__init__':
                    method_name = class_name

                for method_ in covered_method_schema_data['classes'][class_name]['methods']:
                    if method_name.endswith('_'):
                        potential_keyword_name = method_name[:-1]
                        if potential_keyword_name in reserved_tokens and potential_keyword_name == method_.split(':')[1]:
                            method_name = method_
                            break
                    elif method_name == class_name:
                        if method_.split(':')[1] == method_name:
                            method_name = method_
                            break
                    elif 'protected' in covered_method_schema_data['classes'][class_name]['methods'][method_]['modifiers']:
                        if f"_{method_.split(':')[1]}" == method_name:
                            method_name = method_
                            break
                    elif 'private' in covered_method_schema_data['classes'][class_name]['methods'][method_]['modifiers']:
                        if f"__{method_.split(':')[1]}" == method_name:
                            method_name = method_
                            break
                    elif method_name.startswith('test') and method_name[4:] == method_.split(':')[1]:
                        method_name = method_
                        break
                    else:
                        if method_.split(':')[1] == method_name:
                            method_name = method_
                            break
                
                if ':' not in method_name:
                    print(f'{method_name} not found in schema {py_file_path}::{class_name}')
                    continue

                covered_methods.append({'file': py_file_path[py_file_path.index(args.project_name):].replace('.py', '').replace('/', '.'), 'class': class_name, 'method': method_name})

    return covered_methods


def get_covered_lines(xml_file, file_name):
    """
    Parse the coverage XML file and return the set of covered lines.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    covered_lines = set()

    for class_ in root.findall(".//class[@filename='{}']".format(file_name)):
        for line in class_.findall(".//line"):
            if line.get('hits') != '0':
                covered_lines.add(int(line.get('number')))

    return covered_lines
