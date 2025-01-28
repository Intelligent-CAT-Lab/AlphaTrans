import os
import json
import subprocess
import argparse
import xml.etree.ElementTree as ET


def compare_coverage(project_name):

    dev_test_jacoco_xml_path = f'java_projects/cleaned_final_projects/{project_name}/target/site/jacoco/jacoco.xml'
    evo_test_jacoco_xml_path = f'java_projects/cleaned_final_projects_evosuite/{project_name}/target/site/jacoco/jacoco.xml'
    
    subprocess.run(f'mvn clean test -Drat.skip -f java_projects/cleaned_final_projects/{project_name}/pom.xml', shell=True, check=True)
    subprocess.run(f'JAVA_HOME=$HOME/.sdkman/candidates/java/11.0.23-kona mvn clean test -Drat.skip -Dtest=*ESTest* -f java_projects/cleaned_final_projects_evosuite/{project_name}/pom.xml', shell=True, check=True)

    dev_tree = ET.parse(dev_test_jacoco_xml_path)
    dev_root = dev_tree.getroot()
    evo_tree = ET.parse(evo_test_jacoco_xml_path)
    evo_root = evo_tree.getroot()

    def get_covered_methods(root, type_):
        classes = root.findall('.//class')
        test_details = {}
        for class_ in classes:
            original_class_name = class_.get('name')
            path_ = original_class_name[:original_class_name.rfind('/')]
            class_name = original_class_name[original_class_name.rfind('/')+1:]
            nested_class_name = original_class_name[original_class_name.rfind('/')+1:]

            test_details.setdefault(original_class_name, {})

            found_exception = False
            for i in range(11):
                if original_class_name.endswith(f'${i}'):
                    found_exception = True
            
            if found_exception:
                continue

            if '$' in original_class_name:
                splitted = original_class_name[original_class_name.rfind('/')+1:].split('$')
                class_name, nested_class_name = splitted[0], splitted[-1]

            methods = class_.findall('method')

            schema = {}
            with open(f'data/schemas_decomposed_tests/translations/gpt-4o-2024-11-20/body/0.0/{project_name}/{project_name}.src.main.{path_.replace("/", ".")}.{class_name}_python_partial.json') as f:
                schema = json.load(f)

            for method in methods:
                method_name = method.get('name')
                if method_name == '<clinit>':
                    continue
                if method_name == '<init>':
                    start_line = int(method.get('line'))
                    if start_line == schema['classes'][nested_class_name]['start']:
                        continue
            
                counters = [counter for counter in method.findall('counter') if counter.get('type') == 'METHOD']
                covered = counters[0].get('covered')

                test_details[original_class_name][method_name] = covered

        with open(f'{type_}.json', 'w') as f:
            json.dump(test_details, f, indent=4)
        
        return test_details

    dev_test_details = get_covered_methods(dev_root, 'dev')
    evo_test_details = get_covered_methods(evo_root, 'evo')

    total_methods = 0
    total_covered_methods = 0
    for class_ in dev_test_details:
        for method in dev_test_details[class_]:
            total_methods += 1
            if evo_test_details[class_][method] == '1':
                total_covered_methods += 1

    print(f'Total methods: {total_methods}')
    print(f'Total covered methods: {total_covered_methods}')

    coverage_details = {}
    with open(f'data/source_test_execution_evosuite/{project_name}/coverage.json') as f:
        coverage_details = json.load(f)

    total_executed_tests = 0
    total_non_covered_fragments = 0
    non_covered_fragments = {}

    for class_ in evo_test_details:
        if class_ not in dev_test_details:
            continue

        for method in evo_test_details[class_]:
            if method not in dev_test_details[class_]:
                continue

            if evo_test_details[class_][method] == '1' and dev_test_details[class_][method] == '0':
                total_non_covered_fragments += 1

                executed_tests = []
                for evosuite_test_class in coverage_details:
                    for evosuite_test_method in coverage_details[evosuite_test_class]:
                        if class_ in coverage_details[evosuite_test_class][evosuite_test_method]:
                            if method in coverage_details[evosuite_test_class][evosuite_test_method][class_]:
                                executed_tests.append(f'{evosuite_test_class}|{evosuite_test_method}')

                non_covered_fragments.setdefault(class_, {})
                non_covered_fragments[class_][method] = executed_tests
                total_executed_tests += len(executed_tests)

    print(f'Total non covered fragments: {total_non_covered_fragments}')
    print(f'Total executed tests: {total_executed_tests}')

    os.makedirs('data/non_covered_fragments', exist_ok=True)
    with open(f'data/non_covered_fragments/{project_name}.json', 'w') as f:
        json.dump(non_covered_fragments, f, indent=4)


def main(args):
    compare_coverage(args.project_name)

    non_covered_fragments = {}
    with open(f'data/non_covered_fragments/{args.project_name}.json') as f:
        non_covered_fragments = json.load(f)

    subprocess.run(['bash', 'scripts/recompose.sh', args.project_name, '0.0', 'gpt-4o-2024-11-20', 'y'])
    subprocess.run(['bash', 'scripts/recompose.sh', args.project_name, '0.0', 'gpt-4o-2024-11-20', 'n'])
    subprocess.run(['bash', 'run.sh'], cwd=f'data/recomposed_projects/gpt-4o-2024-11-20/body/0.0/{args.project_name}')
    subprocess.run(['bash', 'scripts/recompose.sh', args.project_name, '0.0', 'deepseek-coder-33b-instruct', 'n'])
    subprocess.run(['cp', '-r', f'data/recomposed_projects/gpt-4o-2024-11-20/body/0.0/{args.project_name}/evosuite-test', f'data/recomposed_projects/deepseek-coder-33b-instruct/body/0.0/{args.project_name}/'])
    subprocess.run(['bash', 'run.sh'], cwd=f'data/recomposed_projects/deepseek-coder-33b-instruct/body/0.0/{args.project_name}')

    pytest_xml_path = f'data/recomposed_projects/deepseek-coder-33b-instruct/body/0.0/{args.project_name}/pytest-report.xml'

    tree = ET.parse(pytest_xml_path)
    root = tree.getroot()

    unique_test_cases_1 = set()
    unique_fragments_1 = set()

    test_cases = root.findall('.//testcase')
    py_test_results = {}
    for test_case in test_cases:
        test_class_name = test_case.get('classname')
        test_method_name = test_case.get('name')

        # print if test_case has child
        if len(list(test_case)) > 0:
            continue

        py_test_results.setdefault(test_class_name, [])
        py_test_results[test_class_name].append(test_method_name)

    total_validated = 0
    total_validated_fragments = 0
    for class_ in non_covered_fragments:
        for method_ in non_covered_fragments[class_]:
            executed_tests = non_covered_fragments[class_][method_]
            all_test_pass = True
            for exec_evo_test in executed_tests:
                test_class, test_method = exec_evo_test.split('|')
                
                found_passing_test = False
                for py_test_class in py_test_results:
                    if test_class in py_test_class:
                        if test_method in py_test_results[py_test_class]:
                            total_validated += 1
                            found_passing_test = True
                            unique_test_cases_1.add(f'{test_class}::{test_method}')
                            break

                if not found_passing_test:
                    all_test_pass = False
            
            if all_test_pass:
                total_validated_fragments += 1
                unique_fragments_1.add(f'{class_}::{method_}')
                
    pytest_xml_path = f'data/recomposed_projects/gpt-4o-2024-11-20/body/0.0/{args.project_name}/pytest-report.xml'

    tree = ET.parse(pytest_xml_path)
    root = tree.getroot()

    test_cases = root.findall('.//testcase')
    py_test_results = {}
    for test_case in test_cases:
        test_class_name = test_case.get('classname')
        test_method_name = test_case.get('name')

        # print if test_case has child
        if len(list(test_case)) > 0:
            continue

        py_test_results.setdefault(test_class_name, [])
        py_test_results[test_class_name].append(test_method_name)

    unique_test_cases_2 = set()
    unique_fragments_2 = set()

    total_validated = 0
    total_validated_fragments = 0
    for class_ in non_covered_fragments:
        for method_ in non_covered_fragments[class_]:
            executed_tests = non_covered_fragments[class_][method_]
            all_test_pass = True
            for exec_evo_test in executed_tests:
                test_class, test_method = exec_evo_test.split('|')
                
                found_passing_test = False
                for py_test_class in py_test_results:
                    if test_class in py_test_class:
                        if test_method in py_test_results[py_test_class]:
                            total_validated += 1
                            found_passing_test = True
                            unique_test_cases_2.add(f'{test_class}::{test_method}')
                            break

                if not found_passing_test:
                    all_test_pass = False
            
            if all_test_pass:
                total_validated_fragments += 1
                unique_fragments_2.add(f'{class_}::{method_}')

    print('DeepSeekCoder:')
    print('TPR+:', len(unique_test_cases_1))
    print('ATP+:', len(unique_fragments_1))

    print('GPT-4o:')
    print('TPR+:', len(unique_test_cases_2))
    print('ATP+:', len(unique_fragments_2))

    print('Union:')
    print('TPR+:', len(unique_test_cases_1.union(unique_test_cases_2)))
    print('ATP+:', len(unique_fragments_1.union(unique_fragments_2)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare coverage of dev and evosuite tests')
    parser.add_argument('--project_name', type=str, help='Project name')
    args = parser.parse_args()
    main(args)
