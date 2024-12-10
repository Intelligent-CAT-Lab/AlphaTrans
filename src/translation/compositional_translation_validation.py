import argparse
import json
import tqdm
import os
import time
import re
import math
import datetime
from openai import OpenAI
import tiktoken
import requests

from dotenv import load_dotenv
from src.compositional_glue_tests.script import NOT_EXERCISED, SUCCESS, ERROR, FAILURE
from syntactic_validation import syntactic_validation
from field_exercise_validation import field_exercise_validation
from test_validation import test_validation
from graal_validation import graal_validation
from get_reverse_traversal import get_reverse_traversal
from prompt_generator import PromptGenerator


def get_eligible_tests(fragment, processed_fragments, args):

    global_call_graph = {}
    with open(f'data/call_graphs/{args.project_name}/call_graph.json', 'r') as f:
        global_call_graph = json.load(f)
    
    executed_tests = {}
    with open(f'data/source_test_execution{args.suffix}/{args.project_name}/tests.json', 'r') as f:
        executed_tests = json.load(f)

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
            test_class = test.split('|')[1]
            test_method = test.split('|')[2]

            test_schema_data = {}
            with open(f'{args.translation_dir}/{test_schema}_python_partial.json', 'r') as f:
                test_schema_data = json.load(f)
            if test_class not in test_schema_data['classes']:
                continue
            if test_method not in test_schema_data['classes'][test_class]['methods']:
                continue
            if 'Test' not in [x.split('(')[0] for x in test_schema_data['classes'][test_class]['methods'][test_method]['annotations']]:
                continue
            if 'Ignore' in [x.split('(')[0] for x in test_schema_data['classes'][test_class]['methods'][test_method]['annotations']]:
                continue
            if 'Disabled' in [x.split('(')[0] for x in test_schema_data['classes'][test_class]['methods'][test_method]['annotations']]:
                continue
            # test_class_path = test_schema[test_schema.find('src.test.')+len('src.test.'):]
            # if test_method.split(':')[1] not in executed_tests[test_class_path]:
            #     continue

            executable_tests.append({'schema_name': test_schema, 'class_name': test_class, 'fragment_name': test_method, 'fragment_type': 'method', 'is_test_method': True})
    
    non_decomposed_tests = [x for x in executable_tests if '_decomposed' not in x['fragment_name']]
    executable_tests = [x for x in executable_tests if '_decomposed' in x['fragment_name']]
    executable_tests = sorted(executable_tests, key=lambda x: int(x['fragment_name'].split('_')[-2][4:]))
    executable_tests = executable_tests + non_decomposed_tests
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


def update_budget(fragment, args, budget, type_='original'):
    schema_data = {}
    with open(f'{args.translation_dir}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
        schema_data = json.load(f)
    
    schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']][f'{type_}_budget'] = budget

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
        update_budget(fragment, args, budget={'syntactic': -1, 'field_exercise': -1, 'graal': -1, 'test_execution': -1}, type_='original')
        update_budget(fragment, args, budget={'syntactic': -1, 'field_exercise': -1, 'graal': -1, 'test_execution': -1}, type_='final')
        update_labels(args=args, fragment=fragment, translation=f'<{prompt_generator.prompt_status}>', translation_status='attempted', syntactic_validation='parseable', field_exercise='success', graal_validation='pending', test_execution='pending', elapsed_time=0)
        return True
    
    return False


def is_test_already_translated(test, args):
    """
    Check if a test is already translated and syntactically correct
    """
    test_schema_data = {}
    with open(f'{args.translation_dir}/{test["schema_name"]}_python_partial.json', 'r') as f:
        test_schema_data = json.load(f)

    if test_schema_data['classes'][test['class_name']]['methods'][test['fragment_name']]['syntactic_validation'] == 'parseable':
        return True

    return False


def get_adaptive_budget(fragment, args, feedback=False):
    """
    Get adaptive budget for translation based on dynamic analysis
    1. Fields and static initializers: 3 attempts
    2. Test methods: 3 attempts
    3. Main methods: 10% of total executed tests
    """
    if fragment['fragment_type'] in ['field', 'static_initializer']:
        return 2 if not feedback else 1
    elif fragment['fragment_type'] == 'method' and fragment['is_test_method']:
        return 2 if not feedback else 1
    
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
    max_budget = max(math.ceil(5 * (total_covered / total_executed_tests)), 2)
    if not feedback:
        return min(5, max_budget)
    else:
        return 1


def get_total_input_tokens(prompt, args, model_info):
    if args.use_openai and args.model_name == 'gpt-4o-2024-11-20':
        encoding = tiktoken.encoding_for_model('gpt-4o')
        total_tokens = len(encoding.encode(prompt))
    elif args.use_vllm:
        response = requests.post(url='/'.join(os.environ['VLLM_API_URL'].split('/')[:-1]) + '/tokenize', headers={'accept': 'application/json', 'VLLM_API_KEY': os.environ['VLLM_API_KEY'], 'Content-Type': 'application/json'}, json={'model': model_info[args.model_name]['model_id'], 'prompt': prompt, 'add_special_tokens': True})
        total_tokens = response.json()['count']

    return total_tokens


def prompt_model(model_info, client, prompt, total_input_tokens, args):
    max_new_tokens = model_info[args.model_name]['total'] - total_input_tokens
    max_new_tokens = min(max_new_tokens, model_info[args.model_name]['max_new_tokens'])

    if args.use_openai:
        completion = client.chat.completions.create(
            model=args.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=max_new_tokens,
            temperature=args.temperature,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        generation = completion.choices[0].message.content

    elif args.use_vllm:
        completion = client.completions.create(
            model=model_info[args.model_name]['model_id'],
            prompt=prompt,
            temperature=args.temperature,
            echo=True,
            max_tokens=max_new_tokens
        )

        generation = completion.choices[0].text
        generation = generation[generation.find('### Response:') + len('### Response:'):]
    
    else:
        raise ValueError('No API specified')

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


def get_test_fragment(test, executable_eligible_tests):
    test_fragment = {}
    for test_ in executable_eligible_tests:
        test_schema = test.split('::')[0].replace('/', '.').replace('.py', '')
        test_class = test.split('::')[1]
        test_method = test.split('::')[2]

        if test_schema == test_['schema_name'] and test_class == test_['class_name'] and test_method == test_['fragment_name'].split(':')[1]:
            test_fragment = test_
            break
    
    return test_fragment


def test_has_attribute_error(test_execution_details):
    # Regular expression to match the AttributeError
    error_regex = r"AttributeError: (.+)"
    method_regex = r"File \"(.+)\", line \d+, in (\w+)"
    
    error_message = None
    filepath = None
    method_name = None
    traceback_str = test_execution_details['feedback']

    lines = traceback_str.strip().splitlines()
    
    for i, line in enumerate(lines):
        # Match the error message
        error_match = re.search(error_regex, line)
        if error_match:
            error_message = "AttributeError: " + error_match.group(1)
        
        # Match the method name and file path
        method_match = re.search(method_regex, line)
        if method_match:
            filepath = method_match.group(1)
            method_name = method_match.group(2)
    
    if '_decomposed' not in method_name or 'test' not in method_name:
        return False

    if 'src/test' in filepath and (error_message and 'AttributeError' in error_message):
        return True
    
    return False


def get_suspiciousness_score(fragment):
    
    schema_data = {}
    with open(f'{args.translation_dir}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
        schema_data = json.load(f)
    
    total_tests = 0
    failed_tests = 0

    if isinstance(schema_data['classes'][fragment['class_name']]['methods'][fragment['fragment_name']]['test_execution'], dict):
        for test in schema_data['classes'][fragment['class_name']]['methods'][fragment['fragment_name']]['test_execution']:
            total_tests += 1
            if schema_data['classes'][fragment['class_name']]['methods'][fragment['fragment_name']]['test_execution'][test]['test_outcome'] == 'exercised-failed':
                failed_tests += 1
    
    return failed_tests / total_tests


def translate(fragment, args, processed_fragments, budget={}, feedback=None, recursion_depth=2):

    if recursion_depth == 0:
        return

    model_info = {
                    'deepseek-coder-33b-instruct': {'total': 16384, 'max_new_tokens': 4096, 'model_id': 'deepseek-ai/deepseek-coder-33b-instruct'},
                    'llama-3-70b-instruct': {'total': 8192, 'max_new_tokens': 2048, 'model_id': 'meta-llama/llama-3-70b-instruct'},
                    'gpt-4o-2024-11-20': {'total': 128000, 'max_new_tokens': 16384, 'model_id': 'gpt-4o-2024-11-20'},
                    'llama-3-1-405b-instruct-fp8': {'total': 128000, 'max_new_tokens': 8196, 'model_id': 'meta-llama/llama-3-1-405b-instruct-fp8'},
                    'Qwen2.5-Coder-32B-Instruct': {'total': 131072, 'max_new_tokens': 8196, 'model_id': 'Qwen/Qwen2.5-Coder-32B-Instruct'}
                }

    if args.use_vllm:
        client = OpenAI(
            api_key=os.environ["VLLM_API_KEY"],  
            base_url=os.environ["VLLM_API_URL"],
        )
    elif args.use_openai:
        client = OpenAI(
            api_key=os.environ["OPENAI_API_KEY"],
        )
    else:
        raise ValueError('No API specified')

    if budget == {}:
        adaptive_budget = get_adaptive_budget(fragment, args)
        budget = {'syntactic': adaptive_budget, 'field_exercise': adaptive_budget, 'graal': adaptive_budget, 'test_execution': adaptive_budget}
        adaptive_budget_feedback = get_adaptive_budget(fragment, args, feedback=True)
        feedback_budget = {'syntactic': adaptive_budget_feedback, 'field_exercise': adaptive_budget_feedback, 'graal': adaptive_budget_feedback, 'test_execution': adaptive_budget_feedback}

        update_budget(fragment, args, budget, type_='original')

    current_budget = 'syntactic'
    start_time = time.time()
    extracted_eligible_tests = False
    eligible_tests = []
    executable_eligible_tests = []

    while budget[current_budget] > 0:

        ############################ <TRANSLATION> ############################
        prompt = PromptGenerator(is_feedback=True if feedback else False, args=args, fragment_details=fragment, feedback=feedback).generate_prompt()

        if args.debug:
            print('=======================PROMPT=======================', flush=True)
            print(prompt, flush=True)
            print('=======================GENERATING=======================', flush=True)

        total_input_tokens = get_total_input_tokens(prompt, args, model_info)
        
        # if prompt size exceeds model token limit, mark translation out_of_context and move on to next fragment
        if total_input_tokens >= model_info[args.model_name]['total']:
            update_labels(args=args, fragment=fragment, translation=[], translation_status='out_of_context', syntactic_validation='pending', field_exercise='pending', graal_validation='pending', test_execution='pending', elapsed_time=0)
            update_budget(fragment, args, budget, type_='final')
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
            if budget[current_budget] - 1 == 0:
                # if syntactic validation fails after all syntactic budget attempts, mark translation as non-parseable
                update_labels(args=args, fragment=fragment, translation=[], translation_status='attempted', syntactic_validation='non-parseable', field_exercise='pending', graal_validation='pending', test_execution='pending', elapsed_time=time.time() - start_time)
                update_budget(fragment, args, budget, type_='final')
                break

            if args.debug:
                print('=======================SYNTACTIC VALIDATION FAILED - REPROMPTING=======================', flush=True)

            budget[current_budget] -= 1
            continue

        update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='parseable', field_exercise='pending', graal_validation='pending', test_execution='pending', elapsed_time=time.time() - start_time)
        update_budget(fragment, args, budget, type_='final')
        ############################ </SYNTACTIC VALIDATION> ############################

        if fragment['is_test_method']:
            return

        ############################ <FIELD EXERCISE VALIDATION> ############################
        current_budget = 'field_exercise'
        status, feedback = field_exercise_validation(fragment, args)
        # if execution validation fails, re-prompt the model
        if not status:
            # if execution validation fails after all field_exercise budget attempts, mark field_exercise status as failed
            if budget[current_budget] - 1 == 0:
                if fragment['fragment_type'] == 'method':
                    update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='non-parseable', field_exercise='pending', graal_validation='pending', test_execution='pending', elapsed_time=time.time() - start_time)
                else:
                    update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='parseable', field_exercise='failed', graal_validation='pending', test_execution='pending', elapsed_time=time.time() - start_time)
                    
                update_budget(fragment, args, budget, type_='final')
                break
            
            if args.debug:
                print('=======================EXECUTION VALIDATION FAILED - REPROMPTING=======================', flush=True)

            budget[current_budget] -= 1
            continue

        # immediately store execution validation status and end the loop
        if fragment['fragment_type'] == 'method':
            update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='parseable', field_exercise='pending', graal_validation='pending', test_execution='pending', elapsed_time=time.time() - start_time)
        else:
            update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='parseable', field_exercise='success', graal_validation='pending', test_execution='pending', elapsed_time=time.time() - start_time)
        update_budget(fragment, args, budget, type_='final')

        if fragment['fragment_type'] in ['field', 'static_initializer']:
            break
        ############################ </FIELD EXERCISE VALIDATION> ############################

        assert fragment['fragment_type'] not in ['field', 'static_initializer']

        ############################ <GRAAL VALIDATION> ############################
        current_budget = 'graal'
        graal_status = 'pending'
        if args.validate_by_graal and 'src.main' in fragment['schema_name']:
            status, feedback, message = graal_validation(generation, fragment, args)
            update_labels(args=args, fragment=fragment, translation=generation, translation_status='attempted', syntactic_validation='parseable', field_exercise='pending', graal_validation={'outcome': status, 'message': message}, test_execution='pending', elapsed_time=time.time() - start_time)
            update_budget(fragment, args, budget, type_='final')

            if status == NOT_EXERCISED:
                graal_status = 'not-exercised'

            elif status == ERROR:
                graal_status = 'error'

            elif status == FAILURE:
                graal_status = 'failed'
                
                if args.debug:
                    print('=======================GRAAL VALIDATION FAILED - REPROMPTING=======================', flush=True)

                budget[current_budget] -= 1
                continue
            
            elif status == SUCCESS:
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
                update_budget(fragment, args, budget, type_='final')
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
                    update_budget(fragment, args, budget, type_='final')
                    break

        # after eligible tests are translated, validate the main method fragment with test validation
        test_execution_details = test_validation(args, executable_eligible_tests)

        requires_reprompt = False
        for test in test_execution_details:

            if test_execution_details[test]['test_outcome'] == 'exercised-success':
                for covered_method in test_execution_details[test]['covered_methods']:
                    covered_method_file = covered_method['file']
                    covered_method_class = covered_method['class']
                    covered_method_name = covered_method['method']

                    update_labels(args=args, fragment={'schema_name': covered_method_file, 'class_name': covered_method_class, 'fragment_name': covered_method_name, 'fragment_type': 'method'}, translation=[], translation_status=[], syntactic_validation=[], field_exercise=[], graal_validation=[], test_execution={test: test_execution_details[test]}, elapsed_time=0, update_test_execution=True)
                continue

            requires_reprompt = True

            if args.debug:
                print('=======================TEST VALIDATION FAILED - REPROMPTING=======================', flush=True)

            # heuristic 1: if no methods are covered and test fails, the problem is guaranteed to be in the test method. re-prompt the test method.
            # heuristic 2: if stacktrace shows an AttributeError in the test method, re-prompt the test method only
            if test_execution_details[test]['covered_methods'] == [] or test_has_attribute_error(test_execution_details[test]):

                test_fragment = get_test_fragment(test, executable_eligible_tests)
                if test_fragment == {}:
                    continue
                
                translate(test_fragment, args, processed_fragments, budget=feedback_budget if recursion_depth==2 else budget, feedback=test_execution_details[test]['feedback'], recursion_depth=recursion_depth-1)
                continue            

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
                    
                    if covered_method_schema_data['classes'][covered_method_class]['methods'][covered_method_name]['graal_validation'] in ['success', 'not-exercised']:
                        continue

                # suspiciousness score = total number of failed tests / total number of tests
                suspicious_methods[f'{covered_method_file}|{covered_method_class}|{covered_method_name}'] = get_suspiciousness_score(fragment={'schema_name': covered_method_file, 'class_name': covered_method_class, 'fragment_name': covered_method_name, 'fragment_type': 'method'})
            
            # extract top-k methods with highest suspiciousness score. make k a hyperparameter later.
            k = 3
            suspicious_methods = {k: v for k, v in sorted(suspicious_methods.items(), key=lambda item: item[1], reverse=True)[:k]}

            for suspicious_method in suspicious_methods:
                suspicious_method = {'schema_name': suspicious_method.split('|')[0], 'class_name': suspicious_method.split('|')[1], 'fragment_name': suspicious_method.split('|')[2], 'fragment_type': 'method', 'is_test_method': True if 'test' in suspicious_method.split('|')[2] else False}
                translate(suspicious_method, args, processed_fragments, budget=feedback_budget if recursion_depth==2 else budget, feedback=test_execution_details[test]['feedback'], recursion_depth=recursion_depth-1)

        if args.debug:
            print('=======================TEST VALIDATION FAILED - REPROMPTING=======================', flush=True)
            print('recursion_depth:', recursion_depth, flush=True)
            print('budget:', budget, flush=True)

        if requires_reprompt:
            budget[current_budget] -= 1
            continue

        break
        ############################ </TEST EXECUTION> ############################


def main(args):

    # constant variables
    args.prompt_type = 'body' if args.include_implementation else 'signature'
    args.use_openai = True if not args.use_vllm else False
    args.translation_dir = f'data/schemas{args.suffix}/translations/{args.model_name}/{args.prompt_type}/{args.temperature}/{args.project_name}'

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
        translate(fragment, args, processed_fragments, recursion_depth=args.recursion_depth)
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
    parser_.add_argument('--temperature', type=float, dest='temperature', help='temperature for generation')
    parser_.add_argument('--suffix', type=str, dest='suffix', help='suffix for the translated files')
    parser_.add_argument('--recursion_depth', type=int, dest='recursion_depth', help='depth of recursion for translation')
    parser_.add_argument('--use_vllm', action='store_true', help='use VLLM engine for prompting')
    args = parser_.parse_args()
    main(args)
