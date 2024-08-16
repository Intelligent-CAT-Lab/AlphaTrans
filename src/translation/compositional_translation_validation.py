import argparse
import json
from dotenv import load_dotenv
import tqdm
import os
import time
import math
import datetime
from syntactic_validation import syntactic_validation
from field_exercise_validation import field_exercise_validation
from test_validation import test_validation
from graal_validation import graal_validation
from get_reverse_traversal import get_reverse_traversal
from prompt_generator import PromptGenerator

from genai.client import Client
from genai.credentials import Credentials
from genai.schema import (
    DecodingMethod,
    TextGenerationParameters,
    TextGenerationReturnOptions,
)


def get_eligible_tests(fragment, processed_fragments, args):

    global_call_graph = {}
    with open(f'data/call_graphs/{args.project_name}/call_graph.json', 'r') as f:
        global_call_graph = json.load(f)

    test_focal_method_map = {}
    for class_ in global_call_graph:
        for method_ in global_call_graph[class_]:
            if method_ == 'schema_file' or 'src/test' not in global_call_graph[class_]['schema_file']:
                continue

            test_method = f"{global_call_graph[class_]['schema_file']}|{class_}|{method_}"

            test_focal_method_map.setdefault(test_method, [])
            for focal_method in global_call_graph[class_][method_]:
                test_focal_method_map[test_method].append(f"{focal_method['schema']}|{focal_method['class']}|{focal_method['method']}")

    executable_tests = []
    for test in test_focal_method_map:

        if f"{fragment['schema_name']}|{fragment['class_name']}|{fragment['fragment_name']}" not in test_focal_method_map[test]:
            continue

        if all(focal_method in processed_fragments for focal_method in test_focal_method_map[test] if focal_method != f"{fragment['schema_name']}|{fragment['class_name']}|{fragment['fragment_name']}"):
            test_schema = '.'.join(test.split('|')[0].split('/')[2:]).replace('.java', '')
            test_schema_data = {}
            with open(f'{args.translation_dir}/{test_schema}_python_partial.json', 'r') as f:
                test_schema_data = json.load(f)
            
            if 'Test' not in [x.split('(')[0] for x in test_schema_data['classes'][test.split('|')[1]]['methods'][test.split('|')[2]]['annotations']]:
                continue

            if 'Ignore' in [x.split('(')[0] for x in test_schema_data['classes'][test.split('|')[1]]['methods'][test.split('|')[2]]['annotations']]:
                continue

            executable_tests.append({'schema_name': test_schema, 'class_name': test.split('|')[1], 'fragment_name': test.split('|')[2], 'fragment_type': 'method', 'is_test_method': True})
    
    executable_tests = sorted(executable_tests, key=lambda x: int(x['fragment_name'].split('_')[1][4:]))
    return executable_tests


def get_pending_fragments(fragment_traversal, args):
    """
    Extract all pending fragments which require translation
    """

    processed_fragments, pending_fragments = [], []
    for fragment in fragment_traversal:
        schema_data = {}
        with open(f'{args.translation_dir}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
            schema_data = json.load(f)

        if schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] in ['attempted', 'out_of_context']:
            processed_fragments.append(f'{fragment["schema_name"]}|{fragment["class_name"]}|{fragment["fragment_name"]}')
            continue

        pending_fragments.append(fragment)
    
    return processed_fragments, pending_fragments


def update_labels(args, fragment, translation, translation_status, syntactic_validation, field_exercise, graal_validation, test_execution, elapsed_time, update_test_execution=False):
    """
    Update the labels of the fragment in the schema file
    """
    schema_data = {}
    with open(f'{args.translation_dir}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
        schema_data = json.load(f)
    
    if update_test_execution:
        # if dict ... update test_execution
        if isinstance(schema_data['classes'][fragment['class_name']]['methods'][fragment['fragment_name']]['test_execution'], dict):
            schema_data['classes'][fragment['class_name']]['methods'][fragment['fragment_name']]['test_execution'].update(test_execution)
        else:
            schema_data['classes'][fragment['class_name']]['methods'][fragment['fragment_name']]['test_execution'] = test_execution
    else:
        if translation == '<translated>':
            translation = schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['partial_translation']

        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation'] = translation
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = translation_status
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactic_validation'] = syntactic_validation
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['field_exercise'] = field_exercise
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['graal_validation'] = graal_validation
        if isinstance(schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_execution'], dict):
            pass
        else:
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_execution'] = test_execution
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = elapsed_time
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

    with open(f'{args.translation_dir}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
        json.dump(schema_data, f, indent=4)
        f.flush()
        os.fsync(f.fileno())


def is_field_already_translated(fragment, args):
    """
    Check if a field is already deterministically translated
    """
    prompt_generator = PromptGenerator(is_feedback=False, args=args, fragment_details=fragment)

    if fragment['fragment_type'] == 'field' and prompt_generator.prompt_status == 'translated':
        update_labels(args=args, fragment=fragment, translation=f'<{prompt_generator.prompt_status}>', translation_status='attempted', syntactic_validation='parseable', field_exercise='success', graal_validation='pending', test_execution='pending', elapsed_time=0)
        return True
    
    return False


def is_test_already_translated(test, args):
    """
    Check if a test is already deterministically translated
    """
    test_schema_data = {}
    with open(f'{args.translation_dir}/{test["schema_name"]}_python_partial.json', 'r') as f:
        test_schema_data = json.load(f)

    if test_schema_data['classes'][test['class_name']]['methods'][test['fragment_name']]['translation_status'] == 'attempted':
        return True

    return False


def get_adaptive_budget(fragment, args):
    """
    Get adaptive budget for translation based on dynamic analysis
    1. Fields and static initializers: 3 attempts
    2. Test methods: 3 attempts
    3. Main methods: 10% of total executed tests
    """
    if fragment['fragment_type'] in ['field', 'static_initializer']:
        return 3
    elif fragment['fragment_type'] == 'method' and fragment['is_test_method']:
        return 3
    
    method_coverage = {}
    with open(f'data/source_test_execution{args.suffix}/{args.project_name}/coverage.json', 'r') as f:
        method_coverage = json.load(f)

    main_class_name = fragment['schema_name']
    main_class_name = main_class_name[main_class_name.find('src.main')+9:].replace('.', '/')
    main_method_name = fragment['fragment_name'].split(':')[1]

    total_executed_tests = 0
    total_covered = 0

    for test_class in method_coverage:
        for test_method in method_coverage[test_class]:
            total_executed_tests += 1
            if main_class_name in method_coverage[test_class][test_method]:
                if main_method_name in method_coverage[test_class][test_method][main_class_name]:
                    total_covered += 1 if main_method_name in method_coverage[test_class][test_method][main_class_name] else 0

    assert total_covered < total_executed_tests
    max_budget = max(math.ceil(10 * (total_covered / total_executed_tests)), 3)
    return min(10, max_budget)


def get_total_input_tokens(prompt, client, model_info):
    total_tokens = 0
    for response in client.text.tokenization.create(model_id=model_info[args.model_name]['model_id'], input=prompt):
        total_tokens = response.results[0].token_count

    return total_tokens


def prompt_model(model_info, client, prompt, total_input_tokens, args):
    max_new_tokens = model_info[args.model_name]['total'] - total_input_tokens
    max_new_tokens = min(max_new_tokens, model_info[args.model_name]['max_new_tokens'])

    parameters = TextGenerationParameters(  decoding_method=DecodingMethod.GREEDY,
                                            min_new_tokens=1,
                                            max_new_tokens=max_new_tokens,
                                            return_options=TextGenerationReturnOptions(input_text=True),
                                            time_limit=60000,
                                        )

    for response in client.text.generation.create(model_id=model_info[args.model_name]['model_id'], input=prompt, parameters=parameters):
        generation = response.results[0].input_text + response.results[0].generated_text

    generation = generation[generation.find('### Response:') + len('### Response:'):]

    return generation


def is_test_parseable(test, args):
    """
    Check if a test is translated properly
    """
    schema_data = {}
    with open(f'{args.translation_dir}/{test["schema_name"]}_python_partial.json', 'r') as f:
        schema_data = json.load(f)

    if schema_data['classes'][test['class_name']]['methods'][test['fragment_name']]['syntactic_validation'] == 'parseable':
        return True

    return False


def translate(fragment, args, processed_fragments, feedback=None, recursion_depth=4):

    if recursion_depth == 0:
        return

    # constant variables
    model_info = {
                    'deepseek-coder-33b-instruct': {'total': 16384, 'max_new_tokens': 4096, 'model_id': 'deepseek-ai/deepseek-coder-33b-instruct'},
                    'llama-3-70b-instruct': {'total': 8192, 'max_new_tokens': 2048, 'model_id': 'meta-llama/llama-3-70b-instruct'},
                }
    client = Client(credentials=Credentials.from_env())

    adaptive_budget = get_adaptive_budget(fragment, args)
    BUDGET = {'syntactic': adaptive_budget, 'field_exercise': adaptive_budget, 'graal': adaptive_budget, 'test_execution': adaptive_budget}
    current_budget = 'syntactic'

    start_time = time.time()
    extracted_eligible_tests = False
    eligible_tests = []
    executable_eligible_tests = []

    while BUDGET[current_budget] > 0:

        ############################ <TRANSLATION> ############################
        prompt = PromptGenerator(is_feedback=True if feedback else False, args=args, fragment_details=fragment, feedback=feedback).generate_prompt()

        if args.debug:
            print('=======================PROMPT=======================', flush=True)
            print(prompt, flush=True)
            print('=======================GENERATING=======================', flush=True)

        total_input_tokens = get_total_input_tokens(prompt, client, model_info)
        
        # if prompt size exceeds model token limit, mark translation out_of_context and move on to next fragment
        if total_input_tokens >= model_info[args.model_name]['total']:
            update_labels(args=args, fragment=fragment, translation=[], translation_status='out_of_context', syntactic_validation='pending', field_exercise='pending', graal_validation='pending', test_execution='pending', elapsed_time=0)
            break

        generation = prompt_model(model_info, client, prompt, total_input_tokens, args)

        if args.debug:
            print(generation, flush=True)
            print('---' * 50, flush=True)
        ############################ </TRANSLATION> ############################


        ############################ <SYNTACTIC VALIDATION> ############################
        current_budget = 'syntactic'
        status, generation, feedback = syntactic_validation(generation, fragment, args)

        if not status:
            if BUDGET[current_budget] - 1 == 0:
                # if syntactic validation fails after all syntactic BUDGET attempts, mark translation as non-parseable
                update_labels(args=args, fragment=fragment, translation=[], translation_status='attempted', syntactic_validation='non-parseable', field_exercise='pending', graal_validation='pending', test_execution='pending', elapsed_time=time.time() - start_time)
                break

            if args.debug:
                print('=======================SYNTACTIC VALIDATION FAILED - REPROMPTING=======================', flush=True)

            BUDGET[current_budget] -= 1
            continue

        update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='parseable', field_exercise='pending', graal_validation='pending', test_execution='pending', elapsed_time=time.time() - start_time)
        ############################ </SYNTACTIC VALIDATION> ############################

        if fragment['is_test_method']:
            return

        ############################ <FIELD EXERCISE VALIDATION> ############################
        current_budget = 'field_exercise'
        if fragment['fragment_type'] in ['field', 'static_initializer']:
            status, feedback = field_exercise_validation(fragment, args)
            # if execution validation fails, re-prompt the model
            if not status:
                # if execution validation fails after all field_exercise BUDGET attempts, mark field_exercise status as failed
                if BUDGET[current_budget] - 1 == 0:
                    update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='parseable', field_exercise='failed', graal_validation='pending', test_execution='pending', elapsed_time=time.time() - start_time)
                    break
                
                if args.debug:
                    print('=======================EXECUTION VALIDATION FAILED - REPROMPTING=======================', flush=True)

                BUDGET[current_budget] -= 1
                continue

            # immediately store execution validation status and end the loop
            update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='parseable', field_exercise='success', graal_validation='pending', test_execution='pending', elapsed_time=time.time() - start_time)
            break
        ############################ </FIELD EXERCISE VALIDATION> ############################

        assert fragment['fragment_type'] not in ['field', 'static_initializer']

        ############################ <GRAAL VALIDATION> ############################
        current_budget = 'graal'
        graal_status = 'pending'
        if args.validate_by_graal:
            status, feedback = graal_validation(generation, fragment, args)

            if status == 'error':
                update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='parseable', field_exercise='pending', graal_validation='error', test_execution='pending', elapsed_time=time.time() - start_time)
                graal_status = 'error'

            elif status == 'failure':
                update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='parseable', field_exercise='pending', graal_validation='failed', test_execution='pending', elapsed_time=time.time() - start_time)
                graal_status = 'failed'
                
                if args.debug:
                    print('=======================GRAAL VALIDATION FAILED - REPROMPTING=======================', flush=True)

                BUDGET[current_budget] -= 1
                continue
            
            elif status == 'success':
                update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='parseable', field_exercise='pending', graal_validation='success', test_execution='pending', elapsed_time=time.time() - start_time)
                graal_status = 'success'
        ############################ </GRAAL VALIDATION> ############################


        ############################ <TEST EXECUTION> ############################
        current_budget = 'test_execution'
        if not extracted_eligible_tests:
            eligible_tests = get_eligible_tests(fragment, processed_fragments, args)
            extracted_eligible_tests = True
        
            # if there are no tests ready to be executed, end the loop and mark the fragment as not-exercised
            if eligible_tests == []:
                update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='parseable', field_exercise='pending', graal_validation=graal_status, test_execution='not-exercised', elapsed_time=time.time() - start_time)
                break

            # if there are tests ready to be executed, translate them first
            else:
                for test in eligible_tests:

                    if is_test_already_translated(test, args):
                        executable_eligible_tests.append(test)
                        continue

                    translate(test, args, processed_fragments, recursion_depth=recursion_depth-1)

                    if not is_test_parseable(test, args):
                        continue

                    processed_fragments.append(f'{test["schema_name"]}|{test["class_name"]}|{test["fragment_name"]}')
                    executable_eligible_tests.append(test)

                # if no tests are executable / syntactically correct, end the loop and mark the fragment as not-exercised
                if executable_eligible_tests == []:                    
                    update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='parseable', field_exercise='pending', graal_validation=graal_status, test_execution='not-exercised', elapsed_time=time.time() - start_time)
                    break

        # after eligible tests are translated, validate the main method fragment with test validation
        test_execution_details = test_validation(args, executable_eligible_tests)

        for test in test_execution_details:

            if test_execution_details[test]['test_outcome'] == 'exercised-success':
                for covered_method in test_execution_details[test]['covered_methods']:
                    covered_method_file = covered_method['file']
                    covered_method_class = covered_method['class']
                    covered_method_name = covered_method['method']

                    update_labels(args=args, fragment={'schema_name': covered_method_file, 'class_name': covered_method_class, 'fragment_name': covered_method_name, 'fragment_type': 'method'}, translation=[], translation_status=[], syntactic_validation=[], field_exercise=[], graal_validation=[], test_execution={test: test_execution_details[test]}, elapsed_time=0, update_test_execution=True)
                continue

            # TODO: see if stacktrace can be used to identify test method translation error
            # TODO: what to do if covered methods are empty... definitely test translation should be re-done

            suspicious_methods = {}
            for covered_method in test_execution_details[test]['covered_methods']:
                covered_method_file = covered_method['file']
                covered_method_class = covered_method['class']
                covered_method_name = covered_method['method']

                update_labels(args=args, fragment={'schema_name': covered_method_file, 'class_name': covered_method_class, 'fragment_name': covered_method_name, 'fragment_type': 'method'}, translation=[], translation_status='attempted', syntactic_validation='parseable', field_exercise='pending', graal_validation='pending', test_execution={test: test_execution_details[test]}, elapsed_time=0, update_test_execution=True)

                # if graal flag is set and validates the fragment, skip it from re-prompting
                if args.validate_by_graal:
                    covered_method_schema_data = {}
                    with open(f'{args.translation_dir}/{covered_method_file}_python_partial.json', 'r') as f:
                        covered_method_schema_data = json.load(f)
                    
                    if covered_method_schema_data['classes'][covered_method_class]['methods'][covered_method_name]['graal_validation'] == 'success':
                        continue

                # suspiciousness score = 1 (for now)
                suspicious_methods[f'{covered_method_file}|{covered_method_class}|{covered_method_name}'] = 1
            
            # extract top-k methods with highest suspiciousness score. make k a hyperparameter later.
            suspicious_methods = {k: v for k, v in sorted(suspicious_methods.items(), key=lambda item: item[1], reverse=True)}

            if args.debug:
                print('=======================TEST VALIDATION FAILED - REPROMPTING=======================', flush=True)

            for suspicious_method in suspicious_methods:
                suspicious_method = {'schema_name': suspicious_method.split('|')[0], 'class_name': suspicious_method.split('|')[1], 'fragment_name': suspicious_method.split('|')[2], 'fragment_type': 'method', 'is_test_method': True if 'test' in suspicious_method.split('|')[2] else False}
                translate(suspicious_method, args, processed_fragments, test_execution_details[test]['feedback'], recursion_depth=recursion_depth-1)
        
        break
        ############################ </TEST EXECUTION> ############################


def main(args):

    # constant variables
    args.prompt_type = 'body' if args.include_implementation else 'signature'
    args.translation_dir = f'data/schemas{args.suffix}/translations/{args.model_name}/{args.prompt_type}/{args.project_name}'

    # extract the reverse-topological order of fragments based on call graph
    fragment_traversal = get_reverse_traversal(args)

    # extract all pending fragments which require translation
    processed_fragments, pending_fragments = get_pending_fragments(fragment_traversal, args)
    
    for fragment in tqdm.tqdm(pending_fragments):

        if fragment in processed_fragments:
            continue

        # if a field is already deterministically translated, update labels and move on
        if is_field_already_translated(fragment, args):
            continue
        
        # if a fragment requires translation, translate it with LLM
        translate(fragment, args, processed_fragments, recursion_depth=4)
        processed_fragments.append(f'{fragment["schema_name"]}|{fragment["class_name"]}|{fragment["fragment_name"]}')


if __name__ == '__main__':
    load_dotenv()
    parser_ = argparse.ArgumentParser(description='Translate java types to python types')
    parser_.add_argument('--model_name', type=str, dest='model_name', help='model name to use for translation')
    parser_.add_argument('--project_name', type=str, dest='project_name', help='project name to translate')
    parser_.add_argument('--from_lang', type=str, dest='from_lang', help='language to translate from')
    parser_.add_argument('--to_lang', type=str, dest='to_lang', help='language to translate to')
    parser_.add_argument('--include_call_graph', action='store_true', help='include call graph in translation')
    parser_.add_argument('--include_implementation', action='store_true', help='include implementation of dependent methods')
    parser_.add_argument('--validate_by_graal', action='store_true', help='validate translation by GraalVM')
    parser_.add_argument('--translate_evosuite', action='store_true', help='translate evosuite generated tests')
    parser_.add_argument('--debug', action='store_true', help='debug mode')
    parser_.add_argument('--suffix', type=str, dest='suffix', help='suffix for the translated files')
    args = parser_.parse_args()
    main(args)
