
import argparse
import os
import json
import xml.etree.ElementTree as ET


def main(args):

    surefire_reports_path = f'java_projects/cleaned_final_projects/{args.project_name}/target/surefire-reports'
    assert os.path.exists(surefire_reports_path)

    # Extract executed tests from the project
    xml_reports = []
    for file in os.listdir(surefire_reports_path):
        if file.endswith('.xml'):
            xml_reports.append(file)

    executed_tests = {}
    for f in xml_reports:
        tree = ET.parse(f'{surefire_reports_path}/{f}')
        root = tree.getroot()
        for child in root:
            if child.tag == 'testcase':
                executed_tests.setdefault(child.attrib['classname'], [])
                executed_tests[child.attrib['classname']].append(child.attrib['name'])

    os.makedirs(f'data/executed_tests/{args.project_name}', exist_ok=True)
    with open(f'data/executed_tests/{args.project_name}/executed_tests.json', 'w') as f:
        json.dump(executed_tests, f, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract executed tests from the project')
    parser.add_argument('--project_name', type=str, help='Name of the project')
    args = parser.parse_args()
    main(args)
