import argparse
import json
import os
from src.compositional_glue_tests.script_for_class_by_class import Project, ERROR

SCHEMA_PATH = "data/schemas_decomposed_tests/translations/deepseek-coder-33b-instruct/body/0.0"
PROMPT_TYPE = "body"


def main(args):
    schemas = os.listdir(f'{SCHEMA_PATH}/{args.project_name}/')

    for schema in schemas:
        path_ = f'{SCHEMA_PATH}/{args.project_name}/{schema}'
        with open(path_, 'r') as f:
            data = json.load(f)

        project_name = args.project_name
        project = Project(project_name, SCHEMA_PATH, model_name=args.model_name)
        
        schema_name = schema.replace('.json', '')
        full_schema_name = schema_name
        components = dict()
        injected_translations = dict()
        
        components[full_schema_name] = {}
        
        for class_ in data['classes']:
            for method in data['classes'][class_]['methods']:
                    injected_translations[(full_schema_name, class_, method)] = ''
            components[full_schema_name][class_] = []

        try:
            project.recompose_python_project(injected_translations)
        except Exception as e:
            print(f"Error recomposing project: {e}")
            continue
        
        try:
            test = project.derive_compositional_tests(components, debug=True)
            output = test.run()
        except NotImplementedError as e:
            output = {
                "status": ERROR,
                "feedback": dict(),
                "message": "Unsupported fragment: " + str(e)
            }

        status = output['status']
        
        print(f"Schema '{schema_name}' returned with status '{status}'")

        # write the results to a file
        with open(f'{project_name}_results.jsonl', 'a') as f:
            f.write(json.dumps({
                "schema": schema_name,
                "status": status,
            }) + '\n')


if __name__ == '__main__':
    parser_ = argparse.ArgumentParser(description='Translate java types to python types (Class-by-class variant)')
    parser_.add_argument('--project_name', type=str, dest='project_name', help='project name to translate', required=True)
    parser_.add_argument('--model_name', type=str, dest='model_name', help='model name to use for translation', required=True)
    args = parser_.parse_args()
    
    # reset the stats file
    with open(f'{args.project_name}_results.jsonl', 'w') as f:
        f.write("")
    
    main(args)
    
    # read the stats file and print the number of "success", "failure", "error", "not-exercised" 
    with open(f"{args.project_name}_results.jsonl") as f:
        data = [json.loads(line) for line in f.readlines()]
    statuses = [item['status'] for item in data]
    print(f"#GS: {statuses.count('success')}")
