import argparse
import json
from dotenv import load_dotenv
import torch
import tqdm
import os
import time
import datetime
from transformers import AutoTokenizer, AutoModelForCausalLM
from syntactic_validation import l0_validation

from genai.client import Client
from genai.credentials import Credentials
from genai.schema import (
    DecodingMethod,
    TextGenerationParameters,
    TextGenerationReturnOptions,
)


def translate(model, tokenizer, prompt, device, fragment, args):
    max_attempts = 0
    parsed_fragment = None
    feedback = ''
    start_time = time.time()
    while max_attempts < 5:

        print(prompt, flush=True)
        print('=======================GENERATING=======================', flush=True)

        if args.use_bam:
            client = Client(credentials=Credentials.from_env())
            model_id = "deepseek-ai/deepseek-coder-33b-instruct"

            total_tokens = 0
            for response in client.text.tokenization.create(model_id=model_id, input=prompt):
                total_tokens = response.results[0].token_count
            
            if total_tokens > 16384:
                return None, -1

            max_new_tokens = 16384 - total_tokens

            if fragment == 'field':
                max_new_tokens = min(max_new_tokens, 1024)
                # max_new_tokens = 1024
            elif fragment == 'method':
                max_new_tokens = min(max_new_tokens, 4096)
                # max_new_tokens = 4096

            parameters = TextGenerationParameters(  decoding_method=DecodingMethod.GREEDY,
                                                    min_new_tokens=1,
                                                    max_new_tokens=max_new_tokens,
                                                    return_options=TextGenerationReturnOptions(
                                                        input_text=True,
                                                    )
                                                )

            for response in client.text.generation.create(model_id=model_id, input=prompt, parameters=parameters):
                generation = response.results[0].input_text + response.results[0].generated_text
        
        else:

            input_tokens = tokenizer.encode(prompt, return_tensors="pt").to(device)

            if input_tokens.shape[1] > 16384:
                return None, -1

            max_new_tokens = 16384 - input_tokens.shape[1]
            if fragment == 'field':
                max_new_tokens = min(max_new_tokens, 1024)
                # max_new_tokens = 1024
            elif fragment == 'method':
                max_new_tokens = min(max_new_tokens, 4096)
                # max_new_tokens = 4096

            raw_output = model.generate(
                input_tokens,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                output_scores=True,
                return_dict_in_generate=True,
                pad_token_id=tokenizer.eos_token_id,
            )

            generation = tokenizer.decode(raw_output.sequences[0], skip_special_tokens=True)

        generation = generation[generation.find('### Response:')+13:]

        print(generation, flush=True)
        print('---' * 50, flush=True)

        status, parsed_fragment, feedback = l0_validation(generation)

        if not status:
            max_attempts += 1
            ### TODO: create new prompt with feedback
            # prompt = ...
            continue

        """
        TODO: check for functional validation (L2)
        status, functionally_validated_fragment, feedback = l2_validation(dynamically_validated_fragment)

        if not status:
            max_attempts += 1
            TODO: create new prompt with feedback
            prompt = ...
            continue
        """

        max_attempts = 5

    elapsed_time = time.time() - start_time
    return parsed_fragment, elapsed_time


def generate_prompt(data, schema, class_, fragment_, args, fragment_type):

    persona = f"You are an AI programming assistant, utilizing the DeepSeek Coder model, developed by DeepSeek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer."

    icl = ''
    if fragment_type == 'field':
        icl = "Java code:\n```\npublic class Calculator {\n    public int x;\n}\n```" + "\n\nPartial Python translation:\n```\nclass Calculator:\n    x: int = \n```\n\nPython field translation:\n```\n    x: int = 0\n```\n"
    elif fragment_type == 'method':
        icl = "Java code:\n```\npublic class Calculator {\n    public int add(int a, int b) {\n        return a + b;\n    }\n}\n```" + "\n\nPartial Python translation:\n```\nclass Calculator:\n    def add(self, a: int, b: int) -> int:\n        pass\n```\n\nPython method translation:\n```\n    def add(self, a: int, b: int) -> int:\n        return a + b\n```\n"

    original_fragment = ''.join(data['classes'][class_][f'{fragment_type}s'][fragment_]['body'])

    instruction = f'### Instruction:\nTranslate the following {args.from_lang} {fragment_type} to {args.to_lang} like the example above. You only need to translate the \"{fragment_.split(":")[1]}\" {fragment_type}. All necessary dependencies are available in partial {args.to_lang} translation.\n\n'
    instruction += f"{args.from_lang} code:\n```\nclass {class_} {{\n" + original_fragment + f"\n}}\n```"

    instruction += f'\n\nPartial {args.to_lang} translation:\n```\n'
    instruction += '\n'.join(data['python_imports'])
    instruction += '\n\n'
    instruction += data['classes'][class_]['python_class_declaration']

    if fragment_type == 'field':

        if '<placeholder>' not in ''.join(data['classes'][class_]['fields'][fragment_]['partial_translation']):
            return None

        instruction += ''.join(data['classes'][class_]['fields'][fragment_]['partial_translation'].replace('<placeholder>', '') + '\n')
        instruction += '\n```\n\n### Response:\n'
        instruction += f'Python field translation:\n'

    elif fragment_type == 'method':

        related_fields = []
        for field in data['classes'][class_]['fields']:
            if field.split(':')[1] in original_fragment:
                related_fields.append(field)

        for related_field in related_fields:
            instruction += ''.join(data['classes'][class_]['fields'][related_field]['partial_translation'] + '\n')

        instruction += ''.join(data['classes'][class_]['methods'][fragment_]['partial_translation'])

        if len(data['classes'][class_]['methods'][fragment_]['calls']) != 0 and args.include_call_graph:

            out_of_file_dependencies = []
            for callee_schema, callee_class, callee_method in data['classes'][class_]['methods'][fragment_]['calls']:
                callee_schema_data = {}
                with open(f'data/schemas/{args.project_name}/{callee_schema}_python_partial.json', 'r') as f:
                    callee_schema_data = json.load(f)
                
                if ':' not in callee_method:
                    continue

                if callee_schema != schema.replace('_python_partial.json', ''):
                    out_of_file_dependencies.append((callee_schema, callee_class, callee_method))
                    continue

                callee_partial_translation = ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation'])
                instruction += f"\n{callee_partial_translation}"
            
            instruction += '\n```'
            if len(out_of_file_dependencies) != 0:
                instruction += '\n\nThe following methods are called from other classes:\n'
                for callee_schema, callee_class, callee_method in out_of_file_dependencies:
                    instruction += f"\nClass: {callee_class}, Method: {callee_method.split(':')[1]}"
        
        instruction += '\n\n### Response:\n'
        instruction += f'Python method translation:\n'
        instruction += '```\n'
        instruction += ''.join(data['classes'][class_]['methods'][fragment_]['partial_translation']).replace('pass', '')
    
    prompt = f"{persona}\n\n{icl}\n{instruction}"

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

    if args.model_name == 'deepseek-coder-33b-instruct' and not args.use_bam:
        kwargs = {}
        kwargs["torch_dtype"] = torch.float16
        tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-33b-instruct", cache_dir=args.cache_dir)
        model = AutoModelForCausalLM.from_pretrained("deepseek-ai/deepseek-coder-33b-instruct", cache_dir=args.cache_dir, device_map='auto', **kwargs)

    schemas = os.listdir(f'data/schemas/{args.project_name}')

    traversal = {}
    with open(f'data/dependencies/{args.project_name}/traversal.json', 'r') as f:
        traversal = json.load(f)
    
    traversal_order = list(traversal.values())

    schemas = align_schema_order(schemas, traversal_order)

    waiting_queue = {}
    processed_fragments = []

    for schema in schemas:

        path_ = f'data/schemas/{args.project_name}/{schema}'
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

            print(f'Translating class {class_} @ schema {schema}...', flush=True)
            
            pbar = tqdm.tqdm(data['classes'][class_]['fields'])
            for field_ in pbar:
                pbar.update()
                pbar.set_description(f"Translating field {field_} in class {class_} @ schema {schema}...")

                if data['classes'][class_]['fields'][field_]['translation_status'] == 'success':
                    continue

                prompt = generate_prompt(data, schema, class_, field_, args, 'field')

                if prompt is None:
                    data['classes'][class_]['fields'][field_]['translation'] = data['classes'][class_]['fields'][field_]['partial_translation'].split('\n')
                    data['classes'][class_]['fields'][field_]['elapsed_time'] = 0
                    data['classes'][class_]['fields'][field_]['generation_timestamp'] = datetime.datetime.now().isoformat()
                    data['classes'][class_]['fields'][field_]['translation_status'] = 'success'
                    data['classes'][class_]['fields'][field_]['model_name'] = args.model_name

                    with open(f'data/schemas/{args.project_name}/{schema}', 'w') as f:
                        json.dump(data, f, indent=4)
                    continue

                translation, elapsed_time = translate(model, tokenizer, prompt, device, 'field', args)
                if translation is not None:
                    data['classes'][class_]['fields'][field_]['translation_status'] = 'success'
                else:
                    data['classes'][class_]['fields'][field_]['translation_status'] = 'failed'
                
                data['classes'][class_]['fields'][field_]['translation'] = translation
                data['classes'][class_]['fields'][field_]['elapsed_time'] = elapsed_time
                data['classes'][class_]['fields'][field_]['generation_timestamp'] = datetime.datetime.now().isoformat()
                data['classes'][class_]['fields'][field_]['model_name'] = args.model_name

                with open(f'data/schemas/{args.project_name}/{schema}', 'w') as f:
                    json.dump(data, f, indent=4)

            pbar = tqdm.tqdm(data['classes'][class_]['methods'])
            for method_ in pbar:
                pbar.update()
                pbar.set_description(f"Translating method {method_} in class {class_} @ schema {schema}...")

                full_fragment_name = f'{schema.replace("_python_partial.json", "")}|{class_}|{method_}'
                dependent_fragments = [f'{x[0]}|{x[1]}|{x[2]}' for x in data['classes'][class_]['methods'][method_]['calls'] if ':' in x[2] and full_fragment_name != f'{x[0]}|{x[1]}|{x[2]}']

                if data['classes'][class_]['methods'][method_]['translation_status'] == 'success':
                    processed_fragments.append(full_fragment_name)
                    continue

                if any([x not in processed_fragments for x in dependent_fragments]):
                    waiting_queue[full_fragment_name] = [dependent_fragments, data.copy(), schema, class_, method_, 'method', args]
                    continue

                prompt = generate_prompt(data, schema, class_, method_, args, 'method')

                translation, elapsed_time = translate(model, tokenizer, prompt, device, 'method', args)
                if translation is not None:
                    data['classes'][class_]['methods'][method_]['translation_status'] = 'success'
                else:
                    data['classes'][class_]['methods'][method_]['translation_status'] = 'failed'
                
                processed_fragments.append(full_fragment_name)
                
                data['classes'][class_]['methods'][method_]['translation'] = translation
                data['classes'][class_]['methods'][method_]['elapsed_time'] = elapsed_time
                data['classes'][class_]['methods'][method_]['generation_timestamp'] = datetime.datetime.now().isoformat()
                data['classes'][class_]['methods'][method_]['model_name'] = args.model_name

                with open(f'data/schemas/{args.project_name}/{schema}', 'w') as f:
                    json.dump(data, f, indent=4)

                # check if a waiting fragment is now ready to be processed
                for waiting_fragment in list(waiting_queue.keys()):
                    waiting_dependent_fragments = [x for x in waiting_queue[waiting_fragment][0]]
                    if all([x in processed_fragments for x in waiting_dependent_fragments]):
                        _, waiting_data, waiting_schema, waiting_class, waiting_method, waiting_fragment_type, waiting_args = waiting_queue[waiting_fragment]
                        prompt = generate_prompt(waiting_data, waiting_schema, waiting_class, waiting_method, waiting_args, waiting_fragment_type)

                        translation, elapsed_time = translate(model, tokenizer, prompt, device, 'method', args)

                        waiting_data = {}
                        with open(f'data/schemas/{args.project_name}/{waiting_schema}', 'r') as f:
                            waiting_data = json.load(f)

                        if translation is not None:
                            waiting_data['classes'][waiting_class]['methods'][waiting_method]['translation_status'] = 'success'
                        else:
                            waiting_data['classes'][waiting_class]['methods'][waiting_method]['translation_status'] = 'failed'
                        
                        waiting_data['classes'][waiting_class]['methods'][waiting_method]['translation'] = translation
                        waiting_data['classes'][waiting_class]['methods'][waiting_method]['elapsed_time'] = elapsed_time
                        waiting_data['classes'][waiting_class]['methods'][waiting_method]['generation_timestamp'] = datetime.datetime.now().isoformat()
                        waiting_data['classes'][waiting_class]['methods'][waiting_method]['model_name'] = args.model_name

                        processed_fragments.append(waiting_fragment)
                        del waiting_queue[waiting_fragment]

                        with open(f'data/schemas/{args.project_name}/{waiting_schema}', 'w') as f:
                            json.dump(waiting_data, f, indent=4)

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
                prompt = generate_prompt(waiting_data, waiting_schema, waiting_class, waiting_method, waiting_args, waiting_fragment_type)

                translation, elapsed_time = translate(model, tokenizer, prompt, device, 'method', args)

                waiting_data = {}
                with open(f'data/schemas/{args.project_name}/{waiting_schema}', 'r') as f:
                    waiting_data = json.load(f)

                if translation is not None:
                    waiting_data['classes'][waiting_class]['methods'][waiting_method]['translation_status'] = 'success'
                else:
                    waiting_data['classes'][waiting_class]['methods'][waiting_method]['translation_status'] = 'failed'
                
                waiting_data['classes'][waiting_class]['methods'][waiting_method]['translation'] = translation
                waiting_data['classes'][waiting_class]['methods'][waiting_method]['elapsed_time'] = elapsed_time
                waiting_data['classes'][waiting_class]['methods'][waiting_method]['generation_timestamp'] = datetime.datetime.now().isoformat()
                waiting_data['classes'][waiting_class]['methods'][waiting_method]['model_name'] = args.model_name

                del waiting_queue[waiting_fragment]
                processed_fragments.append(waiting_fragment)
                threshold = 3

                with open(f'data/schemas/{args.project_name}/{waiting_schema}', 'w') as f:
                    json.dump(waiting_data, f, indent=4)
        
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
            prompt = generate_prompt(waiting_data, waiting_schema, waiting_class, waiting_method, waiting_args, waiting_fragment_type)

            translation, elapsed_time = translate(model, tokenizer, prompt, device, 'method', args)

            waiting_data = {}
            with open(f'data/schemas/{args.project_name}/{waiting_schema}', 'r') as f:
                waiting_data = json.load(f)

            if translation is not None:
                waiting_data['classes'][waiting_class]['methods'][waiting_method]['translation_status'] = 'success'
            else:
                waiting_data['classes'][waiting_class]['methods'][waiting_method]['translation_status'] = 'failed'
            
            waiting_data['classes'][waiting_class]['methods'][waiting_method]['translation'] = translation
            waiting_data['classes'][waiting_class]['methods'][waiting_method]['elapsed_time'] = elapsed_time
            waiting_data['classes'][waiting_class]['methods'][waiting_method]['generation_timestamp'] = datetime.datetime.now().isoformat()
            waiting_data['classes'][waiting_class]['methods'][waiting_method]['model_name'] = args.model_name

            processed_fragments.append(cycle_fragment)
            del waiting_queue[cycle_fragment]

            with open(f'data/schemas/{args.project_name}/{waiting_schema}', 'w') as f:
                json.dump(waiting_data, f, indent=4)

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
                prompt = generate_prompt(waiting_data, waiting_schema, waiting_class, waiting_method, waiting_args, waiting_fragment_type)

                translation, elapsed_time = translate(model, tokenizer, prompt, device, 'method', args)

                waiting_data = {}
                with open(f'data/schemas/{args.project_name}/{waiting_schema}', 'r') as f:
                    waiting_data = json.load(f)
                
                if translation is not None:
                    waiting_data['classes'][waiting_class]['methods'][waiting_method]['translation_status'] = 'success'
                else:
                    waiting_data['classes'][waiting_class]['methods'][waiting_method]['translation_status'] = 'failed'
                
                waiting_data['classes'][waiting_class]['methods'][waiting_method]['translation'] = translation
                waiting_data['classes'][waiting_class]['methods'][waiting_method]['elapsed_time'] = elapsed_time
                waiting_data['classes'][waiting_class]['methods'][waiting_method]['generation_timestamp'] = datetime.datetime.now().isoformat()
                waiting_data['classes'][waiting_class]['methods'][waiting_method]['model_name'] = args.model_name

                del waiting_queue[waiting_fragment]
                processed_fragments.append(waiting_fragment)
                threshold = 3

                with open(f'data/schemas/{args.project_name}/{waiting_schema}', 'w') as f:
                    json.dump(waiting_data, f, indent=4)
        
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
    parser_.add_argument('--cache_dir', type=str, dest='cache_dir', help='cache directory')
    parser_.add_argument('--use_bam', action='store_true', help='translate main files')
    parser_.add_argument('--use_cuda', action='store_true', help='use cuda for translation')
    args = parser_.parse_args()
    main(args)
