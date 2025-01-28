import json
import os
import argparse


def main(args):

    prefix_ = f'{args.translation_dir}/{args.model_name}/body/0.0'

    schemas_path = f'{prefix_}/{args.project_name}/'
    subject_cases = []
    test_exec_details = {}

    for schema_file in os.listdir(schemas_path):

        if not schema_file.endswith('_python_partial.json'):
            continue

        if 'ESTest' in schema_file:
            continue

        data = {}
        with open(f'{schemas_path}/{schema_file}', 'r') as f:
            data = json.load(f)

        for class_ in data['classes']:

            if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                continue

            for method_ in data['classes'][class_]['methods']:

                if data['classes'][class_]['methods'][method_]['is_overload']:
                    continue

                if 'src.test' in schema_file:
                    continue

                # only interested in exercised methods
                if isinstance(data['classes'][class_]['methods'][method_]['test_execution'], dict):

                    test_exec_details.setdefault(class_, {})
                    test_exec_details[class_].setdefault(method_, {})

                    for test_case in data['classes'][class_]['methods'][method_]['test_execution']:

                        test_path, test_class, test_method = test_case.split('::')
                        
                        assert '_decomposed' in test_method, f'{test_method}'

                        unique_test_method = test_method.split('_test')[0]

                        test_exec_details[class_][method_].setdefault(test_path, {})
                        test_exec_details[class_][method_][test_path].setdefault(test_class, {})
                        test_exec_details[class_][method_][test_path][test_class].setdefault(unique_test_method, {})
                        test_exec_details[class_][method_][test_path][test_class][unique_test_method][test_method] = data['classes'][class_]['methods'][method_]['test_execution'][test_case]['test_outcome']

    # for class_ in test_exec_details:
    #     print(class_)
    #     for method_ in test_exec_details[class_]:
    #         print(f'\t{method_}')
    #         for test_path in test_exec_details[class_][method_]:
    #             print(f'\t\t{test_path}')
    #             for test_class in test_exec_details[class_][method_][test_path]:
    #                 print(f'\t\t\t{test_class}')
    #                 for test_method in test_exec_details[class_][method_][test_path][test_class]:
    #                     if len(test_exec_details[class_][method_][test_path][test_class][test_method]) == 1:
    #                         continue
    #                     print(f'\t\t\t\t{test_method}')
    #                     for test_case in sorted(test_exec_details[class_][method_][test_path][test_class][test_method], key=lambda x: int(test_case.split('_')[-2][4:])):
    #                         print(f'\t\t\t\t\t{test_case}: {test_exec_details[class_][method_][test_path][test_class][test_method][test_case]}')
    #                     print()
    #                 print()
    # exit()


    pass_rate = []
    total_tests = []
    total_tests_w_decomposition = []
    total_decomposition_all_success = 0
    total_decomposition_last_fail_only = 0
    total_decomposition_all_fail = 0
    other = 0
    for class_ in test_exec_details:
        for method_ in test_exec_details[class_]:
            for test_path in test_exec_details[class_][method_]:
                for test_class in test_exec_details[class_][method_][test_path]:
                    for test_method in test_exec_details[class_][method_][test_path][test_class]:

                        total_tests += [x for x in test_exec_details[class_][method_][test_path][test_class][test_method]]

                        if len(test_exec_details[class_][method_][test_path][test_class][test_method]) == 1:
                            continue

                        total_tests_w_decomposition.append(test_method)

                        test_outcomes = []
                        for test_case in sorted(test_exec_details[class_][method_][test_path][test_class][test_method], key=lambda x: int(test_case.split('_')[-2][4:])):
                            test_outcomes.append(test_exec_details[class_][method_][test_path][test_class][test_method][test_case])
                        
                    
                        if test_outcomes.count('exercised-failed') == 1 and test_outcomes[-1] == 'exercised-failed':
                            pass_rate.append(test_outcomes.count('exercised-success')/len(test_outcomes))
                            total_decomposition_last_fail_only += 1
                        
                        elif test_outcomes.count('exercised-success') == len(test_outcomes):
                            total_decomposition_all_success += 1
                        
                        elif test_outcomes.count('exercised-failed') == len(test_outcomes):
                            total_decomposition_all_fail += 1

                        else:
                            other += 1


    print('project:', args.project_name)
    print('total tests:', len(total_tests))
    print('total tests with decomposition:', len(total_tests_w_decomposition))
    print('total unique tests with decomposition:', len(set(total_tests_w_decomposition)))
    print('total decomposition last fail only:', total_decomposition_last_fail_only, f'[test_pass_rate: {sum(pass_rate)/len(pass_rate) if pass_rate else 0}]')
    print('total decomposition all success:', total_decomposition_all_success)
    print('total decomposition all fail:', total_decomposition_all_fail)
    print('other:', other)
    print('---' * 10)

    with open(f'{args.project_name}.json', 'w') as f:
        json.dump({'pass_rate': pass_rate}, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--project_name', type=str, help='project name')
    parser.add_argument('--model_name', type=str, help='model name')
    parser.add_argument('--translation_dir', type=str, help='translation directory')
    args = parser.parse_args()
    main(args)
