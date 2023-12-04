import argparse
import json
from dotenv import load_dotenv
import torch
import re
from transformers import (
    LlamaForCausalLM, CodeLlamaTokenizer,
)

def main(args):

    with open(f"data/types.json", "r") as f:
        types = json.load(f)

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    if args.model_name == 'codellama-13b-instruct':
        kwargs = {}
        kwargs["torch_dtype"] = torch.float16
        tokenizer = CodeLlamaTokenizer.from_pretrained("codellama/CodeLlama-13b-Instruct-hf", cache_dir='/home/shared/huggingface')
        model = LlamaForCausalLM.from_pretrained("codellama/CodeLlama-13b-Instruct-hf", cache_dir='/home/shared/huggingface', device_map='auto', **kwargs)

    index = 0
    max_attempts = 5
    while index < len(types):
        if max_attempts == 0:
            print(f"Failed to translate {type_}... skipping")
            index += 1
            max_attempts = 5
            continue

        type_ = list(types.keys())[index]
        if types[type_] != '':
            index += 1
            continue

        persona = f"I want you to act like a {args.from_lang} to {args.to_lang} translator expert. Make sure your translations are syntactically correct and satisfy all constrains in the prompt.\n"
        prompt = f"Translate the following {args.from_lang} type to {args.to_lang} type:\n\n{args.from_lang} type:\n" + type_ + f"\n\n{args.to_lang} type:\n"
        prompt = f"<s>[INST] <<SYS>>\n{persona}\n<</SYS>>\n\n{prompt}[/INST]"

        input_tokens = tokenizer.encode(prompt, return_tensors="pt").to(device)

        raw_output = model.generate(
            input_tokens,
            max_new_tokens=20,
            do_sample=True,
            output_scores=True,
            return_dict_in_generate=True,
            pad_token_id=tokenizer.eos_token_id,
            top_p=0.95,
            temperature=0.2,
        )

        generation = tokenizer.decode(raw_output.sequences[0], skip_special_tokens=True)
        generation = re.findall(rf"{args.to_lang} type: (.*)", generation)

        if len(generation) == 0:
            print(f"Failed to translate {type_}... trying again")
            max_attempts -= 1
            continue

        generation = generation[0].strip()

        if generation == '':
            print(f"Failed to translate {type_}... trying again")
            max_attempts -= 1
            continue

        print(f"Translated {type_} to {generation}")

        types[type_] = generation
        index += 1
        max_attempts = 5
    
    with open(f"data/types.json", "w") as f:
        json.dump(types, f, indent=4)


if __name__ == '__main__':
    load_dotenv()
    parser_ = argparse.ArgumentParser(description='Translate java types to python types')
    parser_.add_argument('--model_name', type=str, dest='model_name', help='model name to use for translation')    
    parser_.add_argument('--from_lang', type=str, dest='from_lang', help='language to translate from')
    parser_.add_argument('--to_lang', type=str, dest='to_lang', help='language to translate to')
    args = parser_.parse_args()
    main(args)
