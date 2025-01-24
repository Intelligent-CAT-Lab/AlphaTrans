import os
import json
import argparse


def calc_m1(graal_errors, test_pass):
    all_test_pass = 0
    some_test_pass = 0
    test_pass_fragments = [x[0] for x in test_pass]

    processed = []

    for test in graal_errors:
        if test in test_pass_fragments and test not in processed:
            index = test_pass_fragments.index(test)
            if test_pass[index][1] == 'all':
                all_test_pass += 1
            else:
                some_test_pass += 1
            
            processed.append(test)
    
    return all_test_pass, some_test_pass


def main(args):

    schema_path = f'{args.results_dir}/{args.model}/body/{args.temperature}/{args.project_name}'

    field_count = {'main': {'pending': 0, 'out_of_context': 0, 'attempted': 0}, 'test': {'pending': 0, 'out_of_context': 0, 'attempted': 0}}
    field_syntactic_count = {'main': {'pending': 0, 'parseable': 0, 'non-parseable': 0}, 'test': {'pending': 0, 'parseable': 0, 'non-parseable': 0}}
    field_exercise_count = {'main': {'pending': 0, 'success': 0, 'failed': 0}, 'test': {'pending': 0, 'success': 0, 'failed': 0}}
    main_method_count = {'pending': 0, 'out_of_context': 0, 'attempted': 0}
    main_method_syntactic_count = {'pending': 0, 'parseable': 0, 'non-parseable': 0}
    main_method_test_exec_count = {'pending': 0, 'exercised': {'total-tests': 0, 'exercised-success': 0, 'exercised-failed': {'total': 0, 'assertion': 0, 'other': 0}}, 'not-exercised': 0}
    unique_exercised_tests_pass = set()
    unique_exericsed_tests_assertion = set()
    unique_exericsed_tests_other = set()
    unique_exericsed_tests_failed = set()
    graal_errors = set()
    test_outcome_details = {}
    main_method_graal_count = {'pending': 0, 'not-exercised': 0, 'success': 0, 'error': 0, 'failed': 0, 'failure': 0}
    test_method_count = {'pending': 0, 'out_of_context': 0, 'attempted': 0}
    test_method_syntactic_count = {'pending': 0, 'parseable': 0, 'non-parseable': 0}

    total = 0
    total_fields = 0
    total_main_methods = 0
    total_test_methods = 0

    for schema_file in os.listdir(schema_path):

        if not schema_file.endswith('_python_partial.json'):
            continue

        if 'ESTest' in schema_file:
            continue

        data = {}
        with open(f'{schema_path}/{schema_file}', 'r') as f:
            data = json.load(f)
        
        for class_ in data['classes']:

            if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                continue

            for field_ in data['classes'][class_]['fields']:
                total += 1
                total_fields += 1

                if 'src.test' in schema_file:
                    field_count['test'][data['classes'][class_]['fields'][field_]['translation_status']] += 1
                    field_syntactic_count['test'][data['classes'][class_]['fields'][field_]['syntactic_validation']] += 1
                    field_exercise_count['test'][data['classes'][class_]['fields'][field_]['field_exercise']] += 1
                else:
                    field_count['main'][data['classes'][class_]['fields'][field_]['translation_status']] += 1
                    field_syntactic_count['main'][data['classes'][class_]['fields'][field_]['syntactic_validation']] += 1                    
                    field_exercise_count['main'][data['classes'][class_]['fields'][field_]['field_exercise']] += 1

            test_exec_details = {}
            for method_ in data['classes'][class_]['methods']:

                if data['classes'][class_]['methods'][method_]['is_overload']:
                    continue

                total += 1

                if 'src.test' in schema_file:
                    total_test_methods += 1
                    test_method_count[data['classes'][class_]['methods'][method_]['translation_status']] += 1
                    test_method_syntactic_count[data['classes'][class_]['methods'][method_]['syntactic_validation']] += 1

                else:

                    total_main_methods += 1
                    main_method_count[data['classes'][class_]['methods'][method_]['translation_status']] += 1
                    main_method_syntactic_count[data['classes'][class_]['methods'][method_]['syntactic_validation']] += 1

                    if isinstance(data['classes'][class_]['methods'][method_]['graal_validation'], dict):
                        if 'outcome' in data['classes'][class_]['methods'][method_]['graal_validation']:
                            main_method_graal_count[data['classes'][class_]['methods'][method_]['graal_validation']['outcome']] += 1

                            if data['classes'][class_]['methods'][method_]['graal_validation']['outcome'] == 'error':
                                graal_errors.add(f'{class_}|{method_}')
                            
                            continue
                        if 'graal_outcome' in data['classes'][class_]['methods'][method_]['graal_validation']:
                            main_method_graal_count[data['classes'][class_]['methods'][method_]['graal_validation']['graal_outcome']] += 1
                            
                            if data['classes'][class_]['methods'][method_]['graal_validation']['graal_outcome'] == 'error':
                                graal_errors.add(f'{class_}|{method_}')
                            
                            continue

                        main_method_graal_count[data['classes'][class_]['methods'][method_]['graal_validation']] += 1
                        if data['classes'][class_]['methods'][method_]['graal_validation'] == 'error':
                            graal_errors.add(f'{class_}|{method_}')
                    else:
                        main_method_graal_count[data['classes'][class_]['methods'][method_]['graal_validation']] += 1

                        if data['classes'][class_]['methods'][method_]['graal_validation'] == 'error':
                            graal_errors.add(f'{class_}|{method_}')


                    if isinstance(data['classes'][class_]['methods'][method_]['test_execution'], dict):

                        for test_case in data['classes'][class_]['methods'][method_]['test_execution']:
                            test_case_name = '::'.join(test_case.split('::')[1:])
                            test_outcomes = data['classes'][class_]['methods'][method_]['test_execution'][test_case]

                            test_outcome_details.setdefault(f'{class_}#{method_}', {})
                            test_outcome_details[f'{class_}#{method_}'][test_case_name] = {'test_outcome': test_outcomes['test_outcome'], 'feedback': test_outcomes['feedback']}

                            unique_test_name = ''
                            if '_decomposed' in test_case_name:
                                unique_test_name = '_'.join(test_case_name.split('_')[:-2])
                            else:
                                unique_test_name = test_case_name
                                                            
                            if test_outcomes['test_outcome'] == 'exercised-success':
                                main_method_test_exec_count['exercised']['total-tests'] += 1
                                main_method_test_exec_count['exercised']['exercised-success'] += 1
                                unique_exercised_tests_pass.add(test_case_name)
                            else:
                                main_method_test_exec_count['exercised']['total-tests'] += 1
                                main_method_test_exec_count['exercised']['exercised-failed']['total'] += 1
                                unique_exericsed_tests_failed.add(test_case_name)
                                
                                if 'AssertionError' in test_outcomes['feedback']:
                                    main_method_test_exec_count['exercised']['exercised-failed']['assertion'] += 1
                                    unique_exericsed_tests_assertion.add(test_case_name)
                                else:
                                    main_method_test_exec_count['exercised']['exercised-failed']['other'] += 1
                                    unique_exericsed_tests_other.add(test_case_name)

                    else:
                        main_method_test_exec_count[data['classes'][class_]['methods'][method_]['test_execution']] += 1
            
            if 'static_initializers' in data['classes'][class_]:
                for static_init in data['classes'][class_]['static_initializers']:
                    total += 1
                    total_fields += 1
                    field_count['main'][data['classes'][class_]['static_initializers'][static_init]['translation_status']] += 1
                    field_syntactic_count['main'][data['classes'][class_]['static_initializers'][static_init]['syntactic_validation']] += 1                        
                    field_exercise_count['main'][data['classes'][class_]['static_initializers'][static_init]['field_exercise']] += 1
                    
    print('#' * 50)
    print(f"Total: {total} (fields: {total_fields}, main methods: {total_main_methods}, test methods: {total_test_methods})")
    print('-' * 50)
    print('### Fields MAIN ###')
    print('field_count MAIN:', field_count['main'])
    print('field_syntactic_validation MAIN:', field_syntactic_count['main'])
    print('field_exercise_count MAIN:', field_exercise_count['main'])
    print('-' * 50)
    print('### Fields TEST ###')
    print('field_count TEST:', field_count['test'])
    print('field_syntactic_validation TEST:', field_syntactic_count['test'])
    print('field_exercise_count TEST:', field_exercise_count['test'])
    print('-' * 50)
    print('### Main Methods ###')
    print('main_method_count:', main_method_count)
    print('main_method_syntactic_count:', main_method_syntactic_count)
    print('main_method_graal_count:', main_method_graal_count)
    print('main_method_test_exec_count:', main_method_test_exec_count)

    all_test_pass, one_test_fail_other, one_test_fail_assertion, many_test_fail_other, many_test_fail_assertion, all_test_fail_other, all_test_fail_assertion = 0, 0, 0, 0, 0, 0, 0
    total_one_test_fail, total_many_test_fail, total_all_test_fail = 0, 0, 0
    
    some_test_pass = []
    for k in test_outcome_details:
        details = {'assertion_error': 0, 'other': 0}
        
        total_tests = len(test_outcome_details[k])
        for test_case in test_outcome_details[k]:
            if test_outcome_details[k][test_case]['test_outcome'] != 'exercised-success':
                if 'AssertionError' in test_outcome_details[k][test_case]['feedback']:
                    details['assertion_error'] += 1
                else:
                    details['other'] += 1

        if sum(details.values()) == 0:
            all_test_pass += 1
            some_test_pass.append(('|'.join(k.split('#')), 'all'))

        elif sum(details.values()) == 1:
            total_one_test_fail += 1
            one_test_fail_assertion += details['assertion_error']
            one_test_fail_other += details['other']

            if total_tests > 1:
                some_test_pass.append(('|'.join(k.split('#')), 'some-one'))

        elif sum(details.values()) > 1 and sum(details.values()) < total_tests:
            total_many_test_fail += 1
            many_test_fail_assertion += details['assertion_error']
            many_test_fail_other += details['other']

            if total_tests > 1:
                some_test_pass.append(('|'.join(k.split('#')), 'some-many'))

        else:
            total_all_test_fail += 1
            all_test_fail_assertion += details['assertion_error']
            all_test_fail_other += details['other']
            some_test_pass.append(('|'.join(k.split('#')), 'some-all'))
    
    print('-' * 50)
    print('### Main Methods Test Translation Results ###')
    print('fragments ATP:', all_test_pass)
    print()
    print('fragments OTF:', total_one_test_fail, f'[assertion error: {one_test_fail_assertion}, other error: {one_test_fail_other}]')
    print()
    print('fragments MTF:', total_many_test_fail, f'[assertion error: {many_test_fail_assertion}, other error: {many_test_fail_other}]')
    print()
    print('fragments ATF:', total_all_test_fail, f'[assertion error: {all_test_fail_assertion}, other error: {all_test_fail_other}]')
    print()
    print('unique tests PASS:', len(unique_exercised_tests_pass))
    print('unique tests FAIL:', len(unique_exericsed_tests_failed), f'[assertion error: {len(unique_exericsed_tests_assertion)}, other error: {len(unique_exericsed_tests_other)}]')
    print('-' * 50)
    print('### M1 ###')
    all_, some_ = calc_m1(graal_errors, some_test_pass)
    print('M1 All:', all_)
    print('M1 Some:', some_)
    print('-' * 50)
    print('### Test Methods ###')
    print('test_method_count:', test_method_count)
    print('test_method_syntactic_count:', test_method_syntactic_count)
    print('-' * 50)
    print('total progress:', round(((field_count['main']['attempted'] + field_count['test']['attempted'] + main_method_count['attempted'] + test_method_count['attempted']) / total) * 100, 2))
    print('#' * 50)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print results')
    parser.add_argument('--results_dir', type=str, help='Results directory')
    parser.add_argument('--project_name', type=str, help='Project name')
    parser.add_argument('--temperature', type=str, help='Temperature')
    parser.add_argument('--model', type=str, help='Model')
    args = parser.parse_args()
    main(args)
