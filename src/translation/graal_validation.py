import json
import typing
from src.compositional_glue_tests.script import Project

project = None

def graal_validation(generation: typing.List[str], fragment: typing.Dict[str, str], args) -> typing.Tuple[str, typing.Dict[str, str]]:
    global project

    project_name = args.project_name

    schema_dir = f'data/schemas/translations/{args.model_name}/{args.prompt_type}'
    
    if not project:
        project = Project(project_name, schema_dir)
        
    components = dict()
    injected_translations = dict()
        
    with open(f"{project.schema_dir}/{project_name}/{fragment['schema_name']}_python_partial.json", "r") as f:
        schema_data = json.load(f)

    full_schema_name = fragment['schema_name'] + '_python_partial'
    
    injected_translations[(full_schema_name, fragment['class_name'], fragment['fragment_name'])] = '\n'.join(generation)
    
    fragment_name = fragment['fragment_name'].split(':')[-1]

    # check whether the fragment is a constructor
    if fragment_name == fragment['class_name']:
        fragment_name = '__init__'
    
    if full_schema_name in components:
        if fragment['class_name'] in components[full_schema_name]:
            components[full_schema_name][fragment['class_name']].append(fragment_name)
        else:
            components[full_schema_name][fragment['class_name']] = [fragment_name]
    else:
        components[full_schema_name] = {fragment['class_name']: [fragment_name]}
            
    print("Deriving compositional tests for the following components:", components)

    project.recompose_python_project(injected_translations)

    test = project.derive_compositional_tests(components, debug=True)
    if test is None:
        return "error", {}

    output = test.run()
    status = output['status']
    feedback = output['failed_tests']

    """
    status: success, failure, error
    feedback: Dict[str, str]. example: {'test_1': 'failing message', 'test_2': 'failing message', ...}
    """

    return status, feedback
