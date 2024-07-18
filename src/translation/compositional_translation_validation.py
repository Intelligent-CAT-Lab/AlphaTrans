import argparse
import json
from dotenv import load_dotenv
import tqdm
import os
import time
import datetime
from syntactic_validation import syntactic_validation
from execution_validaton import execution_validation
from test_validation import test_validation
from graal_validation import graal_validation
from get_traversal import get_traversal
from translate_test import translate_test
from translate_feedback import translate_feedback
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
            executable_tests.append({'schema_name': test_schema, 'class_name': test.split('|')[1], 'fragment_name': test.split('|')[2], 'fragment_type': 'method'})
    
    return executable_tests


def translate(fragment, args, processed_fragments, fragment_test_stats):

    model_info = {
                    'deepseek-coder-33b-instruct': {'total': 16384, 'max_new_tokens': 4096, 'model_id': 'deepseek-ai/deepseek-coder-33b-instruct'},
                    'llama-3-70b-instruct': {'total': 8192, 'max_new_tokens': 2048, 'model_id': 'meta-llama/llama-3-70b-instruct'},
                }

    client = Client(credentials=Credentials.from_env())
    model_id = model_info[args.model_name]['model_id']

    max_attempts = 0
    start_time = time.time()

    prompt_gen = PromptGenerator(is_feedback=False, args=args, fragment_details=fragment)
    prompt = prompt_gen.generate_prompt()

    while max_attempts < 5:

        if args.debug:
            print('=======================PROMPT=======================', flush=True)
            print(prompt, flush=True)
            print('=======================GENERATING=======================', flush=True)

        total_tokens = 0
        for response in client.text.tokenization.create(model_id=model_id, input=prompt):
            total_tokens = response.results[0].token_count
        
        # if prompt size exceeds model token limit, mark translation as failed
        if total_tokens > model_info[args.model_name]['total']:
            schema_data = {}
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                schema_data = json.load(f)
            
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'attempted'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'failed'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['execution_validation_status'] = 'failed'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_validation_status'] = 'failed'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['graal_validation_status'] = 'failed'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = -1 # elapsed time is -1 for token limit exceeded
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                json.dump(schema_data, f, indent=4)
                f.flush()
                os.fsync(f.fileno())

            break

        max_new_tokens = model_info[args.model_name]['total'] - total_tokens
        max_new_tokens = min(max_new_tokens, model_info[args.model_name]['max_new_tokens'])

        parameters = TextGenerationParameters(  decoding_method=DecodingMethod.GREEDY,
                                                min_new_tokens=1,
                                                max_new_tokens=max_new_tokens,
                                                return_options=TextGenerationReturnOptions(
                                                    input_text=True,
                                                ),
                                                time_limit=60000,
                                            )

        for response in client.text.generation.create(model_id=model_id, input=prompt, parameters=parameters):
            generation = response.results[0].input_text + response.results[0].generated_text

        generation = generation[generation.find('### Response:') + len('### Response:'):]

        if args.debug:
            print(generation, flush=True)
            print('---' * 50, flush=True)

        status, generation, feedback = syntactic_validation(generation, fragment, args)

        if not status:

            # immediately store syntactic validation status
            schema_data = {}
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                schema_data = json.load(f)
            
            if max_attempts == 4:
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'attempted'

            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'failed'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']].setdefault('re_prompt_count', 0)
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['re_prompt_count'] += 1
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                json.dump(schema_data, f, indent=4)
                f.flush()
                os.fsync(f.fileno())

            if args.debug:
                print('=======================SYNTACTIC VALIDATION FAILED - REPROMPTING=======================', flush=True)
            
            prompt = PromptGenerator(is_feedback=True, args=args, fragment_details=fragment, feedback=feedback).generate_prompt()

            max_attempts += 1
            continue

        # immediately store syntactic validation status
        schema_data = {}
        with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
            schema_data = json.load(f)
        
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation'] = generation
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'success'
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

        with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
            json.dump(schema_data, f, indent=4)
            f.flush()
            os.fsync(f.fileno())

        # perform execution check if fragment is a field
        if fragment['fragment_type'] in ['field', 'static_initializer']:
            status, feedback = execution_validation(fragment, args)

            if not status:

                # immediately store execution validation status
                schema_data = {}
                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                    schema_data = json.load(f)
                
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['execution_validation_status'] = 'failed'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']].setdefault('re_prompt_count', 0)
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['re_prompt_count'] += 1
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                    json.dump(schema_data, f, indent=4)
                    f.flush()
                    os.fsync(f.fileno())
                
                if args.debug:
                    print('=======================EXECUTION VALIDATION FAILED - REPROMPTING=======================', flush=True)
                
                prompt = PromptGenerator(is_feedback=True, args=args, fragment_details=fragment, feedback=feedback).generate_prompt()

                max_attempts += 1
                continue

            # immediately store execution validation status and end the loop
            schema_data = {}
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                schema_data = json.load(f)
            
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'attempted'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['execution_validation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                json.dump(schema_data, f, indent=4)
                f.flush()
                os.fsync(f.fileno())
            
            break

        # make sure all field translation does not reach this point
        assert fragment['fragment_type'] != 'field'

        # if a fragment is a test method, end the loop after syntactic validation
        if fragment['fragment_type'] == 'method' and 'src.test' in fragment['schema_name']:

            schema_data = {}
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                schema_data = json.load(f)
            
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation'] = generation
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'attempted'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                json.dump(schema_data, f, indent=4)
                f.flush()
                os.fsync(f.fileno())

            break

        if args.validate_by_graal:
            status, feedback = graal_validation(generation, fragment, args)

            # graal could not validate the fragment. no feedback required
            if status == 'error':

                # immediately store graal validation status
                schema_data = {}
                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                    schema_data = json.load(f)
                
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['graal_validation_status'] = 'error'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                    json.dump(schema_data, f, indent=4)
                    f.flush()
                    os.fsync(f.fileno())

            elif status == 'failure':

                # immediately store graal validation status
                schema_data = {}
                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                    schema_data = json.load(f)
                
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['graal_validation_status'] = 'failed'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']].setdefault('re_prompt_count', 0)
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['re_prompt_count'] += 1
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                    json.dump(schema_data, f, indent=4)
                    f.flush()
                    os.fsync(f.fileno())
                
                if args.debug:
                    print('=======================GRAAL VALIDATION FAILED - REPROMPTING=======================', flush=True)
                
                prompt = PromptGenerator(is_feedback=True, args=args, fragment_details=fragment, feedback=feedback).generate_prompt()

                max_attempts += 1
                continue
            
            elif status == 'success':
                
                # immediately store graal validation status
                schema_data = {}
                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                    schema_data = json.load(f)
                
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['graal_validation_status'] = 'success'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                    json.dump(schema_data, f, indent=4)
                    f.flush()
                    os.fsync(f.fileno())

        eligible_tests = get_eligible_tests(fragment, processed_fragments, args)
        available_eligible_tests = []
        
        # if there are no tests ready to be executed, end the loop and store the results
        if eligible_tests == []:
            schema_data = {}
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                schema_data = json.load(f)
            
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'attempted'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_validation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                json.dump(schema_data, f, indent=4)
                f.flush()
                os.fsync(f.fileno())
            
            break

        # if there are tests ready to be executed, translate them
        else:
            for test in eligible_tests:

                test_schema_data = {}
                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{test["schema_name"]}_python_partial.json', 'r') as f:
                    test_schema_data = json.load(f)

                if test['class_name'] not in test_schema_data['classes']:
                    continue

                if test['fragment_name'] not in test_schema_data['classes'][test['class_name']]['methods']:
                    continue

                if test_schema_data['classes'][test['class_name']]['methods'][test['fragment_name']]['translation_status'] == 'attempted':
                    available_eligible_tests.append(test)
                    continue

                test_translated = translate_test(test, args)
                # exclude test if not translated properly
                if not test_translated:
                    continue

                processed_fragments.append(f'{test["schema_name"]}|{test["class_name"]}|{test["fragment_name"]}')
                available_eligible_tests.append(test)

            # if no tests are available, end the loop and store the results
            if available_eligible_tests == []:
                schema_data = {}
                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                    schema_data = json.load(f)
                
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'attempted'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_validation_status'] = 'failed'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                    json.dump(schema_data, f, indent=4)
                    f.flush()
                    os.fsync(f.fileno())
                
                break

        # after eligible tests are translated, validate the main method fragment with test valiation
        status, feedback, covered_methods = test_validation(args, available_eligible_tests, fragment_test_stats)

        if not status:

            suspicious_methods = {}
            for covered_method in covered_methods:
                covered_method_file = covered_method['file'][covered_method['file'].index(args.project_name):].replace('.py', '').replace('/', '.')
                covered_method_class = covered_method['class']
                covered_method_name = covered_method['method']

                # if graal flag is set and validates the fragment, skip it from re-prompting
                if args.validate_by_graal:
                    covered_method_schema_data = {}
                    with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{covered_method_file}_python_partial.json', 'r') as f:
                        covered_method_schema_data = json.load(f)
                    
                    if covered_method_schema_data['classes'][covered_method_class]['methods'][covered_method_name]['graal_validation_status'] == 'success':
                        continue

                # suspiciousness score = (total failed tests / total tests)
                suspicious_methods[f'{covered_method_file}|{covered_method_class}|{covered_method_name}'] = len(fragment_test_stats[f'{covered_method_file}|{covered_method_class}|{covered_method_name}']['fail']) / len(fragment_test_stats[f'{covered_method_file}|{covered_method_class}|{covered_method_name}']['total'])
            
            # extract top-k methods with highest suspiciousness score. make k a hyperparameter later.
            suspicious_methods = {k: v for k, v in sorted(suspicious_methods.items(), key=lambda item: item[1], reverse=True)}

            # immediately store test validation status
            schema_data = {}
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                schema_data = json.load(f)
            
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'attempted'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_validation_status'] = 'failed'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                json.dump(schema_data, f, indent=4)
                f.flush()
                os.fsync(f.fileno())

            if args.debug:
                print('=======================TEST VALIDATION FAILED - REPROMPTING=======================', flush=True)

            # re-prompt suspicious fragments with feedback
            translate_feedback(suspicious_methods, feedback, args)

            # after re-prompting, attempt to translate the current fragment again with base prompt
            prompt = PromptGenerator(is_feedback=False, args=args, fragment_details=fragment).generate_prompt()
            max_attempts += 1
            continue
        
        # immediately store test validation status
        schema_data = {}
        with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
            schema_data = json.load(f)
        
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'attempted'
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_validation_status'] = 'success'
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

        with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
            json.dump(schema_data, f, indent=4)
            f.flush()
            os.fsync(f.fileno())

        break


def main(args):

    args.prompt_type = 'body' if args.include_implementation else 'signature'

    fragment_traversal = get_traversal(args)

    processed_fragments = []
    fragment_test_stats = {}

    for fragment in tqdm.tqdm(fragment_traversal):

        if f'{fragment["schema_name"]}|{fragment["class_name"]}|{fragment["fragment_name"]}' in processed_fragments:
            continue

        schema_data = {}
        with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
            schema_data = json.load(f)

        if schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] == 'attempted':
            processed_fragments.append(f'{fragment["schema_name"]}|{fragment["class_name"]}|{fragment["fragment_name"]}')
            continue

        prompt_gen = PromptGenerator(is_feedback=False, args=args, fragment_details=fragment)
        prompt_status = prompt_gen.prompt_status

        # if a field is already deterministically translated, skip it
        if fragment['fragment_type'] == 'field' and prompt_status == 'error':
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation'] = schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['partial_translation']
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'attempted'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['execution_validation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = 0
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                json.dump(schema_data, f, indent=4)
                f.flush()
                os.fsync(f.fileno())

            continue

        translate(fragment, args, processed_fragments, fragment_test_stats)
        processed_fragments.append(f'{fragment["schema_name"]}|{fragment["class_name"]}|{fragment["fragment_name"]}')

    with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/fragment_test_stats.json', 'w') as f:
        json.dump(fragment_test_stats, f, indent=4)
        f.flush()
        os.fsync(f.fileno())


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
    args = parser_.parse_args()
    main(args)
