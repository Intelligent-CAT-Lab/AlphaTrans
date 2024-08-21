import argparse
import json
import tqdm
import os
import time
from src.compositional_glue_tests.utils import topological_sort
from syntactic_validation import l0_validation
from src.translation.graal_validation import graal_validation

# subprocess.run(['git', 'checkout', 'data/schemas/'])
i = 0

def translate(model, tokenizer, device, members_to_translate: list[list], dump_syntactically_validated_fragments, is_test):
    """
    members_to_translate: [prompt, fragment, use_bam, project_name, schema, class_, fragment_]
    """
    global i, RECORD_ALL, args
    i += 1
    # if i > 2:
    #     quit()
    syntactically_validated_members = []    
    for member in members_to_translate:
        prompt = member['prompt']
        fragment = member['fragment_type']
        use_bam = member['use_bam']
        project_name = member['project_name']
        schema = member['schema']
        class_ = member['class']
        fragment_ = member['fragment']
    
        max_attempts = 0
        parsed_fragment = None
        feedback = ''
        start_time = time.time()
        while max_attempts < 1:

            print(prompt, flush=True)
            print('=======================GENERATING=======================', flush=True)
            
            # open the schema file
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{schema}', 'r') as f:
                data = json.load(f)
                
            # get the precomputed translation
            translation = data['classes'][class_][f'{fragment}s'][fragment_]['translation']
            if type(translation) is str:
                generation = translation
            else:
                generation = "\n".join(translation)
                
            loc = len(generation.split('\n'))
            
            print(generation, flush=True)
            print('---' * 50, flush=True)

            status, parsed_fragment, feedback = l0_validation(generation)

            if not status:
                max_attempts += 1
                ### TODO: create new prompt with feedback
                # prompt = ...
                continue
            
            syntactically_validated_members.append([parsed_fragment, schema, class_, fragment_, args])
            
            max_attempts = 5
    
    # if syntactically_validated_members == []:
    #     elapsed_time = time.time() - start_time
    #     return None, elapsed_time

    if members_to_translate[0]['fragment_type'] == 'field':
        elapsed_time = time.time() - start_time
        return syntactically_validated_members, elapsed_time

    # if dump_syntactically_validated_fragments:
    #     elapsed_time = time.time() - start_time
    #     return syntactically_validated_members, elapsed_time
    
    if is_test:
        elapsed_time = time.time() - start_time
        return syntactically_validated_members, elapsed_time

    fragment_obj = {
        "fragment_type": fragment,
        "schema_name": schema.replace('_python_partial.json', '').replace('.json', ''),
        "fragment_name": fragment_,
        "class_name": class_,
    }
    status, feedback = graal_validation(generation.split('\n'), fragment_obj, args)
    functionally_validated_members = syntactically_validated_members if status == 'success' else None
    
    if status == 'success':
        print("\033[92mPASSED!\033[0m")
    else:
        print("\033[93m" + status.upper() + "\033[0m")
        if not RECORD_ALL:
            if input("Do you want to interrupt? (no=Enter)"):
                quit()
                
    # record
    if RECORD_ALL:
        with open(f'{project_name}_stats.csv', 'a') as f:
            f.write(f"{schema}, {class_}, {fragment_}, {status}, {loc}\n")
        
    if not status:
        # TODO: handle feedback
        # print(feedback, flush=True)
        return None, 0

    elapsed_time = time.time() - start_time
    return functionally_validated_members, elapsed_time


def align_schema_order(schemas, traversal_order):
    aligned_schemas = []
    for fname in traversal_order:
        found_schema = []
        for schema in schemas:
            if f'.{fname}_python_partial.json' in schema:
                found_schema.append(schema)
        
        # assert len(found_schema) == 1, f"Found more than one schema for {fname}: {found_schema}"
        aligned_schemas += found_schema
    
    schemas = [fname for fname in schemas if fname.endswith('_python_partial.json')]
    # assert len(aligned_schemas) == len(schemas), f"Found less schemas than expected: {aligned_schemas}"

    return aligned_schemas


def main(args):
    global SCHEMA_BREAK, SCHEMA_BREAK_PASSED, CLASS_BREAK, CLASS_BREAK_PASSED, METHOD_BREAK, METHOD_BREAK_PASSED, RECORD_ALL
    device = 'cpu' # 'cuda' if torch.cuda.is_available() and args.use_cuda else 'cpu''
    tokenizer, model = None, None

    schemas = os.listdir(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}')

    traversal = {}
    with open(f'data/dependencies/{args.project_name}/traversal.json', 'r') as f:
        traversal = json.load(f)
    
    traversal_order = list(traversal.values())

    schemas = align_schema_order(schemas, traversal_order)

    for schema in schemas:
        if SCHEMA_BREAK and SCHEMA_BREAK not in schema and not SCHEMA_BREAK_PASSED:
            continue
        SCHEMA_BREAK_PASSED = True

        path_ = f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{schema}'
        with open(path_, 'r') as f:
            data = json.load(f)
      
        dependency_graph = set() # set of (dependent, dependency) pairs
        
        for class_ in data['classes']:
            if data['classes'][class_]['extends']:
                if data['classes'][class_]['extends'][0] in data['classes']:
                    dependency_graph.add((class_, data['classes'][class_]['extends'][0]))
                
            if data['classes'][class_]['implements']:
                for interface in data['classes'][class_]['implements']:
                    if interface in data['classes']:
                        dependency_graph.add((class_, interface))
            
            if data['classes'][class_]['nested_inside']:
                dependency_graph.add((class_, data['classes'][class_]['nested_inside']))
                
        class_order = topological_sort(dependency_graph)[::-1]
        
        # check for any classes that were not included in the dependency graph
        class_order += [clz for clz in data['classes'] if clz not in class_order]
        
        for class_ in class_order:
            if CLASS_BREAK and CLASS_BREAK != class_ and not CLASS_BREAK_PASSED:
                continue
            CLASS_BREAK_PASSED = True

            if 'new' in class_ or '{' in class_: # skip nested and shameless classes
                continue

            print(f'Translating class {class_} @ schema {schema}...', flush=True)

            pbar = tqdm.tqdm(data['classes'][class_]['methods'])
            for method_ in pbar:
                if METHOD_BREAK and not method_.endswith(METHOD_BREAK) and not METHOD_BREAK_PASSED:
                    continue
                METHOD_BREAK_PASSED = True
                
                pbar.update()
                pbar.set_description(f"Translating method {method_} in class {class_} @ schema {schema}...")

                prompt = "<prompt>"

                translate(model, tokenizer, device, [{'prompt': prompt, 'fragment_type': 'method', 'use_bam': args.use_bam, 'project_name': args.project_name, 'schema': schema, 'class': class_, 'fragment': method_}], args.dump_syntactically_validated_fragments, 'src.main' not in schema)


if __name__ == '__main__':
    # load_dotenv()
    parser_ = argparse.ArgumentParser(description='Translate java types to python types')
    parser_.add_argument('--project_name', type=str, dest='project_name', help='project name to translate')
    
    parser_.add_argument('--schema', type=str, dest='schema', default=None, required=False)
    parser_.add_argument('--class', type=str, dest='class_', default=None, required=False)
    parser_.add_argument('--method', type=str, dest='method', default=None, required=False)
    parser_.add_argument('--record', action='store_true', help='record all')
    
    args = parser_.parse_args()
    
    args.model_name = None
    args.from_lang = 'java'
    args.to_lang = 'python'
    args.cache_dir = 'cache'
    args.use_bam = False
    args.use_cuda = False
    args.include_call_graph = True
    args.dump_syntactically_validated_fragments = False
    args.model_name = "deepseek-coder-33b-instruct"
    args.prompt_type = "body"
    
    SCHEMA_BREAK = f'.{args.schema}_' if args.schema else None
    CLASS_BREAK = args.class_
    METHOD_BREAK = args.method
    
    SCHEMA_BREAK_PASSED, CLASS_BREAK_PASSED, METHOD_BREAK_PASSED = False, False, False
    
    RECORD_ALL = args.record
    
    # reset the stats file
    if RECORD_ALL:
        with open(f'{args.project_name}_stats.csv', 'w') as f:
            f.write("")
    
    main(args)
