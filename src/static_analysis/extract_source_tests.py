import os
import json
import argparse
import xml.etree.ElementTree as ET
import subprocess


def main(args):

    os.makedirs(f'data/source_test_execution{args.suffix}/{args.project_name}', exist_ok=True)

    if not os.path.exists(f'data/source_test_execution{args.suffix}/{args.project_name}/tests.json'):

        surefire_report_path = f'java_projects/cleaned_final_projects{args.suffix}/{args.project_name}/target/surefire-reports'
        surefire_reports = [f for f in os.listdir(surefire_report_path) if f.endswith('.xml')]
        
        test_details = {}
        for surefire_report in surefire_reports:
            test_class = surefire_report.replace('TEST-', '').replace('.xml', '')

            if args.suffix == '_evosuite' and 'ESTest' not in test_class:
                continue

            test_details.setdefault(test_class, [])
            with open(f'{surefire_report_path}/{surefire_report}', 'r', encoding='utf-8') as f:
                data = f.read()
                root = ET.fromstring(data)
                for testcase in root.findall('testcase'):
                    if testcase.find('skipped') is not None:
                        continue
                    test_name = testcase.attrib['name']

                    if '(' in test_name:
                        if '[' in test_name and test_name.index('[') < test_name.index('('):
                            pass
                        else:
                            test_name = test_name.split('(')[0]
                    
                    if test_name not in test_details[test_class]:
                        test_details[test_class].append(test_name)
        
        with open(f'data/source_test_execution{args.suffix}/{args.project_name}/tests.json', 'w', encoding='utf-8') as f:
            json.dump(test_details, f, indent=4, ensure_ascii=False)

    test_details = {}
    with open(f'data/source_test_execution{args.suffix}/{args.project_name}/tests.json', 'r', encoding="utf-8") as f:
        test_details = json.load(f)

    coverage_details = {}
    for test_class in test_details:
        for test_case in test_details[test_class]:

            print(f'runnig: {test_class}#{test_case}')
            
            status = subprocess.run(f'mvn clean test -Drat.skip=true -Dtest="{test_class}#{test_case}"', shell=True, cwd=f'java_projects/cleaned_final_projects{args.suffix}/{args.project_name}')

            if status.returncode != 0:
                print(f'Error in running test {test_class}#{test_case}')
                continue
            
            assert os.path.exists(f'java_projects/cleaned_final_projects{args.suffix}/{args.project_name}/target/site/jacoco/index.html'), 'Jacoco report not generated'

            coverage_report_path = f'java_projects/cleaned_final_projects{args.suffix}/{args.project_name}/target/site/jacoco/jacoco.xml'
            assert os.path.exists(coverage_report_path), f'Jacoco report not generated for {test_class}#{test_case}'

            coverage_details.setdefault(test_class, {})
            coverage_details[test_class].setdefault(test_case, {})

            with open(coverage_report_path, 'r') as f:
                data = f.read()
                root = ET.fromstring(data)
                for package in root.findall('package'):
                    for class_ in package.findall('class'):
                        coverage_details[test_class][test_case].setdefault(class_.attrib['name'], [])

                        for method in class_.findall('method'):
                            for counter in method.findall('counter'):
                                if counter.attrib['type'] == 'METHOD' and counter.attrib['covered'] != '0':
                                    coverage_details[test_class][test_case][class_.attrib['name']].append(method.attrib['name'])

    with open(f'data/source_test_execution{args.suffix}/{args.project_name}/coverage.json', 'w') as f:
        json.dump(coverage_details, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='extract call graph of preprocessed project')
    parser.add_argument('--project_name', type=str, help='Name of the project')
    parser.add_argument('--suffix', type=str, help='Suffix of the project name')
    args = parser.parse_args()
    main(args)
