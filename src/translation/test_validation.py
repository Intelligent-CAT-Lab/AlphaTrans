import os
import json
import subprocess
import re
from subprocess import Popen


def parse_pytest_exec(content):

    parsed = [[], [], [], []]
    while content:
        line = content.pop(0)
        if '= test session starts =' in line:
            parsed[0].append(line)
            while content:
                line = content.pop(0)
                if '= ERRORS =' in line:
                    content.insert(0, line)
                    break
                parsed[0].append(line)
        elif '= ERRORS =' in line:
            parsed[1].append(line)
            while content:
                line = content.pop(0)
                if '= FAILURES =' in line:
                    content.insert(0, line)
                    break
                parsed[1].append(line)
        elif '= FAILURES =' in line:
            parsed[2].append(line)
            while content:
                line = content.pop(0)
                if '= short test summary info =' in line:
                    content.insert(0, line)
                    break
                parsed[2].append(line)
        elif '= short test summary info =' in line:
            parsed[3].append(line)
            while content:
                line = content.pop(0)
                parsed[3].append(line)
    
    return parsed


def extract_fragment_location(traceback, project_name):
    index = -1
    while index >= -len(traceback):
        if traceback[index].strip().startswith('File') and project_name in traceback[index]:
            break
        index -= 1

    traceback = '\n'.join(traceback[index:])

    # Regular expression to extract the file path and function name
    pattern = r'File "([^"]+)", line \d+, in (\w+)'

    # Using re.search to find the match
    match = re.search(pattern, traceback)

    if match:
        file_path = match.group(1)
        function_name = match.group(2)
        if function_name.strip() == '__init__':
            function_name = file_path.split('/')[-1].replace('.py', '')
        elif function_name.strip().startswith('__'):
            function_name = function_name.strip()[2:]
        elif function_name.strip().startswith('_'):
            function_name = function_name.strip()[1:]
        return traceback.replace(file_path, 'script.py'), file_path, function_name
    else:
        raise Exception("No match found")


def test_validation(schema, fragment_class, fragment_method, project_name, processed_fragments, model_name, type_):

    os.system(f'python3 src/postprocessing/recompose.py --project_name={project_name} --model_name={model_name} --output_dir=data/recomposed_projects --type={type_}')

    global_call_graph = {}
    with open(f'data/call_graphs/{project_name}/call_graph.json', 'r') as f:
        global_call_graph = json.load(f)

    test_focal_method_map = {}
    for class_ in global_call_graph:
        for test_method in global_call_graph[class_]:
            if test_method == 'schema_file':
                continue

            test_focal_method_map.setdefault(f"{global_call_graph[class_]['schema_file']}|{class_}|{test_method}", [])
            for focal_method in global_call_graph[class_][test_method]:
                test_focal_method_map[f"{global_call_graph[class_]['schema_file']}|{class_}|{test_method}"].append(f"{focal_method['schema']}|{focal_method['class']}|{focal_method['method']}")

    executable_tests = []
    for test in test_focal_method_map:
        if 'src/test' not in test:
            continue
        if f'{schema.replace("_python_partial.json", "")}|{fragment_class}|{fragment_method}' not in test_focal_method_map[test]:
            continue

        if all(focal_method in processed_fragments for focal_method in test_focal_method_map[test] if focal_method != f'{schema.replace("_python_partial.json", "")}|{fragment_class}|{fragment_method}'):
            executable_tests.append(test)

    green_tests = True
    feedback, file_path, function_name = None, None, None
    for test in executable_tests:
        test_path, test_class, test_method = test.split('|')
        test_path = test_path[test_path.index(project_name):].replace('test/java/org', 'test/org').replace('.java', '.py')
        test_method = test_method.split(':')[1]

        p = Popen(['python3', '-m', 'pytest', f'data/recomposed_projects/{model_name}/{type_}/{test_path}::{test_class}::{test_method}'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        try:
            stdout, stderr = p.communicate(timeout=100)
        except subprocess.TimeoutExpired:
            continue

        stdout_data = stdout.decode('utf-8')

        parsed_output = parse_pytest_exec(stdout_data.split('\n'))

        if parsed_output[1] or parsed_output[2]:
            green_tests = False
            feedback = parsed_output[2]
            try:
                feedback, file_path, function_name = extract_fragment_location(feedback, project_name)
            except Exception as e:
                pass
            break
    
    return green_tests, feedback, file_path, function_name, 'AttributeError' in feedback if feedback else False
