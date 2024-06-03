from src.compositional_glue_tests.script import Project

project = None

def l2_validation(translated_member, args, schema_data, class_, fragment_):
    global project
    if not project:
        project = Project(args.project_name)
    
    schema_file_name = schema_data['path'].split('/')[-1]
    schema_name = schema_data['path'].split('/')[-1].split('.')[-2]
    
    project.inject_translated_method(translated_member, schema_file_name, class_, fragment_)
    
    fragment_name = fragment_.split(':')[-1]
    
    # check whether the fragment is a constructor
    if fragment_name == class_:
        fragment_name = '__init__'
    
    test = project.derive_compositional_tests({
        schema_name: {
            class_: [fragment_name]
        }
    })
    
    status, feedback = test.run()
    
    return status, translated_member, feedback
