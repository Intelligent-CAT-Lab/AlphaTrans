import argparse
import json
from dotenv import load_dotenv
import torch
import tqdm
import subprocess
import os
import re
from subprocess import Popen
import logging
from transformers import (
    LlamaForCausalLM, CodeLlamaTokenizer,
)


def main(args):

    if not os.path.exists(f"data/type_resolution/universal_type_map.json"):
        with open(f"data/type_resolution/universal_type_map.json", "w") as f:
            json.dump({}, f)

    universal_type_map = {}
    with open(f"data/type_resolution/universal_type_map.json", "r") as f:
        universal_type_map = json.load(f)

    logging.basicConfig(filename=f"data/type_resolution/{args.project_name}/{args.type}.log", level=logging.INFO, format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('new run started...')

    in_fname = f"data/type_resolution/{args.project_name}/s1_input.json"
    out_fname = f"data/type_resolution/{args.project_name}/s1_output.json"

    if args.type == 'source_description':
        in_fname = f"data/type_resolution/{args.project_name}/s1_output.json"
        out_fname = f"data/type_resolution/{args.project_name}/s2_output.json"

    logging.info(f"Translating types from {args.from_lang} to {args.to_lang} in project {args.project_name} using {args.model_name}")
    logging.info(f"Target language version: {args.to_lang_version}. Translation type: {args.type}")

    types = {}
    with open(in_fname, "r") as f:
        types = json.load(f)

    type_description = {}
    with open(f"data/type_resolution/{args.project_name}/type_description.json", "r") as f:
        type_description = json.load(f)

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    if args.model_name == 'codellama-13b-instruct':
        kwargs = {}
        kwargs["torch_dtype"] = torch.float16
        tokenizer = CodeLlamaTokenizer.from_pretrained("codellama/CodeLlama-13b-Instruct-hf", cache_dir='/home/shared/huggingface')
        model = LlamaForCausalLM.from_pretrained("codellama/CodeLlama-13b-Instruct-hf", cache_dir='/home/shared/huggingface', device_map='auto', **kwargs)
        logging.info(f'Loaded model: {args.model_name}')

    index = 0
    max_attempts = 5
    total_failed = 0
    total_success = 0
    total_overturning_attempts = []
    include_feedback = False
    feedback = ''
    pbar = tqdm.tqdm(total=len(types))
    while index < len(types):
        if max_attempts == 0:
            logging.info(f"Failed to translate {type_}... skipping")
            total_failed += 1
            index += 1
            include_feedback = False
            feedback = ''
            max_attempts = 5
            universal_type_map[type_] = ''
            pbar.update(1)
            continue

        type_ = list(types.keys())[index]

        if type_ in universal_type_map and universal_type_map[type_] != '':
            assert universal_type_map[type_].strip() != ''
            logging.info(f"{type_} already translated to {universal_type_map[type_]}")
            types[type_] = universal_type_map[type_]
            index += 1
            total_success += 1
            pbar.update(1)
            continue

        if types[type_] != '':
            index += 1
            universal_type_map[type_] = types[type_]
            pbar.update(1)
            continue

        icl = f"{args.from_lang} type:\nString\n\n{args.to_lang} type:\nstr\n\n"
        system_message = f"You are an expert {args.to_lang} programmer and assistant."
        instruction = f"Translate the following {args.from_lang} type to {args.to_lang} {args.to_lang_version} type and write your response like the example above:\n\n{args.from_lang} type:\n" + type_ + f"\n\n{args.to_lang} type:\n\n"

        if args.type == 'source_description':
            description = type_description[type_]['summarized_text'].replace('\n', '')
            instruction = instruction.replace(f'Translate the following {args.from_lang} type to {args.to_lang} {args.to_lang_version} type and write your response like the example above:', f"Translate the following {args.from_lang} type to {args.to_lang} {args.to_lang_version} type and write your response like the example above. A description of {args.from_lang} type is give as well:\n\nType Description:\n{description}")

            if include_feedback:
                instruction = instruction.replace(f'A description of {args.from_lang} type is give as well:\n\nType Description:\n{description}', f'Your previous translation attempt was incorrect. Here is the feedback:\n\n{feedback}\n\nA description of {args.from_lang} type is give as well:\n\nType Description:\n{description}')

        elif args.type == 'simple':
            if include_feedback:
                instruction = instruction.replace(f'Translate the following {args.from_lang} type to {args.to_lang} {args.to_lang_version} type and write your response like the example above:', f'Your previous translation attempt was incorrect. Here is the feedback:\n\n{feedback}\n\nTranslate the following {args.from_lang} type to {args.to_lang} {args.to_lang_version} type and write your response like the example above:')

        prompt = f"<s>{icl}[INST] <<SYS>>\n{system_message}\n<</SYS>>\n\n{instruction}[/INST]"

        logging.info('*' * 100)
        logging.info(prompt)
        logging.info('*' * 100)

        input_tokens = tokenizer.encode(prompt, return_tensors="pt").to(device)

        raw_output = model.generate(
            input_tokens,
            max_new_tokens=100,
            do_sample=True,
            output_scores=True,
            return_dict_in_generate=True,
            pad_token_id=tokenizer.eos_token_id,
            top_p=0.95,
            temperature=0.2,
        )

        generation = tokenizer.decode(raw_output.sequences[0])
        generation = generation.replace(prompt, '').replace('<s>', '').replace('</s>', '').replace(f'{args.to_lang} type:', '').replace(f'{args.from_lang} type:', '').strip().split('\n')

        if len(generation) == 0:
            logging.info(f"Failed to translate {type_}... trying again")
            max_attempts -= 1
            continue

        generation = generation[0].strip()

        if generation == '':
            logging.info(f"Failed to translate {type_}... trying again")
            max_attempts -= 1
            continue

        generation = generation.replace('list', 'List')
        generation = generation.replace('dict', 'Dict')
        generation = generation.replace('set', 'Set')
        generation = generation.replace('type', 'Type')

        pattern = re.compile(r'\bV\b')
        generation = pattern.sub('Any', generation)

        pattern = re.compile(r'\bE\b')
        generation = pattern.sub('Any', generation)

        pattern = re.compile(r'\bC\b')
        generation = pattern.sub('Any', generation)

        pattern = re.compile(r'\bP\b')
        generation = pattern.sub('Any', generation)

        pattern = re.compile(r'\bWE\b')
        generation = pattern.sub('Any', generation)

        pattern = re.compile(r'\bR\b')
        generation = pattern.sub('Any', generation)

        pattern = re.compile(r'\bD\b')
        generation = pattern.sub('Any', generation)

        pattern = re.compile(r'\bK\b')
        generation = pattern.sub('Any', generation)

        pattern = re.compile(r'\bF\b')
        generation = pattern.sub('Any', generation)

        if 'Option' in type_ and 'Optional' in generation:
            generation = generation.replace('Optional', 'Option')

        with open(f'data/templates/{args.project_name}/template.py', 'r') as f:
            python_program = f.read()
            python_program = python_program.replace('<placeholder>', generation)

        with open('program.py', 'w') as f:
            f.write(python_program)

        try:
            subprocess.run("python3 -m py_compile program.py", check=True, capture_output=True, shell=True, timeout=30)
            p = Popen(['python3', 'program.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr_data = p.communicate(timeout=100)

            if stderr_data.decode('utf-8') != '':
                # logging.info(stderr_data.decode('utf-8'))
                logging.info(f'execution error for translated type {generation}... trying again for {type_}')
                feedback = stderr_data.decode('utf-8')
                feedback = '\n'.join(feedback.strip().split('\n')[-2:])
                include_feedback = True
                max_attempts -= 1
                continue
            else:
                # logging.info('success')
                pass
        
        except subprocess.CalledProcessError as e:
            # logging.info(e.stderr.decode('utf-8'))
            logging.info(f'compile error for translated type {generation}... trying again for {type_}')
            feedback = f'The translated type {generation} is syntactically incorrect in {args.to_lang} {args.to_lang_version}.\n\n'
            include_feedback = True
            max_attempts -= 1
            continue

        os.remove('program.py')

        logging.info(f"Translated {type_} to {generation}")

        pbar.update(1)
        total_success += 1
        types[type_] = generation
        universal_type_map[type_] = generation
        index += 1
        total_overturning_attempts.append(5 - max_attempts)
        max_attempts = 5
        include_feedback = False
        feedback = ''
    
    with open(out_fname, "w") as f:
        json.dump(types, f, indent=4)
    
    with open(f"data/type_resolution/universal_type_map.json", "w") as f:
        json.dump(universal_type_map, f, indent=4)

    logging.info(f"Total success: {total_success}")
    logging.info(f"Total failed: {total_failed}")
    logging.info(f"Average attempts to overturn: {sum(total_overturning_attempts) / len(total_overturning_attempts)}")


if __name__ == '__main__':
    load_dotenv()
    parser_ = argparse.ArgumentParser(description='Translate java types to python types')
    parser_.add_argument('--project_name', type=str, dest='project_name', help='project name')
    parser_.add_argument('--model_name', type=str, dest='model_name', help='model name to use for translation')
    parser_.add_argument('--from_lang', type=str, dest='from_lang', help='language to translate from')
    parser_.add_argument('--to_lang', type=str, dest='to_lang', help='language to translate to')
    parser_.add_argument('--to_lang_version', type=str, dest='to_lang_version', help='language version to translate to')
    parser_.add_argument('--type', type=str, dest='type', help='translation type')
    args = parser_.parse_args()
    main(args)
