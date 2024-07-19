import os
import json
import subprocess
from subprocess import Popen
import xml.etree.ElementTree as ET
from calculate_coverage import calculate_method_coverage


def test_validation(args, eligible_tests, fragment_test_stats):

    os.system(f'python3 src/postprocessing/recompose.py --project_name={args.project_name} --model_name={args.model_name} --output_dir=data/recomposed_projects --type={args.prompt_type}')

    green_tests = True
    feedback = 'the test did not execute successfully'
    for test in eligible_tests:
        test_path = test['schema_name'].replace('.', '/') + '.java'
        test_path = test_path[test_path.index(args.project_name):].replace('test/java/org', 'test/org').replace('.java', '.py')
        test_class = test['class_name']
        test_method = test['fragment_name'].split(':')[1]

        if os.path.exists(f'{args.project_name}-pytest-report.xml'):
            os.remove(f'{args.project_name}-pytest-report.xml')
        if os.path.exists(f'{args.project_name}-coverage.xml'):
            os.remove(f'{args.project_name}-coverage.xml')

        try:
            subprocess.run(
                [
                    'pytest', f'data/recomposed_projects/{args.model_name}/{args.prompt_type}/{test_path}::{test_class}::{test_method}',
                    '--cov=src.main',
                    '--cov=src.test',
                    '--cov-report=term-missing',
                    f'--cov-report=xml:{args.project_name}-coverage.xml',
                    f'--junitxml={args.project_name}-pytest-report.xml'
                ],
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            green_tests = False
        
        if not os.path.exists(f'{args.project_name}-coverage.xml'):
            green_tests = False
            covered_methods = []
        else:
            covered_methods = calculate_method_coverage(args, f'data/recomposed_projects/{args.model_name}/{args.prompt_type}/{args.project_name}')

        assert os.path.exists(f'{args.project_name}-pytest-report.xml')
        with open(f'{args.project_name}-pytest-report.xml', 'r') as f:
            tree = ET.parse(f)
            root = tree.getroot()
            for testcase in root.findall('.//testcase'):
                if testcase.get('name') == test_method:
                    if testcase.find('failure') is not None:
                        feedback = testcase.find('failure').text
                    elif testcase.find('error') is not None:
                        feedback = testcase.find('error').text
                    break

        for covered_method in covered_methods:
            covered_method_file = covered_method['file'][covered_method['file'].index(args.project_name):].replace('.py', '').replace('/', '.')
            covered_method_class = covered_method['class']
            covered_method_name = covered_method['method']

            fragment_test_stats.setdefault(f'{covered_method_file}|{covered_method_class}|{covered_method_name}', {'total': [], 'pass': [], 'fail': []})

            fragment_test_stats[f'{covered_method_file}|{covered_method_class}|{covered_method_name}']['total'].append(f'{test_path}|{test_class}|{test_method}')
            if green_tests:
                fragment_test_stats[f'{covered_method_file}|{covered_method_class}|{covered_method_name}']['pass'].append(f'{test_path}|{test_class}|{test_method}')
            else:
                fragment_test_stats[f'{covered_method_file}|{covered_method_class}|{covered_method_name}']['fail'].append(f'{test_path}|{test_class}|{test_method}')

        if not green_tests:
            break

    return green_tests, feedback, covered_methods
