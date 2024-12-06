import argparse
import json
from dotenv import load_dotenv
import tqdm
import subprocess
import os
import re
from subprocess import Popen
import logging
from genai.client import Client
from genai.credentials import Credentials
from genai.schema import (
    DecodingMethod,
    TextGenerationParameters,
    TextGenerationReturnOptions,
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

        index += 1

        icl = f"{args.from_lang} type:\nString\n\n{args.to_lang} type:\nstr"
        instruction = f"### Instruction:\nTranslate the following {args.from_lang} type to {args.to_lang} {args.to_lang_version} type and write your response like the example above:\n\n{args.from_lang} type:\n" + type_ + f"\n\n### Response:\n{args.to_lang} type:\n\n"

        if args.type == 'source_description':
            description = type_description[type_]['summarized_text'].replace('\n', '')
            instruction = instruction.replace(f'### Instruction:\nTranslate the following {args.from_lang} type to {args.to_lang} {args.to_lang_version} type and write your response like the example above:', f"### Instruction:\nTranslate the following {args.from_lang} type to {args.to_lang} {args.to_lang_version} type and write your response like the example above. A description of {args.from_lang} type is given as well:\n\nType Description:\n{description}")

            if include_feedback:
                instruction = instruction.replace(f'A description of {args.from_lang} type is given as well:\n\nType Description:\n{description}', f'Your previous translation attempt was incorrect. Here is the feedback:\n\n{feedback}\n\nA description of {args.from_lang} type is give as well:\n\nType Description:\n{description}')

        elif args.type == 'simple':
            if include_feedback:
                instruction = instruction.replace(f'### Instruction:\nTranslate the following {args.from_lang} type to {args.to_lang} {args.to_lang_version} type and write your response like the example above:', f'Your previous translation attempt was incorrect. Here is the feedback:\n\n{feedback}\n\n### Instruction:\nTranslate the following {args.from_lang} type to {args.to_lang} {args.to_lang_version} type and write your response like the example above:')

        prompt = f"{icl}\n\n{instruction}"

        logging.info('*' * 100)
        logging.info(prompt)
        logging.info('*' * 100)

        client = Client(credentials=Credentials.from_env())
        model_id = "deepseek-ai/deepseek-coder-33b-instruct"

        parameters = TextGenerationParameters(  decoding_method=DecodingMethod.GREEDY,
                                                min_new_tokens=1,
                                                max_new_tokens=1024,
                                                return_options=TextGenerationReturnOptions(
                                                    input_text=True,
                                                ),
                                                time_limit=60000,
                                            )

        for response in client.text.generation.create(model_id=model_id, input=prompt, parameters=parameters):
            generation = response.results[0].input_text + response.results[0].generated_text

        generation = generation[generation.find('### Response:') + len('### Response:'):].strip()

        generation = generation.replace('```python', '```')
        pattern = r'```((?:[^`]|`[^`]|``[^`])*?)```'
        match = re.search(pattern, generation, re.DOTALL)

        if not match:
            logging.info(f"Failed to translate {type_}... trying again")
            max_attempts -= 1
            continue

        generation = match.group(1).strip()

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
    if total_overturning_attempts != []:
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
