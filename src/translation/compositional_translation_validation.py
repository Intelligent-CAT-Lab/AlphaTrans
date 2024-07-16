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
from prompt_generator import PromptGenerator

from genai.client import Client
from genai.credentials import Credentials
from genai.schema import (
    DecodingMethod,
    TextGenerationParameters,
    TextGenerationReturnOptions,
)


def translate(fragment, args, prompt_gen):

    model_info = {
                    'deepseek-coder-33b-instruct': {'total': 16384, 'max_new_tokens': 4096, 'model_id': 'deepseek-ai/deepseek-coder-33b-instruct'},
                    'llama-3-70b-instruct': {'total': 8192, 'max_new_tokens': 2048, 'model_id': 'meta-llama/llama-3-70b-instruct'},
                }

    client = Client(credentials=Credentials.from_env())
    model_id = model_info[args.model_name]['model_id']

    max_attempts = 0
    start_time = time.time()

    while max_attempts < 5:

        prompt = prompt_gen.generate_prompt()

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
            
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'failed'
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
            # TODO: re-prompt the model with feedback

            # immediately store syntactic validation status
            schema_data = {}
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                schema_data = json.load(f)
            
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'failed'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'failed'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['execution_validation_status'] = 'failed'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_validation_status'] = 'failed'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['graal_validation_status'] = 'failed'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                json.dump(schema_data, f, indent=4)
                f.flush()
                os.fsync(f.fileno())

            max_attempts = 5 # change this later
            continue

        # immediately store syntactic validation status
        schema_data = {}
        with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
            schema_data = json.load(f)
        
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation'] = generation
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'pending'
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'success'
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['execution_validation_status'] = 'pending'
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_validation_status'] = 'pending'
        schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['graal_validation_status'] = 'pending'
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
                # TODO: re-prompt the model with feedback

                # immediately store execution validation status
                schema_data = {}
                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                    schema_data = json.load(f)
                
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'failed'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'success'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['execution_validation_status'] = 'failed'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_validation_status'] = 'failed'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['graal_validation_status'] = 'failed'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                    json.dump(schema_data, f, indent=4)
                    f.flush()
                    os.fsync(f.fileno())

                max_attempts = 5 # change this later
                continue

            # immediately store execution validation status and end the loop
            schema_data = {}
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                schema_data = json.load(f)
            
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['execution_validation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_validation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['graal_validation_status'] = 'success'
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
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['execution_validation_status'] = 'pending'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_validation_status'] = 'pending'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['graal_validation_status'] = 'pending'
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
                pass

            elif status == 'failure':
                # TODO: re-prompt the model with feedback

                # immediately store graal validation status
                schema_data = {}
                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                    schema_data = json.load(f)
                
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'failed'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'success'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['execution_validation_status'] = 'pending'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_validation_status'] = 'pending'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['graal_validation_status'] = 'failed'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                    json.dump(schema_data, f, indent=4)
                    f.flush()
                    os.fsync(f.fileno())
            
            elif status == 'success':
                
                # immediately store graal validation status
                schema_data = {}
                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                    schema_data = json.load(f)
                
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'pending'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'success'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['execution_validation_status'] = 'success'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_validation_status'] = 'pending'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['graal_validation_status'] = 'success'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                    json.dump(schema_data, f, indent=4)
                    f.flush()
                    os.fsync(f.fileno())

        # TODO: perform test execution

        break
        


def main(args):

    args.prompt_type = 'body' if args.include_implementation else 'signature'

    fragment_traversal = get_traversal(args)

    for fragment in tqdm.tqdm(fragment_traversal):

        schema_data = {}
        with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
            schema_data = json.load(f)

        if schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] in ['success', 'failed']:
            continue

        prompt_gen = PromptGenerator(is_feedback=False, args=args, fragment_details=fragment)
        prompt_status = prompt_gen.prompt_status

        # if a field is already deterministically translated, skip it
        if fragment['fragment_type'] == 'field' and prompt_status == 'error':
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation'] = schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['partial_translation']
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = 0
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['execution_validation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['test_validation_status'] = 'success'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['graal_validation_status'] = 'success'

            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                json.dump(schema_data, f, indent=4)
                f.flush()
                os.fsync(f.fileno())

            continue

        translate(fragment, args, prompt_gen)

        break


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
