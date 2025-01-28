import os
import re
import argparse
import ast
import tqdm
import tiktoken
from ollama import Client
from openai import OpenAI


def get_all_java_files(path_):
    java_files = []
    for root, _, files in os.walk(path_):
        for file in files:
            if file.endswith('.java'):
                java_files.append(f'{root}/{file}')
    java_files = [file for file in java_files if 'evosuite-tests' not in file]
    return java_files


def syntactic_validation(generation):

    generation = generation.replace('```python', '```')
    pattern = r'```((?:[^`]|`[^`]|``[^`])*?)```'
    match = re.search(pattern, generation, re.DOTALL)

    if match:
        try:
            output = match.group(1)

            ast.parse(output)

            return True, output, None

        except (SyntaxError, MemoryError) as e:

            feedback = e.msg if hasattr(e, 'msg') else str(e)
            return False, None, feedback
    else:
        return False, None, 'the model did not generate any code'


def prompt_model(model_info, client, prompt, args):

    if args.model_name == 'gpt-4o-2024-11-20':
        completion = client.chat.completions.create(
            model=args.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=model_info[args.model_name]['max_new_tokens'],
            temperature=0.0,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )

        generation = completion.choices[0].message.content

    else:
        completion = client.chat(
            model=model_info[args.model_name]['model_id'],
            messages=[
            {
                'role': 'user',
                'content': prompt,
            }],
            options={
                "temperature": 0.0,
                "num_predict": model_info[args.model_name]['max_new_tokens'],
            }
        )
        generation = completion.message.content

    return generation


def main(args):

    model_info = {
        'deepseek-coder-33b-instruct': {'total': 16384, 'max_new_tokens': 4096, 'model_id': 'deepseek-ai/deepseek-coder-33b-instruct'},
        'gpt-4o-2024-11-20': {'total': 128000, 'max_new_tokens': 16384, 'model_id': 'gpt-4o-2024-11-20'}
    }

    client = None
    if args.model_name in model_info:
        if args.model_name == 'gpt-4o-2024-11-20':
            client = OpenAI(
                api_key=os.environ["OPENAI_API_KEY"],
            )
        else:
            client = Client(
                host=os.environ["OLLAMA_HOST"],
            )
    else:
        raise ValueError('No model found')

    schemas_path = f'java_projects/cleaned_final_projects/{args.project_name}'

    translation_dir = f'class_by_class_prompting/class_by_class_{args.model_name}'

    os.makedirs(f'{translation_dir}', exist_ok=True)

    java_files = get_all_java_files(schemas_path)

    encoding = tiktoken.encoding_for_model('gpt-4o')

    total_files = 0
    total_files_token_exceed = 0
    total_compile_error = 0

    for file in tqdm.tqdm(java_files):

        subdir = '/'.join(file.replace('java_projects/cleaned_final_projects/', '').split('/')[:-1])
        os.makedirs(f'{translation_dir}/{subdir}', exist_ok=True)

        content = ''
        with open(file) as f:
            content = f.read()

        total_files += 1
        
        total_input_tokens = len(encoding.encode(content))
        
        if total_input_tokens >= model_info[args.model_name]['total']:
            total_files_token_exceed += 1
            continue
        
        prompt = f'### Instruction:\nTranslate the following Java code to Python. You can assume all dependencies will be imported so only translate the given source code.\n\nJava Code:\n{content}\n\n### Response:\nPython Code:\n```\n'

        generation = prompt_model(model_info, client, prompt, args)

        status, cleaned_out, feedback = syntactic_validation(generation)

        if not status:
            total_compile_error += 1
            print(f'Compile Error: {file}')
            continue

        with open(f'{translation_dir}/{file.replace("java_projects/cleaned_final_projects/", "").replace(".java", "")}.py', 'w') as f:
            f.write(cleaned_out)

    print('Project:', args.project_name)
    print('Total Files:', total_files)
    print('Total Files Token Exceed:', total_files_token_exceed)
    print('Total Compile Error:', total_compile_error)

    with open(f'{translation_dir}/{args.project_name}/pytest.ini', 'w') as f:
        f.write('# pytest.ini\n\n[pytest]\n# Require at least this version of pytest\nminversion = 8.2.1\n\n# Add options to control the pytest output\naddopts = -ra -q --continue-on-collection-errors --tb=native --junitxml=pytest-report.xml\n\n# Define directories to look for tests\n;testpaths = evosuite-test\ntestpaths = src/test\n\npython_files = *.py\n\npython_classes = *Test\n\npython_functions = test*\n')

    with open(f'{translation_dir}/{args.project_name}/run.sh', 'w') as f:
        f.write('CURRENT_DIR=$(pwd)\nexport PYTHONPATH=$CURRENT_DIR\npython3 -m pytest\nxmllint --format pytest-report.xml -o pytest-report.xml')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--project_name', type=str, help='Project Name')
    parser.add_argument('--model_name', type=str, help='Model Name')
    args = parser.parse_args()
    main(args)
