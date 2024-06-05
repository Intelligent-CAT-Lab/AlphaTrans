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
    project_name = members_to_validate[0][4]
    
    if not project:
        project = Project(project_name)
        
    components = dict()
    
    for member in members_to_validate:
        translation, schema, class_, fragment, args = member
        
        with open(f"{project.schema_dir}/{project_name}/{schema}", "r") as f:
            schema_data = json.load(f)
            
        schema_file_name = schema_data['path'].split('/')[-1]
        schema_name = schema_data['path'].split('/')[-1].split('.')[-2]
        
        project.inject_translated_method(translation, schema_file_name, class_, fragment)
        
        fragment_name = fragment.split(':')[-1]
    
        # check whether the fragment is a constructor
        if fragment_name == class_:
            fragment_name = '__init__'
        
        if schema_name in components:
            if class_ in components[schema_name]:
                components[schema_name][class_].append(fragment_name)
            else:
                components[schema_name][class_] = [fragment_name]
        else:
            components[schema_name] = {class_: [fragment_name]}
            
    test = project.derive_compositional_tests(components)
    status, feedback = test.run()
    
    return status, members_to_validate, feedback
