import os
import subprocess
import xml.etree.ElementTree as ET
from calculate_coverage import calculate_method_coverage


def test_validation(args, eligible_tests):

    os.system(f'python3 src/postprocessing/recompose.py --project_name={args.project_name} \
                                                        --model_name={args.model_name} \
                                                        --output_dir=data/recomposed_projects \
                                                        --temperature={args.temperature} \
                                                        --type={args.prompt_type} \
                                                        --suffix={args.suffix}')

    test_execution_results = {}
    failed_tests = []
    for test in eligible_tests:

        test_path = test['schema_name'].replace('.', '/') + '.java'
        test_path = test_path[test_path.index(args.project_name):].replace('test/java/org', 'test/org').replace('.java', '.py')
        test_class = test['class_name']
        test_method = test['fragment_name'].split(':')[1]

        if not test_method.startswith('test'):
            test_method = 'test' + test_method

        if '_decomposed' in test_method:
            actual_test_name = test_method[:test_method.index('_decomposed')].split('_')[0]
        else:
            actual_test_name = test_method

        if actual_test_name in failed_tests:
            continue

        test_execution_results.setdefault(f'{test_path}::{test_class}::{test_method}', {'test_outcome': 'exercised-success', 'feedback': '', 'covered_methods': []})

        if os.path.exists(f'{args.project_name}-{args.model_name}-pytest-report.xml'):
            os.remove(f'{args.project_name}-{args.model_name}-pytest-report.xml')
        if os.path.exists(f'{args.project_name}-{args.model_name}-coverage.xml'):
            os.remove(f'{args.project_name}-{args.model_name}-coverage.xml')

        current_dir = os.getcwd()
        env = os.environ.copy()
        env['PYTHONPATH'] = f'{current_dir}/data/recomposed_projects/{args.model_name}/{args.prompt_type}/{args.temperature}/{args.project_name}'
        
        try:
            subprocess.run(
                [
                    'pytest', f'data/recomposed_projects/{args.model_name}/{args.prompt_type}/{args.temperature}/{test_path}::{test_class}::{test_method}',
                    '--cov=src.main',
                    '--cov=src.test',
                    '--cov-report=term-missing',
                    f'--cov-report=xml:{args.project_name}-{args.model_name}-coverage.xml',
                    f'--junitxml={args.project_name}-{args.model_name}-pytest-report.xml'
                ],
                check=True,
                capture_output=True,
                text=True,
                env=env
            )
        except subprocess.CalledProcessError as e:
            test_execution_results[f'{test_path}::{test_class}::{test_method}']['test_outcome'] = 'exercised-failed'
            failed_tests.append(actual_test_name)
                    
        if not os.path.exists(f'{args.project_name}-{args.model_name}-coverage.xml'):
            test_execution_results[f'{test_path}::{test_class}::{test_method}']['test_outcome'] = 'exercised-failed'
            failed_tests.append(actual_test_name)
        else:
            covered_methods = calculate_method_coverage(args, f'data/recomposed_projects/{args.model_name}/{args.prompt_type}/{args.temperature}/{args.project_name}')
            test_execution_results[f'{test_path}::{test_class}::{test_method}']['covered_methods'] = covered_methods

        assert os.path.exists(f'{args.project_name}-{args.model_name}-pytest-report.xml')
        with open(f'{args.project_name}-{args.model_name}-pytest-report.xml', 'r') as f:
            tree = ET.parse(f)
            root = tree.getroot()
            for testcase in root.findall('.//testcase'):
                if testcase.get('name') == test_method:
                    if testcase.find('failure') is not None:
                        test_execution_results[f'{test_path}::{test_class}::{test_method}']['feedback'] = testcase.find('failure').text
                    elif testcase.find('error') is not None:
                        test_execution_results[f'{test_path}::{test_class}::{test_method}']['feedback'] = testcase.find('error').text
                    break
        
        if test_execution_results[f'{test_path}::{test_class}::{test_method}']['test_outcome'] == 'exercised-failed' and test_execution_results[f'{test_path}::{test_class}::{test_method}']['feedback'] == '':
            test_execution_results[f'{test_path}::{test_class}::{test_method}']['feedback'] = 'test did not execute properly'

    return test_execution_results
