import argparse
import json
from collections import defaultdict
from src.compositional_glue_tests.script import Project


def analyse(project_name: str, model_name: str, prompt_type: str):
    # directory containing the schema files
    schema_dir = f'data/schemas/translations/{model_name}/{prompt_type}'
    
    project = Project(project_name, schema_dir)
    
    results = dict() # { (test_class, test_method): status }
    
    # loop over all tests
    for test_schema, test_class, test_method in project.test_dependencies:
        test_method_name = test_method.split(':')[-1]
        
        components = defaultdict(lambda: defaultdict(list)) # components to be "glued" for the test
        injected_translations = dict() # translations to be injected
        
        for _schema, class_name, _method in project.test_dependencies[(test_schema, test_class, test_method)]:  
            full_schema_name = _schema + '_python_partial'
            method_name = _method.split(':')[-1]

            # ignore test classes
            if 'src.test.' in _schema: continue 
            
            # ignore non-test methods
            if not _method.startswith('test'): continue
            
            # get the translation
            with open(f'{project.schema_dir}/{project.name}/{full_schema_name}.json') as f:
                translation = "\n".join(json.load(f)['classes'][class_name]['methods'][_method]['translation'])
            
            injected_translations[(full_schema_name, class_name, _method)] = translation
            
            # check whether the method is a constructor
            if method_name == class_name:
                method_name = '__init__'
            
            components[full_schema_name][class_name].append(method_name)
        
        project.recompose_python_project(injected_translations)
        test = project.derive_compositional_tests(components, debug=True)
        
        if test is None:
            results[(test_class, test_method_name)] = 'error'
        else:    
            output = test.run({test_class: [test_method_name]})
            results[(test_class, test_method_name)] = output['status']
        
        print(f"{test_class}#{test_method_name}: {results[(test_class, test_method_name)]}")

        # write the results
        with open(f'{project.root_dir}/per_test_results.{project.name}.txt', 'a') as f:
            f.write(f"{test_class}#{test_method_name}: {results[(test_class, test_method_name)]}" + "\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run per-test analysis')
    parser.add_argument('--project_name', type=str, help='Name of the project')
    parser.add_argument('--model_name', type=str, help='Name of the model', default='deepseek-coder-33b-instruct')
    parser.add_argument('--prompt_type', type=str, help='Type of prompt', default='body')
    args = parser.parse_args()
    
    analyse(args.project_name, args.model_name, args.prompt_type)
