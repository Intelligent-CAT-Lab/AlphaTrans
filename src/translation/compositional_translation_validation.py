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

from genai.client import Client
from genai.credentials import Credentials
from genai.schema import (
    DecodingMethod,
    TextGenerationParameters,
    TextGenerationReturnOptions,
)


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

            token_limits = {
                                'deepseek-coder-33b-instruct': {'total': 16384, 'max_new_tokens': 4096},
                                'granite-34b-code-instruct': {'total': 8192, 'max_new_tokens': 1024},
                                'llama-3-70b-instruct': {'total': 8192, 'max_new_tokens': 2048},
                            }

            if use_bam:
                client = Client(credentials=Credentials.from_env())
                model_id = ""
                if args.model_name == 'deepseek-coder-33b-instruct':
                    model_id = "deepseek-ai/deepseek-coder-33b-instruct"
                elif args.model_name == 'granite-34b-code-instruct':
                    model_id = "ibm/granite-34b-code-instruct"

                total_tokens = 0
                for response in client.text.tokenization.create(model_id=model_id, input=prompt):
                    total_tokens = response.results[0].token_count
                
                if total_tokens > token_limits[args.model_name]['total']:
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

                max_new_tokens = token_limits[args.model_name]['total'] - total_tokens
                max_new_tokens = min(max_new_tokens, token_limits[args.model_name]['max_new_tokens'])

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
            
            elif args.use_vela:
                headers = {"Content-Type": "application/json"}
                vela_url = os.getenv("VELA_URL")

                client = Client(credentials=Credentials.from_env())
                model_id = ""
                if args.model_name == 'deepseek-coder-33b-instruct':
                    model_id = "deepseek-ai/deepseek-coder-33b-instruct"
                elif args.model_name == 'granite-34b-code-instruct':
                    model_id = "ibm/granite-34b-code-instruct"
                elif args.model_name == 'llama-3-70b-instruct':
                    model_id = "meta-llama/llama-3-70b-instruct"

                total_tokens = 0
                for response in client.text.tokenization.create(model_id=model_id, input=prompt):
                    total_tokens = response.results[0].token_count

                if total_tokens > token_limits[args.model_name]['total']:
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

                max_new_tokens = token_limits[args.model_name]['total'] - total_tokens
                max_new_tokens = min(max_new_tokens, token_limits[args.model_name]['max_new_tokens'])

                try:
                    response = requests.post(
                                                vela_url,
                                                headers=headers,
                                                json={
                                                        'prompt': prompt,
                                                        'model': "meta-llama/Meta-Llama-3-70B",
                                                        'max_tokens': max_new_tokens,
                                                        'temperature': 0
                                                    }
                                        )

                    response.raise_for_status()
                    result = response.json()

                    generated_text = result.get('choices', '')[0]['text']
                    generation = prompt + generated_text
                
                except Exception as e:
                    print(f"Error: {e}")
                    exit()

            else:

                input_tokens = tokenizer.encode(prompt, return_tensors="pt").to(device)

                if input_tokens.shape[1] > token_limits[args.model_name]['total']:
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

                max_new_tokens = token_limits[args.model_name]['total'] - input_tokens.shape[1]
                max_new_tokens = min(max_new_tokens, token_limits[args.model_name]['max_new_tokens'])

                raw_output = model.generate(
                    input_tokens,
                    max_new_tokens=max_new_tokens,
                    do_sample=False,
                    output_scores=True,
                    return_dict_in_generate=True,
                    pad_token_id=tokenizer.eos_token_id,
                )

                generation = tokenizer.decode(raw_output.sequences[0], skip_special_tokens=True)

            model_response = ''
            if args.model_name == 'deepseek-coder-33b-instruct':
                model_response = '### Response:'
            elif args.model_name == 'granite-34b-code-instruct':
                model_response = 'Answer:'

            generation = generation[generation.find(model_response) + len(model_response):]

            print(generation, flush=True)
            print('---' * 50, flush=True)

            status, parsed_fragment, feedback = l0_validation(generation, fragment)

            if not status:
                max_attempts += 1
                ### TODO: create new prompt with feedback
                # prompt = ...
                continue
            
            schema_data['classes'][class_][f'{fragment}s'][fragment_]['translation'] = parsed_fragment
            # schema_data['classes'][class_][f'{fragment}s'][fragment_]['translation_status'] = 'success' if fragment == 'field' or 'src.test' in schema else 'pending'
            schema_data['classes'][class_][f'{fragment}s'][fragment_]['translation_status'] = 'success'
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

            translated_fragment = True
            break # remove this later

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
                status, feedback, file_path, function_name = l1_validation(schema, class_, fragment_, project_name, processed_fragments)

                if not status:
                    incorrect_schema, incorrect_class_, incorrect_fragment_ = get_incorrect_fragment(file_path, project_name, function_name)
                    assert incorrect_schema is not None, f"Could not find incorrect fragment for {file_path} {function_name}"
                    assert incorrect_class_ is not None, f"Could not find incorrect fragment for {file_path} {function_name}"
                    assert incorrect_fragment_ is not None, f"Could not find incorrect fragment for {file_path} {function_name}"

                    schema_data = {}
                    with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{incorrect_schema}', 'r') as f:
                        schema_data = json.load(f)
                    
                    schema_data['classes'][incorrect_class_][f'{fragment}s'][incorrect_fragment_]['translation_status'] = 'failed'

                    with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{incorrect_schema}', 'w') as f:
                        json.dump(schema_data, f, indent=4)
                        f.flush()
                        os.fsync(f.fileno())

                    if incorrect_schema != schema and incorrect_class_ != class_ and incorrect_fragment_ != fragment_:
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
                        

def get_incorrect_fragment(file_path, project_name, method_name):
    file_path = file_path[file_path.find(project_name):]
    incorrect_schema_name = file_path.replace('/', '.').replace('.py', '_python_partial.json')

    schema_data = {}
    with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{incorrect_schema_name}', 'r') as f:
        schema_data = json.load(f)
    
    for class_ in schema_data['classes']:
        if 'new' in class_ or '{' in class_: # skip nested and nameless classes
            continue

        for method_ in schema_data['classes'][class_]['methods']:
            if method_.split(':')[1] == method_name:
                return incorrect_schema_name, class_, method_

    return None, None, None


def create_feedback_prompt(feedback, project_name, schema, class_, fragment_, incorrect_translation, args):
    persona = f"You are an AI programming assistant, utilizing the DeepSeek Coder model, developed by DeepSeek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer."

    icl = "Java code:\n```\npublic class Calculator {\n    public int add(int a, int b) {\n        return a + b;\n    }\n}\n```" + "\n\nIncorrect Python translation:\n```\nclass Calculator:\n    def add(self, a: int, b: int) -> int:\n        return a + c\n```\n\nExecution feedback:\n```\n  File \"script.py\", line 5, in add\n    return a + c\nNameError: name 'c' is not defined\n```\n\nPartial Python translation:\n```\nclass Calculator:\n    def add(self, a: int, b: int) -> int:\n        pass\n```\n\nPython method translation:\n```\n    def add(self, a: int, b: int) -> int:\n        return a + b\n```\n"

    data = {}
    with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{project_name}/{schema}', 'r') as f:
        data = json.load(f)

    original_fragment = f"class {class_}" + " {\n"
    for field in data['classes'][class_]['fields']:
        if field == fragment_:
            continue
        original_fragment += ''.join(data['classes'][class_]['fields'][field]['body'])
    
    original_fragment += '\n'

    for method in data['classes'][class_]['methods']:
        if method == fragment_:
            continue
        if method.split(':')[1] in ''.join(data['classes'][class_]['methods'][fragment_]['body']):
            original_fragment += '\n'.join([f"    @{x}" for x in data['classes'][class_]['methods'][method]['annotations'] if x.startswith('Test')]).rstrip() + '\n'
            original_fragment += ''.join(data['classes'][class_]['methods'][method]['body']).split('{')[0].rstrip() + ' {}\n'

    original_fragment += '\n'

    original_fragment += '\n'.join([f"    @{x}" for x in data['classes'][class_]['methods'][fragment_]['annotations'] if x.startswith('Test')]) + '\n'
    original_fragment += ''.join(data['classes'][class_]['methods'][fragment_]['body'])
    original_fragment += '\n}\n'

    instruction = f'### Instruction:\nTranslate the following Java method to Python 3.10 like the example above. You only need to translate the \"{fragment_.split(":")[1]}\" method. All necessary dependencies are available in partial Python translation. A feedback is provided after executing your recent incorrect translation.\n\n'

    instruction += f"{args.from_lang} code:\n```\n{original_fragment}\n```"

    incorrect_translation = data['classes'][class_]['methods'][fragment_]['translation'] if data['classes'][class_]['methods'][fragment_]['translation'] != [] else incorrect_translation

    instruction += f'\n\nIncorrect Python translation:\n```\nclass {class_}:\n' + '\n'.join(incorrect_translation) + '\n```\n\nExecution feedback:\n```\n' + feedback + '\n```\n\nPartial Python translation:\n```\n'
    instruction += '\n'.join(data['python_imports'])
    instruction += '\n\n'
    instruction += data['classes'][class_]['python_class_declaration']

    related_fields = []
    for field in data['classes'][class_]['fields']:
        if field.split(':')[1] in original_fragment:
            related_fields.append(field)
    
    for related_field in related_fields:
        instruction += '\n'.join(data['classes'][class_]['fields'][related_field]['translation']).rstrip() + '\n' if data['classes'][class_]['fields'][related_field]['translation'] != [] else ''.join(data['classes'][class_]['fields'][related_field]['partial_translation']).replace('<placeholder>', 'None').rstrip() + '\n'
    
    related_methods = []
    for method in data['classes'][class_]['methods']:
        if method.split(':')[1] in original_fragment and method != fragment_:
            related_methods.append(method)
    
    if args.include_implementation:
        for related_method in related_methods:
            instruction += '\n'.join(data['classes'][class_]['methods'][related_method]['translation']).rstrip() if data['classes'][class_]['methods'][related_method]['translation'] != [] else ''.join(data['classes'][class_]['methods'][related_method]['partial_translation']).rstrip()
            instruction += '\n\n'
    else:
        for related_method in related_methods:
            instruction += ''.join(data['classes'][class_]['methods'][related_method]['partial_translation']).rstrip()
            instruction += '\n\n'

    instruction += ''.join(data['classes'][class_]['methods'][fragment_]['partial_translation']).rstrip()
    instruction += '\n```\n\n### Response:\n'
    instruction += f'Python method translation:\n'
    instruction += '```\n'
    instruction += ''.join(data['classes'][class_]['methods'][fragment_]['partial_translation']).rstrip().replace('pass', '')

    return f"{persona}\n\n{icl}\n{instruction}"


def generate_prompt(data, schema, class_, fragment_, args, fragment_type, model):

    persona = ""
    if args.model_name == 'deepseek-coder-33b-instruct':
        persona = f"You are an AI programming assistant, utilizing the DeepSeek Coder model, developed by DeepSeek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer."

    icl = ''
    if fragment_type == 'field':
        icl = "Java code:\n```\npublic class Calculator {\n    public int x;\n}\n```" + "\n\nPartial Python translation:\n```\nclass Calculator:\n    x: int = \n```\n\nPython field translation:\n```\n    x: int = 0\n```\n"
    elif fragment_type in ['method', 'static_initializer']:
        icl = "Java code:\n```\npublic class Calculator {\n    public int add(int a, int b) {\n        return a + b;\n    }\n}\n```" + "\n\nPartial Python translation:\n```\nclass Calculator:\n    def add(self, a: int, b: int) -> int:\n        pass\n```\n\nPython method translation:\n```\n    def add(self, a: int, b: int) -> int:\n        return a + b\n```\n"

    original_fragment = f"class {class_}" + " {\n"
    for field in data['classes'][class_]['fields']:
        if field == fragment_:
            continue
        if field.split(':')[1] in ''.join(data['classes'][class_][fragment_type + 's'][fragment_]['body']):
            original_fragment += ''.join(data['classes'][class_]['fields'][field]['body'])
    
    original_fragment += '\n'

    if fragment_type == 'method':
        for method in data['classes'][class_]['methods']:
            if method == fragment_:
                continue
            if method.split(':')[1] in ''.join(data['classes'][class_]['methods'][fragment_]['body']):
                original_fragment += '\n'.join([f"    @{x}" for x in data['classes'][class_]['methods'][method]['annotations'] if x.startswith('Test')]).rstrip() + '\n'
                original_fragment += ''.join(data['classes'][class_]['methods'][method]['body']).split('{')[0].rstrip() + ' {}\n'

    original_fragment += '\n'

    original_fragment += '\n'.join([f"    @{x}" for x in data['classes'][class_]['methods'][fragment_]['annotations'] if x.startswith('Test')]) + '\n' if fragment_type == 'method' else ''
    original_fragment += ''.join(data['classes'][class_][f'{fragment_type}s'][fragment_]['body'])
    original_fragment += '\n}\n'

    prompt_instruction = ""
    if args.model_name == 'deepseek-coder-33b-instruct':
        prompt_instruction = "### Instruction:"
    elif args.model_name == 'granite-34b-code-instruct':
        prompt_instruction = "Question:"
    
    model_response = ""
    if args.model_name == 'deepseek-coder-33b-instruct':
        model_response = '### Response:'
    elif args.model_name == 'granite-34b-code-instruct':
        model_response = 'Answer:'

    instruction = f'{prompt_instruction}\nTranslate the following {args.from_lang} {fragment_type} to {args.to_lang} 3.10 like the example above. You only need to translate the \"{fragment_.split(":")[1]}\" {fragment_type}. All necessary dependencies are available in partial {args.to_lang} translation.\n\n'
    instruction += f"{args.from_lang} code:\n```\n{original_fragment}\n```"

    instruction += f'\n\nPartial {args.to_lang} translation:\n```\n'
    instruction += '\n'.join(data['python_imports'])
    instruction += '\n\n'

    nested_classes = data['classes'][class_]['nests']
    for nested_class_ in nested_classes:
        if 'new' in nested_class_ or '{' in nested_class_:
            continue
        instruction += f"\n\nclass {nested_class_}:\n"
        for field in data['classes'][nested_class_]['fields']:
            instruction += '\n'.join(data['classes'][nested_class_]['fields'][field]['translation']) + '\n' if data['classes'][nested_class_]['fields'][field]['translation'] != [] else ''.join(data['classes'][nested_class_]['fields'][field]['partial_translation']).replace('<placeholder>', 'None') + '\n'

    main_class_decl = data['classes'][class_]['python_class_declaration']

    if fragment_type == 'field':

        if '<placeholder>' not in ''.join(data['classes'][class_]['fields'][fragment_]['partial_translation']):
            return None

        related_fields = []
        for field in data['classes'][class_]['fields']:
            if field.split(':')[1] == fragment_.split(':')[1]:
                continue
            if '=' not in ''.join(data['classes'][class_]['fields'][field]['body']):
                continue
            if field.split(':')[1] in ''.join(''.join(data['classes'][class_]['fields'][fragment_]['body']).split('=')[1:]).strip():
                related_fields.append(field)
        
        for related_field in related_fields:
            if related_field == fragment_:
                continue
            main_class_decl += '\n'.join(data['classes'][class_]['fields'][related_field]['translation']) + '\n' if data['classes'][class_]['fields'][related_field]['translation'] != [] else ''.join(data['classes'][class_]['fields'][related_field]['partial_translation']).replace('<placeholder>', 'None') + '\n'

        related_methods = []
        for method in data['classes'][class_]['methods']:
            if method.split(':')[1] in ''.join(data['classes'][class_]['fields'][fragment_]['body']):
                related_methods.append(method)
        
        for related_method in related_methods:
            if args.include_implementation:
                main_class_decl += '\n'.join(data['classes'][class_]['methods'][related_method]['translation']).rstrip() if data['classes'][class_]['methods'][related_method]['translation'] != [] else ''.join(data['classes'][class_]['methods'][related_method]['partial_translation']).rstrip()
            else:
                main_class_decl += ''.join(data['classes'][class_]['methods'][related_method]['partial_translation'])

        main_class_decl += ''.join(data['classes'][class_]['fields'][fragment_]['partial_translation']).replace('<placeholder>', '') + '\n'
        main_class_decl += f'\n```\n\n{model_response}\n'
        main_class_decl += f'Python field translation:\n'
        instruction += main_class_decl

    elif fragment_type == 'method':

        # include fields of superclass
        for super_class in data['classes'][class_]['extends']:
            super_class_schema = ''
            for schema_file in os.listdir(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}'):
                if f'.{super_class}_python_partial.json' in schema_file:
                    super_class_schema = schema_file
                    break
            
            if super_class_schema == '':
                continue

            super_class_data = {}
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{super_class_schema}', 'r') as f:
                super_class_data = json.load(f)

            instruction += super_class_data['classes'][super_class]['python_class_declaration']
            for field in super_class_data['classes'][super_class]['fields']:
                instruction += '\n'.join(super_class_data['classes'][super_class]['fields'][field]['translation']) + '\n' if super_class_data['classes'][super_class]['fields'][field]['translation'] != [] else ''.join(super_class_data['classes'][super_class]['fields'][field]['partial_translation']).replace('<placeholder>', 'None') + '\n'

        # include related fields
        related_fields = []
        for field in data['classes'][class_]['fields']:
            if field.split(':')[1] in ''.join(data['classes'][class_]['methods'][fragment_]['body']):
                related_fields.append(field)

        for related_field in related_fields:
            main_class_decl += '\n'.join(data['classes'][class_]['fields'][related_field]['translation']) + '\n' if data['classes'][class_]['fields'][related_field]['translation'] != [] else ''.join(data['classes'][class_]['fields'][related_field]['partial_translation']).replace('<placeholder>', 'None') + '\n'

        main_class_decl += '\n'

        for method in data['classes'][class_]['methods']:
            if ('setUp' in method or 'tearDown' in method) and 'Test' in [x.split('(')[0] for x in data['classes'][class_]['methods'][fragment_]['annotations']]:
                main_class_decl += '\n'.join(data['classes'][class_]['methods'][method]['translation']).rstrip() if data['classes'][class_]['methods'][method]['translation'] != [] else ''.join(data['classes'][class_]['methods'][method]['partial_translation']).rstrip()

        if len(data['classes'][class_]['methods'][fragment_]['calls']) != 0 and args.include_call_graph:

            out_of_file_dependencies = []
            out_of_class_dependencies = []
            for callee_schema, callee_class, callee_method in data['classes'][class_]['methods'][fragment_]['calls']:
                callee_schema_data = {}
                with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{callee_schema}_python_partial.json', 'r') as f:
                    callee_schema_data = json.load(f)
                
                if ':' not in callee_method:
                    continue

                if callee_schema != schema.replace('_python_partial.json', ''):
                    out_of_file_dependencies.append((callee_schema, callee_class, callee_method))
                    continue

                if callee_class != class_:
                    out_of_class_dependencies.append((callee_schema, callee_class, callee_method))
                    continue

                if args.include_implementation:
                    callee_partial_translation = '\n'.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['translation']).rstrip() if callee_schema_data['classes'][callee_class]['methods'][callee_method]['translation'] != [] else ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation']).rstrip()
                else:
                    callee_partial_translation = ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation']).rstrip()
                main_class_decl += f"\n\n{callee_partial_translation}\n\n"

            main_class_decl += '\n'
            main_class_decl += ''.join(data['classes'][class_]['methods'][fragment_]['partial_translation']).rstrip()

            if len(out_of_file_dependencies) != 0:
                ordered_out_of_file_dependencies = {}
                for callee_schema, callee_class, callee_method in out_of_file_dependencies:
                    ordered_out_of_file_dependencies.setdefault(callee_schema, [])
                    ordered_out_of_file_dependencies[callee_schema].append((callee_class, callee_method))

                for callee_schema in ordered_out_of_file_dependencies:
                    for callee_class, callee_method in ordered_out_of_file_dependencies[callee_schema]:

                        callee_schema_data = {}
                        with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{callee_schema}_python_partial.json', 'r') as f:
                            callee_schema_data = json.load(f)
                        
                        if f'class {callee_class}:' not in instruction:
                            instruction += f"\n\nclass {callee_class}:\n"
                            for field in callee_schema_data['classes'][callee_class]['fields']:
                                instruction += '\n'.join(callee_schema_data['classes'][callee_class]['fields'][field]['translation']) + '\n' if callee_schema_data['classes'][callee_class]['fields'][field]['translation'] != [] else ''.join(callee_schema_data['classes'][callee_class]['fields'][field]['partial_translation']).replace('<placeholder>', 'None') + '\n'

                        if args.include_implementation:
                            instruction += '\n'.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['translation']) if callee_schema_data['classes'][callee_class]['methods'][callee_method]['translation'] != [] else f"\nclass {callee_class}:\n" + ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation'])
                        else:
                            instruction += ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation'])

            if len(out_of_class_dependencies) != 0:
                ordered_out_of_file_dependencies = {}
                for callee_schema, callee_class, callee_method in out_of_class_dependencies:
                    ordered_out_of_file_dependencies.setdefault(callee_schema, [])
                    ordered_out_of_file_dependencies[callee_schema].append((callee_class, callee_method))

                for callee_schema in ordered_out_of_file_dependencies:
                    for callee_class, callee_method in ordered_out_of_file_dependencies[callee_schema]:
                        callee_schema_data = {}
                        with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{callee_schema}_python_partial.json', 'r') as f:
                            callee_schema_data = json.load(f)
                        
                        instruction += f"\n\nclass {callee_class}:\n"
                        for field in callee_schema_data['classes'][callee_class]['fields']:
                            instruction += '\n'.join(callee_schema_data['classes'][callee_class]['fields'][field]['translation']) + '\n' if callee_schema_data['classes'][callee_class]['fields'][field]['translation'] != [] else ''.join(callee_schema_data['classes'][callee_class]['fields'][field]['partial_translation']).replace('<placeholder>', 'None') + '\n'
                        
                        if args.include_implementation:
                            instruction += '\n'.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['translation']) if callee_schema_data['classes'][callee_class]['methods'][callee_method]['translation'] != None else f"\nclass {callee_class}:\n" + ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation'])
                        else:
                            instruction += ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation'])
                    
            instruction += '\n\n' + main_class_decl + '\n\n'
            
        else:
            main_class_decl += '\n'
            main_class_decl += ''.join(data['classes'][class_]['methods'][fragment_]['partial_translation']).rstrip()
            instruction += '\n\n' + main_class_decl + '\n\n'
        
        instruction += f'\n```\n\n{model_response}\n'
        instruction += f'Python method translation:\n'
        instruction += '```\n'
        instruction += ''.join(data['classes'][class_]['methods'][fragment_]['partial_translation']).rstrip().replace('    pass', '    ')
    
    elif fragment_type == 'static_initializer':

        # include fields of superclass
        for super_class in data['classes'][class_]['extends']:
            super_class_schema = ''
            for schema_file in os.listdir(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}'):
                if f'{super_class}_python_partial.json' in schema_file:
                    super_class_schema = schema_file
                    break
            
            if super_class_schema == '':
                continue

            super_class_data = {}
            with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{super_class_schema}', 'r') as f:
                super_class_data = json.load(f)
            
            instruction += super_class_data['classes'][super_class]['python_class_declaration']
            for field in super_class_data['classes'][super_class]['fields']:
                instruction += '\n'.join(super_class_data['classes'][super_class]['fields'][field]['translation']) + '\n' if super_class_data['classes'][super_class]['fields'][field]['translation'] != [] else ''.join(super_class_data['classes'][super_class]['fields'][field]['partial_translation']).replace('<placeholder>', 'None') + '\n'

        # include related fields
        related_fields = []
        for field in data['classes'][class_]['fields']:
            if field.split(':')[1] in original_fragment:
                related_fields.append(field)

        for related_field in related_fields:
            main_class_decl += '\n'.join(data['classes'][class_]['fields'][related_field]['translation']) + '\n' if data['classes'][class_]['fields'][related_field]['translation'] != [] else ''.join(data['classes'][class_]['fields'][related_field]['partial_translation']).replace('<placeholder>', 'None') + '\n'
        
        main_class_decl += '\n'

        related_methods = []
        for method in data['classes'][class_]['methods']:
            if method.split(':')[1] in original_fragment:
                related_methods.append(method)
        
        for related_method in related_methods:
            if args.include_implementation:
                main_class_decl += '\n'.join(data['classes'][class_]['methods'][related_method]['translation']).rstrip() if data['classes'][class_]['methods'][related_method]['translation'] != [] else ''.join(data['classes'][class_]['methods'][related_method]['partial_translation']).rstrip()
            else:
                main_class_decl += ''.join(data['classes'][class_]['methods'][related_method]['partial_translation']).rstrip()
            main_class_decl += '\n\n'

        main_class_decl += '    @staticmethod\n    def run_static_init():\n        pass'

        instruction += '\n\n' + main_class_decl + '\n\n'
        instruction += f'\n```\n\n{model_response}\n'
        instruction += f'Python method translation:\n'
        instruction += '```\n'
        instruction += '    @staticmethod\n    def run_static_init():\n        '

    prompt = f"{persona}\n\n{icl}\n{instruction}"

    # replace the null char in the prompt
    prompt = prompt.replace('\u0000', '')

    return prompt


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
    assert len(aligned_schemas) == len(schemas), f"Found less schemas than expected: {aligned_schemas}"

    return aligned_schemas


def main(args):
    device = 'cuda' if torch.cuda.is_available() and args.use_cuda else 'cpu'
    tokenizer, model = None, None

    args.prompt_type = 'body' if args.include_implementation else 'signature'

    if args.model_name == 'deepseek-coder-33b-instruct' and not args.use_bam:
        kwargs = {}
        kwargs["torch_dtype"] = torch.float16
        tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-33b-instruct", cache_dir=args.cache_dir)
        model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-33b-instruct", cache_dir=args.cache_dir, device_map='auto', **kwargs)

    schemas = os.listdir(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}')

    traversal = {}
    with open(f'data/dependencies/{args.project_name}/traversal.json', 'r') as f:
        traversal = json.load(f)
    
    traversal_order = list(traversal.values())

    schemas = align_schema_order(schemas, traversal_order)

    for schema in schemas:

        path_ = f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{schema}'
        with open(path_, 'r') as f:
            data = json.load(f)

        for class_ in data['classes']:

            if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                continue

            print(f'Translating fields of class {class_} @ schema {schema}...', flush=True)

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

            pbar = tqdm.tqdm(field_order)
            for field_ in pbar:
                pbar.update()
                pbar.set_description(f"Translating field {field_} in class {class_} @ schema {schema}...")

                if data['classes'][class_]['fields'][field_]['translation_status'] == 'failed':
                    continue

                if data['classes'][class_]['fields'][field_]['translation_status'] == 'success':
                    continue

                prompt = generate_prompt(data, schema, class_, field_, args, 'field', args.model_name)

                if prompt is None:
                    data['classes'][class_]['fields'][field_]['translation'] = data['classes'][class_]['fields'][field_]['partial_translation']
                    data['classes'][class_]['fields'][field_]['elapsed_time'] = 0
                    data['classes'][class_]['fields'][field_]['generation_timestamp'] = datetime.datetime.now().isoformat()
                    data['classes'][class_]['fields'][field_]['translation_status'] = 'success'
                    data['classes'][class_]['fields'][field_]['syntactical_validation_status'] = 'success'
                    data['classes'][class_]['fields'][field_]['test_validation_status'] = 'pending'
                    data['classes'][class_]['fields'][field_]['graal_validation_status'] = 'pending'
                    data['classes'][class_]['fields'][field_]['model_name'] = args.model_name
                    data['classes'][class_]['fields'][field_]['include_implementation'] = args.include_implementation

                    with open(f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{schema}', 'w') as f:
                        json.dump(data, f, indent=4)
                        f.flush()
                        os.fsync(f.fileno())

                    continue

                translate(model, tokenizer, device, [{'prompt': prompt, 'fragment_type': 'field', 'use_bam': args.use_bam, 'project_name': args.project_name, 'schema': schema, 'class': class_, 'fragment': field_}], [], args)

            if 'static_initializers' not in data['classes'][class_]:
                continue

            print(f'Translating static initializers of class {class_} @ schema {schema}...', flush=True)

            pbar = tqdm.tqdm(data['classes'][class_]['static_initializers'])
            assert 1 == len(data['classes'][class_]['static_initializers']), f"Found more than one static initializer for class {class_} @ schema {schema}"
            
            for static_initializer in pbar:
                pbar.update()
                pbar.set_description(f"Translating static initializer {static_initializer} in class {class_} @ schema {schema}...")

                if data['classes'][class_]['static_initializers'][static_initializer]['translation_status'] == 'failed':
                    continue

                if data['classes'][class_]['static_initializers'][static_initializer]['translation_status'] == 'success':
                    continue

                prompt = generate_prompt(data, schema, class_, static_initializer, args, 'static_initializer', args.model_name)

                translate(model, tokenizer, device, [{'prompt': prompt, 'fragment_type': 'static_initializer', 'use_bam': args.use_bam, 'project_name': args.project_name, 'schema': schema, 'class': class_, 'fragment': static_initializer}], [], args)

    waiting_queue = {}
    processed_fragments = []
    for schema in schemas:

        path_ = f'data/schemas/translations/{args.model_name}/{args.prompt_type}/{args.project_name}/{schema}'
        with open(path_, 'r') as f:
            data = json.load(f)

        class_order = []
        while len(class_order) != len(data['classes']):
            for class_ in data['classes']:
                if class_ in class_order:
                    continue

                if not set(data['classes'][class_]['extends']).issubset(set(class_order)) and all([x in data['classes'].keys() for x in data['classes'][class_]['extends']]):
                    continue
                
                if not set(data['classes'][class_]['implements']).issubset(set(class_order)) and all([x in data['classes'].keys() for x in data['classes'][class_]['implements']]):
                    continue                                                                                                                       
                
                if data['classes'][class_]['nests'] == []:
                    class_order.append(class_)
                    continue

                if all([x in class_order for x in data['classes'][class_]['nests']]):
                    class_order.append(class_)
        
        for class_ in class_order:

            if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                continue

            print(f'Translating methods of class {class_} @ schema {schema}...', flush=True)
            
            pbar = tqdm.tqdm(data['classes'][class_]['methods'])
            for method_ in pbar:
                pbar.update()
                pbar.set_description(f"Translating method {method_} in class {class_} @ schema {schema}...")

                full_fragment_name = f'{schema.replace("_python_partial.json", "")}|{class_}|{method_}'
                dependent_fragments = [f'{x[0]}|{x[1]}|{x[2]}' for x in data['classes'][class_]['methods'][method_]['calls'] if ':' in x[2] and full_fragment_name != f'{x[0]}|{x[1]}|{x[2]}']

                if data['classes'][class_]['methods'][method_]['translation_status'] == 'failed':
                    processed_fragments.append(full_fragment_name)
                    continue

                if data['classes'][class_]['methods'][method_]['translation_status'] == 'success':
                    processed_fragments.append(full_fragment_name)
                    continue

                if any([x not in processed_fragments for x in dependent_fragments]):
                    waiting_queue[full_fragment_name] = [dependent_fragments, data.copy(), schema, class_, method_, 'method', args]
                    continue

                prompt = generate_prompt(data, schema, class_, method_, args, 'method', args.model_name)

                translate(model, tokenizer, device, [{'prompt': prompt, 'fragment_type': 'method', 'use_bam': args.use_bam, 'project_name': args.project_name, 'schema': schema, 'class': class_, 'fragment': method_}], processed_fragments, args)

                processed_fragments.append(full_fragment_name)
                                
                # check if a waiting fragment is now ready to be processed
                for waiting_fragment in list(waiting_queue.keys()):
                    waiting_dependent_fragments = [x for x in waiting_queue[waiting_fragment][0]]
                    if all([x in processed_fragments for x in waiting_dependent_fragments]):
                        _, waiting_data, waiting_schema, waiting_class, waiting_method, waiting_fragment_type, waiting_args = waiting_queue[waiting_fragment]
                        prompt = generate_prompt(waiting_data, waiting_schema, waiting_class, waiting_method, waiting_args, waiting_fragment_type, args.model_name)

                        translate(model, tokenizer, device, [{'prompt': prompt, 'fragment_type': 'method', 'use_bam': args.use_bam, 'project_name': args.project_name, 'schema': waiting_schema, 'class': waiting_class, 'fragment': waiting_method}], processed_fragments, args)

                        processed_fragments.append(waiting_fragment)
                        del waiting_queue[waiting_fragment]

    # further checking the waiting queue to see if any fragment can be processed
    threshold = 3
    while True:
        if len(waiting_queue) == 0:
            break

        if threshold == 0:
            break

        for waiting_fragment in list(waiting_queue.keys()):
            waiting_dependent_fragments = [x for x in waiting_queue[waiting_fragment][0]]
            if all([x in processed_fragments for x in waiting_dependent_fragments]):
                _, waiting_data, waiting_schema, waiting_class, waiting_method, waiting_fragment_type, waiting_args = waiting_queue[waiting_fragment]
                prompt = generate_prompt(waiting_data, waiting_schema, waiting_class, waiting_method, waiting_args, waiting_fragment_type, args.model_name)

                translate(model, tokenizer, device, [{'prompt': prompt, 'fragment_type': 'method', 'use_bam': args.use_bam, 'project_name': args.project_name, 'schema': waiting_schema, 'class': waiting_class, 'fragment': waiting_method}], processed_fragments, args)

                processed_fragments.append(waiting_fragment)
                del waiting_queue[waiting_fragment]
                threshold = 10
        
        threshold -= 1
    
    if len(waiting_queue) == 0:
        print(f'no cycles found for project: {args.project_name}')
        return

    # finding cycles
    cycles = []
    for k in waiting_queue:
        waiting_dependent_fragments, waiting_data, waiting_schema, waiting_class, waiting_method, waiting_fragment_type, waiting_args = waiting_queue[k]

        for df in waiting_dependent_fragments:
            if df not in waiting_queue:
                continue

            if k in waiting_queue[df][0] and df in waiting_queue[k][0] and [df, k] not in cycles:
                cycles.append([k, df])

    # translating all cycles at once
    for cycle in cycles:
        for cycle_fragment in cycle:
            waiting_dependent_fragments, waiting_data, waiting_schema, waiting_class, waiting_method, waiting_fragment_type, waiting_args = waiting_queue[cycle_fragment]
            prompt = generate_prompt(waiting_data, waiting_schema, waiting_class, waiting_method, waiting_args, waiting_fragment_type, args.model_name)
        
            translate(model, tokenizer, device, [{'prompt': prompt, 'fragment_type': 'method', 'use_bam': args.use_bam, 'project_name': args.project_name, 'schema': waiting_schema, 'class': waiting_class, 'fragment': waiting_method}], processed_fragments, args)

            processed_fragments.append(cycle_fragment)
            del waiting_queue[cycle_fragment]

    # further checking the waiting queue to see if any fragment can be processed
    threshold = 3
    while True:
        if len(waiting_queue) == 0:
            break

        if threshold == 0:
            break

        for waiting_fragment in list(waiting_queue.keys()):
            waiting_dependent_fragments = [x for x in waiting_queue[waiting_fragment][0]]
            if all([x in processed_fragments for x in waiting_dependent_fragments]):
                _, waiting_data, waiting_schema, waiting_class, waiting_method, waiting_fragment_type, waiting_args = waiting_queue[waiting_fragment]
                prompt = generate_prompt(waiting_data, waiting_schema, waiting_class, waiting_method, waiting_args, waiting_fragment_type, args.model_name)

                translate(model, tokenizer, device, [{'prompt': prompt, 'fragment_type': 'method', 'use_bam': args.use_bam, 'project_name': args.project_name, 'schema': waiting_schema, 'class': waiting_class, 'fragment': waiting_method}], processed_fragments, args)

                processed_fragments.append(waiting_fragment)
                del waiting_queue[waiting_fragment]
                threshold = 10
        
        threshold -= 1

    assert len(waiting_queue) == 0, f"Found cycles in the waiting queue"


if __name__ == '__main__':
    load_dotenv()
    parser_ = argparse.ArgumentParser(description='Translate java types to python types')
    parser_.add_argument('--model_name', type=str, dest='model_name', help='model name to use for translation')
    parser_.add_argument('--project_name', type=str, dest='project_name', help='project name to translate')
    parser_.add_argument('--from_lang', type=str, dest='from_lang', help='language to translate from')
    parser_.add_argument('--to_lang', type=str, dest='to_lang', help='language to translate to')
    parser_.add_argument('--include_call_graph', action='store_true', help='include call graph in translation')
    parser_.add_argument('--include_implementation', action='store_true', help='include implementation of dependent methods')
    parser_.add_argument('--cache_dir', type=str, dest='cache_dir', help='cache directory')
    parser_.add_argument('--use_bam', action='store_true', help='use BAM for translation')
    parser_.add_argument('--use_vela', action='store_true', help='use Vela for translation')
    parser_.add_argument('--use_cuda', action='store_true', help='use cuda for translation')
    parser_.add_argument('--validate_by_graal', action='store_true', help='validate translation by GraalVM')
    parser_.add_argument('--validate_by_test', action='store_true', help='validate translation by test cases')
    args = parser_.parse_args()
    main(args)
