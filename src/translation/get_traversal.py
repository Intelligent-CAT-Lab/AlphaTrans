import os
import json


def order_fragments(project_traversal):

    ordered_project_traversal = []
    for fragment in project_traversal.copy():
        if fragment['fragment_type'] in ['field', 'static_initializer']:
            ordered_project_traversal.append(fragment)
            project_traversal.remove(fragment)
            continue
    
    return ordered_project_traversal + project_traversal


def process_waiting_queue(waiting_queue, processed_fragments, project_traversal):

    threshold = 10
    while True:
        if len(waiting_queue) == 0:
            break

        if threshold == 0:
            break

        for waiting_fragment in list(waiting_queue.keys()):
            waiting_dependent_fragments = [x for x in waiting_queue[waiting_fragment][0]]
            if all([x in processed_fragments for x in waiting_dependent_fragments]):
                _, waiting_schema, waiting_class, waiting_method = waiting_queue[waiting_fragment]

                processed_fragments.append(waiting_fragment)
                del waiting_queue[waiting_fragment]
                project_traversal.append({'schema_name': waiting_schema, 'class_name': waiting_class, 'fragment_name': waiting_method, 'fragment_type': 'method'})
                threshold = 10
        
        threshold -= 1
    
    return waiting_queue, processed_fragments, project_traversal


def get_traversal(args):
    project_traversal = []

    schemas = os.listdir(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}')

    # extract all fields and static initializers
    waiting_queue = {}
    processed_fragments = []
    for schema in schemas:

        if '_python_partial.json' not in schema:
            continue

        schema_base_name = schema.replace('_python_partial.json', '')

        if args.translate_evosuite and 'ESTest' not in schema:
            continue

        if not args.translate_evosuite and 'ESTest' in schema:
            continue

        path_ = f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{schema}'
        with open(path_, 'r') as f:
            data = json.load(f)

        for class_ in data['classes']:

            if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                continue

            field_dependencies = {}
            for field in data['classes'][class_]['fields']:
                field_dependencies.setdefault(field, [])
                for field_ in data['classes'][class_]['fields']:
                    if field == field_:
                        continue
                    if '=' not in ''.join(data['classes'][class_]['fields'][field]['body']):
                        continue
                    if field_ in ''.join(''.join(data['classes'][class_]['fields'][field]['body']).split('=')[1:]).strip():
                        field_dependencies[field].append(field_)

            field_order = []
            while len(field_order) != len(data['classes'][class_]['fields']):
                for field in data['classes'][class_]['fields']:
                    if field in field_order:
                        continue
                    if all([x in field_order for x in field_dependencies[field]]):
                        field_order.append(field)

            for field_ in field_order:
                project_traversal.append({'schema_name': schema_base_name, 'class_name': class_, 'fragment_name': field_, 'fragment_type': 'field'})

            if 'static_initializers' in data['classes'][class_]:

                assert 1 == len(data['classes'][class_]['static_initializers']), f"Found more than one static initializer for class {class_} @ schema {schema_base_name}"
                
                for static_initializer in data['classes'][class_]['static_initializers']:
                    project_traversal.append({'schema_name': schema_base_name, 'class_name': class_, 'fragment_name': static_initializer, 'fragment_type': 'static_initializer'})
            
            for method_ in data['classes'][class_]['methods']:

                if data['classes'][class_]['methods'][method_]['is_overload']:
                    continue

                full_fragment_name = f'{schema_base_name}|{class_}|{method_}'
                dependent_fragments = [f'{x[0]}|{x[1]}|{x[2]}' for x in data['classes'][class_]['methods'][method_]['calls'] if ':' in x[2] and full_fragment_name != f'{x[0]}|{x[1]}|{x[2]}']

                if any([x not in processed_fragments for x in dependent_fragments]) and not args.translate_evosuite:
                    waiting_queue[full_fragment_name] = [dependent_fragments, schema_base_name, class_, method_]
                    continue

                processed_fragments.append(full_fragment_name)
                project_traversal.append({'schema_name': schema_base_name, 'class_name': class_, 'fragment_name': method_, 'fragment_type': 'method'})
                                
                # check if a waiting fragment is now ready to be processed
                for waiting_fragment in list(waiting_queue.keys()):
                    waiting_dependent_fragments = [x for x in waiting_queue[waiting_fragment][0]]
                    if all([x in processed_fragments for x in waiting_dependent_fragments]):
                        _, waiting_schema, waiting_class, waiting_method = waiting_queue[waiting_fragment]

                        processed_fragments.append(waiting_fragment)
                        del waiting_queue[waiting_fragment]

                        project_traversal.append({'schema_name': waiting_schema, 'class_name': waiting_class, 'fragment_name': waiting_method, 'fragment_type': 'method'})

    # further checking the waiting queue to see if any fragment can be processed
    waiting_queue, processed_fragments, project_traversal = process_waiting_queue(waiting_queue, processed_fragments, project_traversal)
    
    if len(waiting_queue) == 0:
        return order_fragments(project_traversal)

    # finding cycles
    cycles = []
    for k in waiting_queue:
        waiting_dependent_fragments, waiting_schema, waiting_class, waiting_method = waiting_queue[k]

        for df in waiting_dependent_fragments:
            if df not in waiting_queue:
                continue

            if k in waiting_queue[df][0] and df in waiting_queue[k][0] and [df, k] not in cycles:
                cycles.append([k, df])

    # translating elements of cycles one by one
    for cycle in cycles:
        for cycle_fragment in cycle:
            waiting_dependent_fragments, waiting_schema, waiting_class, waiting_method = waiting_queue[cycle_fragment]

            processed_fragments.append(cycle_fragment)
            del waiting_queue[cycle_fragment]

            project_traversal.append({'schema_name': waiting_schema, 'class_name': waiting_class, 'fragment_name': waiting_method, 'fragment_type': 'method'})

    # further checking the waiting queue to see if any fragment can be processed
    waiting_queue, processed_fragments, project_traversal = process_waiting_queue(waiting_queue, processed_fragments, project_traversal)

    assert len(waiting_queue) == 0, f"Found cycles in the waiting queue"

    return order_fragments(project_traversal)
