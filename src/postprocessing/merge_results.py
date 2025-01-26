import os
import json
import argparse


def main(args):

    os.makedirs(f'data/results/{args.first_model}_{args.second_model}_MERGED/body/{args.temperature}', exist_ok=True)

    first_model_prefix = f'data/results/{args.first_model}/body/{args.temperature}'
    second_model_prefix = f'data/results/{args.second_model}/body/{args.temperature}'

    for project in ['commons-cli', 'commons-codec', 'commons-csv', 'commons-validator', 'commons-fileupload', 'commons-pool', 'commons-graph', 'commons-exec', 'jansi', 'JavaFastPFOR']:
        os.makedirs(f'data/results/{args.first_model}_{args.second_model}_MERGED/body/{args.temperature}/{project}', exist_ok=True)

        first_schemas_path = f'{first_model_prefix}/{project}/'
        second_schemas_path = f'{second_model_prefix}/{project}/'

        for first_schema_file in os.listdir(first_schemas_path):

            if not first_schema_file.endswith('_python_partial.json'):
                continue

            if 'ESTest' in first_schema_file:
                continue

            merged_schema = {}
            with open(f'{first_schemas_path}/{first_schema_file}', 'r') as f:
                merged_schema = json.load(f)
            
            second_schema = {}
            with open(f'{second_schemas_path}/{first_schema_file}', 'r') as f:
                second_schema = json.load(f)
            
            for class_ in second_schema['classes']:

                if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                    continue

                for field_ in second_schema['classes'][class_]['fields']:
                    if merged_schema['classes'][class_]['fields'][field_]['translation_status'] != 'attempted' and second_schema['classes'][class_]['fields'][field_]['translation_status'] == 'attempted':
                        merged_schema['classes'][class_]['fields'][field_] = second_schema['classes'][class_]['fields'][field_]
                    elif merged_schema['classes'][class_]['fields'][field_]['translation_status'] == 'attempted' and merged_schema['classes'][class_]['fields'][field_]['syntactic_validation'] != 'parseable' and second_schema['classes'][class_]['fields'][field_]['syntactic_validation'] == 'parseable':
                        merged_schema['classes'][class_]['fields'][field_] = second_schema['classes'][class_]['fields'][field_]
                    elif merged_schema['classes'][class_]['fields'][field_]['translation_status'] == 'attempted' and merged_schema['classes'][class_]['fields'][field_]['field_exercise'] != 'success' and second_schema['classes'][class_]['fields'][field_]['field_exercise'] == 'success':
                        merged_schema['classes'][class_]['fields'][field_] = second_schema['classes'][class_]['fields'][field_]

                for method_ in second_schema['classes'][class_]['methods']:
                    merged_graal_outcome = ''
                    if isinstance(merged_schema['classes'][class_]['methods'][method_]['graal_validation'], dict):
                        if 'outcome' in merged_schema['classes'][class_]['methods'][method_]['graal_validation']:
                            merged_graal_outcome = merged_schema['classes'][class_]['methods'][method_]['graal_validation']['outcome']
                            
                        if 'graal_outcome' in merged_schema['classes'][class_]['methods'][method_]['graal_validation']:
                            merged_graal_outcome = merged_schema['classes'][class_]['methods'][method_]['graal_validation']['graal_outcome']
                    else:
                        merged_graal_outcome = merged_schema['classes'][class_]['methods'][method_]['graal_validation']
                    
                    assert merged_graal_outcome != ''
                    
                    second_graal_outcome = ''
                    if isinstance(second_schema['classes'][class_]['methods'][method_]['graal_validation'], dict):
                        if 'outcome' in second_schema['classes'][class_]['methods'][method_]['graal_validation']:
                            second_graal_outcome = second_schema['classes'][class_]['methods'][method_]['graal_validation']['outcome']
                            
                        if 'graal_outcome' in second_schema['classes'][class_]['methods'][method_]['graal_validation']:
                            second_graal_outcome = second_schema['classes'][class_]['methods'][method_]['graal_validation']['graal_outcome']
                    else:
                        second_graal_outcome = second_schema['classes'][class_]['methods'][method_]['graal_validation']
                    
                    assert second_graal_outcome != ''

                    if merged_schema['classes'][class_]['methods'][method_]['translation_status'] != 'attempted' and second_schema['classes'][class_]['methods'][method_]['translation_status'] == 'attempted':
                        merged_schema['classes'][class_]['methods'][method_] = second_schema['classes'][class_]['methods'][method_]
                    elif merged_schema['classes'][class_]['methods'][method_]['translation_status'] == 'attempted' and merged_schema['classes'][class_]['methods'][method_]['syntactic_validation'] != 'parseable' and second_schema['classes'][class_]['methods'][method_]['syntactic_validation'] == 'parseable':
                        merged_schema['classes'][class_]['methods'][method_] = second_schema['classes'][class_]['methods'][method_]
                    elif merged_schema['classes'][class_]['methods'][method_]['translation_status'] == 'attempted' and merged_graal_outcome != 'success' and second_graal_outcome == 'success':
                        merged_schema['classes'][class_]['methods'][method_] = second_schema['classes'][class_]['methods'][method_]
                    elif merged_schema['classes'][class_]['methods'][method_]['translation_status'] == 'attempted' and merged_schema['classes'][class_]['methods'][method_]['test_execution'] != 'exercised' and second_schema['classes'][class_]['methods'][method_]['test_execution'] == 'exercised':
                        merged_schema['classes'][class_]['methods'][method_] = second_schema['classes'][class_]['methods'][method_]
                
                if 'static_initializers' in second_schema['classes'][class_]:
                    for static_init in second_schema['classes'][class_]['static_initializers']:
                        if merged_schema['classes'][class_]['static_initializers'][static_init]['translation_status'] != 'attempted' and second_schema['classes'][class_]['static_initializers'][static_init]['translation_status'] == 'attempted':
                            merged_schema['classes'][class_]['static_initializers'][static_init] = second_schema['classes'][class_]['static_initializers'][static_init]
                        elif merged_schema['classes'][class_]['static_initializers'][static_init]['translation_status'] == 'attempted' and merged_schema['classes'][class_]['static_initializers'][static_init]['syntactic_validation'] != 'parseable' and second_schema['classes'][class_]['static_initializers'][static_init]['syntactic_validation'] == 'parseable':
                            merged_schema['classes'][class_]['static_initializers'][static_init] = second_schema['classes'][class_]['static_initializers'][static_init]
                        elif merged_schema['classes'][class_]['static_initializers'][static_init]['translation_status'] == 'attempted' and merged_schema['classes'][class_]['static_initializers'][static_init]['field_exercise'] != 'success' and second_schema['classes'][class_]['static_initializers'][static_init]['field_exercise'] == 'success':
                            merged_schema['classes'][class_]['static_initializers'][static_init] = second_schema['classes'][class_]['static_initializers'][static_init]
            
            with open(f'data/results/{args.first_model}_{args.second_model}_MERGED/body/{args.temperature}/{project}/{first_schema_file}', 'w') as f:
                json.dump(merged_schema, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merge results')
    parser.add_argument('--temperature', type=str, help='Temperature')
    parser.add_argument('--first_model', type=str, help='First Model')
    parser.add_argument('--second_model', type=str, help='Second Model')

    args = parser.parse_args()
    main(args)
