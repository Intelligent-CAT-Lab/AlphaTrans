import json
import os
import time
import datetime
from syntactic_validation import syntactic_validation
from prompt_generator import PromptGenerator

from genai.client import Client
from genai.credentials import Credentials
from genai.schema import (
    DecodingMethod,
    TextGenerationParameters,
    TextGenerationReturnOptions,
)


def translate_feedback(suspicious_fragments, feedback, args):

    model_info = {
                    'deepseek-coder-33b-instruct': {'total': 16384, 'max_new_tokens': 4096, 'model_id': 'deepseek-ai/deepseek-coder-33b-instruct'},
                    'llama-3-70b-instruct': {'total': 8192, 'max_new_tokens': 2048, 'model_id': 'meta-llama/llama-3-70b-instruct'},
                }

    client = Client(credentials=Credentials.from_env())
    model_id = model_info[args.model_name]['model_id']

    for fragment in suspicious_fragments:

        max_attempts = 0
        start_time = time.time()

        fragment = {'schema_name': fragment.split('|')[0], 'class_name': fragment.split('|')[1], 'fragment_name': fragment.split('|')[2], 'fragment_type': 'method'}

        while max_attempts < 5:
            
            prompt_gen = PromptGenerator(is_feedback=True, args=args, fragment_details=fragment, feedback=feedback)
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

            # if there is a syntax error, mark translation as failed and repeat the process at most 5 times
            if not status:

                # immediately store syntactic validation status
                schema_data = {}
                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                    schema_data = json.load(f)
                
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['syntactical_validation_status'] = 'failed'
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
                schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                    json.dump(schema_data, f, indent=4)
                    f.flush()
                    os.fsync(f.fileno())

                max_attempts += 1
                continue

            # immediately store syntactic validation status
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

            schema_data = {}
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'r') as f:
                schema_data = json.load(f)
            
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['translation_status'] = 'attempted'
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['elapsed_time'] = time.time() - start_time
            schema_data['classes'][fragment['class_name']][f'{fragment["fragment_type"]}s'][fragment['fragment_name']]['generation_timestamp'] = datetime.datetime.now().isoformat()

            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{fragment["schema_name"]}_python_partial.json', 'w') as f:
                json.dump(schema_data, f, indent=4)
                f.flush()
                os.fsync(f.fileno())

            break
