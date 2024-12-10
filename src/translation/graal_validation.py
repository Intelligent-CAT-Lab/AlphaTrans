import json
import typing
from src.compositional_glue_tests.script import Project, ERROR

project = None


def graal_validation(generation: typing.List[str], fragment: typing.Dict[str, str], args) -> typing.Tuple[str, typing.Dict[str, str], str]:
    """
    generation: List of strings. Each string is a line of code of the translation.
    fragment: Dictionary containing information about the fragment. (TODO: add more details)
    
    returns (status, feedback) where
        status: success, failure, error
        feedback: Dict[str, str]. example: {'test_1': 'failing message', 'test_2': 'failing message', ...}
        message: str. A message for the user.
    """
    global project
    project_name = args.project_name

    schema_dir = '/'.join(args.translation_dir.split('/')[:-1])

    if not project:
        project = Project(project_name, schema_dir)
        
    components = dict()
    injected_translations = dict()

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

    try:
        test = project.derive_compositional_tests(components, debug=True)
        output = test.run()
        assert isinstance(output, dict)
    except NotImplementedError as e:
        output = {
            "status": ERROR,
            "feedback": dict(),
            "message": "Unsupported fragment: " + str(e)
        }
    except AssertionError:
        output = {
            "status": ERROR,
            "feedback": dict(),
            "message": ""
        }

    status = output['status']
    feedback = output['feedback']
    is_dct = False
    graal_feedback = ''
    if isinstance(feedback, dict):
        is_dct = True
        for test_id in feedback:
            graal_feedback += f'{test_id}: {feedback[test_id]}\n'
    if is_dct:
        feedback = graal_feedback        
    message = output['message']

    return status, feedback, message
