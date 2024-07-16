import argparse
import json
from dotenv import load_dotenv
import torch
import tqdm
import os
import time
import datetime
import requests
from transformers import AutoTokenizer, AutoModelForCausalLM
from syntactic_validation import l0_validation
from semantic_validation import l1_validation
from functional_validation import l2_validation
from get_traversal import get_traversal
from prompt_generator import PromptGenerator

from genai.client import Client
from genai.credentials import Credentials
from genai.schema import (
    DecodingMethod,
    TextGenerationParameters,
    TextGenerationReturnOptions,
)


def get_dependency_path(dependent_class, project_name):
    if os.path.exists(f'java_projects/cleaned_final_projects/{project_name}/src/main/java/' + dependent_class.replace('.', '/') + '.java'):
        return f'src.main.{dependent_class}'
    elif os.path.exists(f'java_projects/cleaned_final_projects/{project_name}/src/test/java/' + dependent_class.replace('.', '/') + '.java'):
        return f'src.test.{dependent_class}'
    else:
        return f'src.main.{dependent_class}'


def translate(model, tokenizer, device, members_to_translate: list[list], processed_fragments, args):
    """
    members_to_translate: [prompt, fragment, use_bam, project_name, schema, class_, fragment_]
    """
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
        fixing_same_fragment = True
        translated_fragment = False
        original_schema, original_class, original_fragment = schema, class_, fragment_
        while max_attempts < 5:

            schema_data = {}
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{schema}', 'r') as f:
                schema_data = json.load(f)

            if feedback == '':
                prompt = generate_prompt(schema_data, schema, class_, fragment_, args, fragment, args.model_name)

            print(prompt, flush=True)
            print('=======================GENERATING=======================', flush=True)

            model_info = {
                            'deepseek-coder-33b-instruct': {'total': 16384, 'max_new_tokens': 4096, 'model_id': 'deepseek-ai/deepseek-coder-33b-instruct'},
                            'llama-3-70b-instruct': {'total': 8192, 'max_new_tokens': 2048, 'model_id': 'meta-llama/llama-3-70b-instruct'},
                        }

            client = Client(credentials=Credentials.from_env())
            model_id = model_info[args.model_name]['model_id']

            total_tokens = 0
            for response in client.text.tokenization.create(model_id=model_id, input=prompt):
                total_tokens = response.results[0].token_count
            
            if total_tokens > model_info[args.model_name]['total']:
                schema_data['classes'][class_][f'{fragment}s'][fragment_]['translation_status'] = 'token_limit_exceeded'
                schema_data['classes'][class_][f'{fragment}s'][fragment_]['syntactical_validation_status'] = 'pending'
                schema_data['classes'][class_][f'{fragment}s'][fragment_]['test_validation_status'] = 'pending'
                schema_data['classes'][class_][f'{fragment}s'][fragment_]['graal_validation_status'] = 'pending'
                schema_data['classes'][class_][f'{fragment}s'][fragment_]['elapsed_time'] = time.time() - start_time
                schema_data['classes'][class_][f'{fragment}s'][fragment_]['generation_timestamp'] = datetime.datetime.now().isoformat()
                schema_data['classes'][class_][f'{fragment}s'][fragment_]['model_name'] = args.model_name
                schema_data['classes'][class_][f'{fragment}s'][fragment_]['include_implementation'] = args.include_implementation
                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{schema}', 'w') as f:
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

            print(generation, flush=True)
            print('---' * 50, flush=True)

            status, parsed_fragment, feedback = l0_validation(generation, fragment)

            if not status:
                max_attempts += 1
                # TODO: create feedback prompt
                # prompt = create_feedback_prompt(feedback, project_name, schema, class_, fragment_, parsed_fragment, args)
                continue
            
            schema_data['classes'][class_][f'{fragment}s'][fragment_]['translation'] = parsed_fragment
            schema_data['classes'][class_][f'{fragment}s'][fragment_]['translation_status'] = 'success' if fragment == 'field' or 'src.test' in schema else 'pending'
            schema_data['classes'][class_][f'{fragment}s'][fragment_]['syntactical_validation_status'] = 'success'
            schema_data['classes'][class_][f'{fragment}s'][fragment_]['test_validation_status'] = 'pending'
            schema_data['classes'][class_][f'{fragment}s'][fragment_]['graal_validation_status'] = 'pending'
            schema_data['classes'][class_][f'{fragment}s'][fragment_]['elapsed_time'] = time.time() - start_time
            schema_data['classes'][class_][f'{fragment}s'][fragment_]['generation_timestamp'] = datetime.datetime.now().isoformat()
            schema_data['classes'][class_][f'{fragment}s'][fragment_]['model_name'] = args.model_name
            schema_data['classes'][class_][f'{fragment}s'][fragment_]['include_implementation'] = args.include_implementation

            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{schema}', 'w') as f:
                json.dump(schema_data, f, indent=4)
                f.flush()
                os.fsync(f.fileno())

            if fragment == 'field' or 'src.test' in schema: # do not proceed to semantic validation for fields and test methods
                translated_fragment = True
                break

            if args.validate_by_graal:
                status, _, feedback = l2_validation([[parsed_fragment, schema, class_, fragment_, args]])

                if status == "failure":
                    schema_data['classes'][class_][f'{fragment}s'][fragment_]['translation_status'] = 'failed'
                    schema_data['classes'][class_][f'{fragment}s'][fragment_]['graal_validation_status'] = 'failed'
                    schema_data['classes'][class_][f'{fragment}s'][fragment_]['elapsed_time'] = time.time() - start_time
                    schema_data['classes'][class_][f'{fragment}s'][fragment_]['generation_timestamp'] = datetime.datetime.now().isoformat()

                    with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{schema}', 'w') as f:
                        json.dump(schema_data, f, indent=4)
                        f.flush()
                        os.fsync(f.fileno())

                    #TODO: create new prompt with feedback
                    max_attempts += 1
                    break
                    continue

                elif status == "success":
                    schema_data['classes'][class_][f'{fragment}s'][fragment_]['translation_status'] = 'success'
                    schema_data['classes'][class_][f'{fragment}s'][fragment_]['graal_validation_status'] = 'success'
                    schema_data['classes'][class_][f'{fragment}s'][fragment_]['elapsed_time'] = time.time() - start_time
                    schema_data['classes'][class_][f'{fragment}s'][fragment_]['generation_timestamp'] = datetime.datetime.now().isoformat()

                    with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{schema}', 'w') as f:
                        json.dump(schema_data, f, indent=4)
                        f.flush()
                        os.fsync(f.fileno())
                    
                    translated_fragment = True
                    break

                elif status == "error":
                    schema_data['classes'][class_][f'{fragment}s'][fragment_]['translation_status'] = 'failed'
                    schema_data['classes'][class_][f'{fragment}s'][fragment_]['graal_validation_status'] = 'error'
                    schema_data['classes'][class_][f'{fragment}s'][fragment_]['elapsed_time'] = time.time() - start_time
                    schema_data['classes'][class_][f'{fragment}s'][fragment_]['generation_timestamp'] = datetime.datetime.now().isoformat()

                    with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{schema}', 'w') as f:
                        json.dump(schema_data, f, indent=4)
                        f.flush()
                        os.fsync(f.fileno())
                    
                    translated_fragment = True
                    break

            elif args.validate_by_test:
                status, feedback, file_path, function_name, is_attr_error = l1_validation(schema, class_, fragment_, project_name, processed_fragments, args.model_name, args.prompt_type)

                if not status:

                    if not is_attr_error:
                        schema_data['classes'][class_][f'{fragment}s'][fragment_]['translation_status'] = 'failed'
                        schema_data['classes'][class_][f'{fragment}s'][fragment_]['reprompt_attempt'] = f'not_attribute_error: {feedback}'

                        with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{schema}', 'w') as f:
                            json.dump(schema_data, f, indent=4)
                            f.flush()
                            os.fsync(f.fileno())

                        break # breaking the loop because the issue is not an attribute error and cant be fixed with re-prompting
                    
                    else:

                        incorrect_schema, incorrect_class_, incorrect_fragment_ = get_incorrect_fragment(file_path, project_name, function_name)

                        assert incorrect_schema is not None, f"Could not find incorrect fragment for {file_path} {function_name}"
                        assert incorrect_class_ is not None, f"Could not find incorrect fragment for {file_path} {function_name}"
                        assert incorrect_fragment_ is not None, f"Could not find incorrect fragment for {file_path} {function_name}"

                        schema_data = {}
                        with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{incorrect_schema}', 'r') as f:
                            schema_data = json.load(f)
                        
                        schema_data['classes'][incorrect_class_][f'{fragment}s'][incorrect_fragment_]['translation_status'] = 'failed'
                        schema_data['classes'][incorrect_class_][f'{fragment}s'][incorrect_fragment_]['reprompt_attempt'] = 'attribute_error'

                        with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{incorrect_schema}', 'w') as f:
                            json.dump(schema_data, f, indent=4)
                            f.flush()
                            os.fsync(f.fileno())

                        if f'{incorrect_schema.replace("_python_partial.json", "")}|{incorrect_class_}|{incorrect_fragment_}' != f'{schema.replace("_python_partial.json", "")}|{class_}|{fragment_}':
                            schema = incorrect_schema
                            class_ = incorrect_class_
                            fragment_ = incorrect_fragment_
                            fixing_same_fragment = False

                    max_attempts += 1
                    ### TODO: create new prompt with feedback
                    prompt = create_feedback_prompt(feedback, project_name, schema, class_, fragment_, parsed_fragment, args)

                    continue
                
                schema_data['classes'][class_][f'{fragment}s'][fragment_]['translation_status'] = 'success'
                schema_data['classes'][class_][f'{fragment}s'][fragment_]['test_validation_status'] = 'success'
                schema_data['classes'][class_][f'{fragment}s'][fragment_]['elapsed_time'] = time.time() - start_time
                schema_data['classes'][class_][f'{fragment}s'][fragment_]['generation_timestamp'] = datetime.datetime.now().isoformat()

                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{schema}', 'w') as f:
                    json.dump(schema_data, f, indent=4)
                    f.flush()
                    os.fsync(f.fileno())
                
                feedback = ''

                if not fixing_same_fragment:
                    schema, class_, fragment_ = original_schema, original_class, original_fragment
                    fixing_same_fragment = True
                    continue

                translated_fragment = True
                break

        if not translated_fragment:
            schema_data = {}
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{original_schema}', 'r') as f:
                schema_data = json.load(f)

            schema_data['classes'][original_class][f'{fragment}s'][original_fragment]['translation_status'] = 'failed'

            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{original_schema}', 'w') as f:
                json.dump(schema_data, f, indent=4)
                f.flush()
                os.fsync(f.fileno())


def main(args):

    args.prompt_type = 'body' if args.include_implementation else 'signature'

    fragment_traversal = get_traversal(args)

    for fragment in fragment_traversal:

        prompt_gen = PromptGenerator(is_feedback=False, args=args, fragment_details=fragment)
        prompt = prompt_gen.generate_prompt()
        prompt_status = prompt_gen.prompt_status


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
    args = parser_.parse_args()
    main(args)
