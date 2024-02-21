import argparse
import json
from dotenv import load_dotenv
import torch
import re
import tqdm
import ast
import os
from transformers import LlamaForCausalLM, CodeLlamaTokenizer


def translate(model, tokenizer, prompt, device, fragment):
    max_attempts = 0
    extracted_string = None
    while max_attempts < 5:

        input_tokens = tokenizer.encode(prompt, return_tensors="pt").to(device)

        raw_output = model.generate(
            input_tokens,
            max_new_tokens=(2000 - input_tokens.shape[1]),
            do_sample=True,
            output_scores=True,
            return_dict_in_generate=True,
            pad_token_id=tokenizer.eos_token_id,
            top_p=0.95,
            temperature=0.2,
        )

        generation = tokenizer.decode(raw_output.sequences[0], skip_special_tokens=True)
        generation = generation[generation.find('[/INST]')+8:]

        print(prompt, flush=True)
        print('=======================GENERATING=======================', flush=True)
        print(generation, flush=True)
        print('---' * 50, flush=True)

        if fragment == 'field':
            pattern = r'Python field:\n```([^`]+)```'
        elif fragment == 'method':
            pattern = r'Python method:\n```([^`]+)```'

        match = re.search(pattern, generation, re.DOTALL)

        if match:
            try:
                ast.parse(match.group(1).strip())
                print(f'=======================PARSED=======================\n{match.group(1)}\n---' * 50, flush=True)
            except (SyntaxError, MemoryError) as e:
                print(f'=======================PARSE ERROR=======================\n{e}\n---' * 50, flush=True)
                max_attempts += 1
                continue
            extracted_string = match.group(1).split('\n')
            max_attempts = 5
        else:
            max_attempts += 1

    return extracted_string


def main(args):

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    if args.model_name == 'codellama-13b-instruct':
        kwargs = {}
        # kwargs["torch_dtype"] = torch.float16
        tokenizer = CodeLlamaTokenizer.from_pretrained("codellama/CodeLlama-13b-Instruct-hf", cache_dir='/home/shared/huggingface')
        model = LlamaForCausalLM.from_pretrained("codellama/CodeLlama-13b-Instruct-hf", cache_dir='/home/shared/huggingface', device_map='auto', **kwargs)
    else:
        raise ValueError(f"Model name {args.model_name} not supported")

    schemas = os.listdir(f'data/schemas/{args.project_name}')

    for schema in schemas:

        if not schema.endswith('_python_partial.json'):
            continue

        if os.path.exists(f'data/translations/{args.project_name}/{schema.replace("python_partial", "translation")}'):
            continue

        if 'src.test' not in schema:
            continue

        # if 'FileItemHeadersTest' not in schema:
        #     continue

        path_ = f'data/schemas/{args.project_name}/{schema}'
        with open(path_, 'r') as f:
            data = json.load(f)

        for class_ in data['classes']:

            print(f'Translating class {class_} @ schema {schema}...', flush=True)
            
            pbar = tqdm.tqdm(data['classes'][class_]['fields'])
            for field_ in pbar:
                pbar.update()
                pbar.set_description(f"Translating field {field_} in class {class_} @ schema {schema}...")

                original_field = ''.join(data['classes'][class_]['fields'][field_]['body'])
                partial_translated_field = data['classes'][class_]['fields'][field_]['partial_translation']

                icl = "Java field:\n```\n    public int x;\n```" + "\n\nPython field:\n```\n    x: int = 0\n```\n\n"

                persona = f"You are an expert {args.to_lang} programmer and assistant."

                for i in range(args.num_translations):
                    if '<placeholder>' not in partial_translated_field:
                        data['classes'][class_]['fields'][field_][f'translation_{i + 1}'] = partial_translated_field
                        continue

                    prompt = f"Translate the following {args.from_lang} field to {args.to_lang} like the example above:\n" + f"\n{args.from_lang} field:\n```\n" + original_field + f"\n```\n\n{args.to_lang} field:\n```\n{partial_translated_field.replace('<placeholder>', '')}"
                    prompt = f"<s>{icl}[INST] <<SYS>>\n{persona}\n<</SYS>>\n\n{prompt}[/INST]"
                    translated_fragment = translate(model, tokenizer, prompt, device, 'field')
                    data['classes'][class_]['fields'][field_][f'translation_{i + 1}'] = translated_fragment

            pbar = tqdm.tqdm(data['classes'][class_]['methods'])
            for method_ in pbar:
                pbar.update()
                pbar.set_description(f"Translating method {method_} in class {class_} @ schema {schema}...")

                icl = "Java method:\n```\n\tpublic int add(int a, int b) {\n\t\treturn a + b;\n\t}\n```" + "\n\nPython method:\n```\n\tdef add(self, a: int, b: int) -> int:\n\t\treturn a + b\n```\n\n"
                persona = f"You are an expert {args.to_lang} programmer and assistant."

                original_method = ''.join(data['classes'][class_]['methods'][method_]['body'])
                partial_translated_method = ''.join(data['classes'][class_]['methods'][method_]['partial_translation'])

                related_fields = []
                for field in data['classes'][class_]['fields']:
                    if field.split(':')[1] in original_method:
                        related_fields.append(field)

                for i in range(args.num_translations):

                    instruction = f"Translate the following {args.from_lang} method to {args.to_lang} like the example above:\n"

                    if len(data['classes'][class_]['methods'][method_]['calls']) != 0 and args.include_call_graph:
                        instruction += f"\nThe following methods are called in the method body and are already translated:\n"

                        for callee_schema, callee_class, callee_method in data['classes'][class_]['methods'][method_]['calls']:
                            callee_schema_data = {}
                            with open(f'data/schemas/{args.project_name}/{callee_schema}_python_partial.json', 'r') as f:
                                callee_schema_data = json.load(f)
                            if ':' not in callee_method:
                                continue
                            callee_partial_translation = ''.join(callee_schema_data['classes'][callee_class]['methods'][callee_method]['partial_translation'])
                            instruction += f"\n{callee_partial_translation}"
                    
                    for related_field in related_fields:
                        instruction += f"\n\nThe following field(s) are used in the method body and are already translated:\n"
                        instruction += f"{related_field.split(':')[1].strip()} -> {data['classes'][class_]['fields'][related_field]['partial_translation'].split(':')[0].strip()}\n"
                    
                    prompt = f"{instruction}\n{args.from_lang} method:\n```\n" + original_method + f"\n```\n\n{args.to_lang} method:\n```\n{partial_translated_method.replace('pass', '')}"

                    prompt = f"\n<s>{icl}[INST] <<SYS>>\n{persona}\n<</SYS>>\n\n{prompt}[/INST]"
                    translated_fragment = translate(model, tokenizer, prompt, device, 'method')
                    data['classes'][class_]['methods'][method_][f'translation_{i + 1}'] = translated_fragment
    
        os.makedirs(f'data/translations/{args.project_name}', exist_ok=True)
        with open(f'data/translations/{args.project_name}/{schema.replace("python_partial", "translation")}', 'w') as f:
            json.dump(data, f, indent=4)


if __name__ == '__main__':
    load_dotenv()
    parser_ = argparse.ArgumentParser(description='Translate java types to python types')
    parser_.add_argument('--model_name', type=str, dest='model_name', help='model name to use for translation')
    parser_.add_argument('--project_name', type=str, dest='project_name', help='project name to translate')
    parser_.add_argument('--from_lang', type=str, dest='from_lang', help='language to translate from')
    parser_.add_argument('--to_lang', type=str, dest='to_lang', help='language to translate to')
    parser_.add_argument('--include_call_graph', action='store_true', help='include call graph in translation')
    parser_.add_argument('--num_translations', type=int, dest='num_translations', help='number of translations to generate per request')
    parser_.add_argument('--translate_test', action='store_true', help='translate test files')
    parser_.add_argument('--translate_main', action='store_true', help='translate main files')
    args = parser_.parse_args()
    main(args)
