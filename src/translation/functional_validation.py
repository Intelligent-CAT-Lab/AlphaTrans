import json
from src.compositional_glue_tests.script import Project

project = None

def l2_validation(members_to_validate: list[list]):
    """
    [
        [translation, schema, class, fragment, args],
        ...
    ]
    """    
    global project
    args = members_to_validate[0][4]
    project_name = args.project_name

    schema_dir = f'data/schemas/translations/{args.model_name}/{args.prompt_type}'
    
    if not project:
        project = Project(project_name, schema_dir)
        
    components = dict()
    injected_translations = dict()
    
    for member in members_to_validate:
        translation, schema, class_, fragment, args = member
        
        with open(f"{project.schema_dir}/{project_name}/{schema}", "r") as f:
            schema_data = json.load(f)

        schema_name = schema_data['path'].split('/')[-1].split('.')[-2]
        full_schema_name = ".".join(schema.split('.')[:-1])
        
        injected_translations[(full_schema_name, class_, fragment)] = translation
        
        fragment_name = fragment.split(':')[-1]
    
        # check whether the fragment is a constructor
        if fragment_name == class_:
            fragment_name = '__init__'
        
        if full_schema_name in components:
            if class_ in components[full_schema_name]:
                components[full_schema_name][class_].append(fragment_name)
            else:
                components[full_schema_name][class_] = [fragment_name]
        else:
            components[full_schema_name] = {class_: [fragment_name]}
            
    print("Deriving compositional tests for the following components:", components)

    project.recompose_python_project(injected_translations)

    test = project.derive_compositional_tests(components, debug=True)
    if test is None:
        return "error", members_to_validate, []

    output = test.run()
    status = output['status']
    feedback = output['failed_tests']

    return status, members_to_validate, feedback
