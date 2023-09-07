import os
import openai
import argparse
import re
import tiktoken
import json
from dotenv import load_dotenv
import parser


def setup_api():
    api_key = os.getenv("OPENAI_KEY")
    openai.api_key = api_key


def send_message_to_openai(message_log):
    "Use OpenAI's ChatCompletion API to get the chatbot's response"
    encoding = tiktoken.encoding_for_model("gpt-4")
    num_tokens = len(encoding.encode(message_log[1]["content"]))

    response = "<problem with OpenAI API>"
    is_success = False
    max_attempts = 5
    while max_attempts > 0:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # The name of the OpenAI chatbot model to use
                # The conversation history up to this point, as a list of dictionaries
                messages=message_log,
                # The maximum number of tokens (words or subwords) in the generated response
                max_tokens=max(1, 8000-num_tokens),
                # The "creativity" of the generated response (higher temperature = more creative)
                temperature=0,
            )
            is_success = True
            break
        except openai.error.InvalidRequestError as e:
            return "# Token size exceeded."
        except Exception as e:
            max_attempts -= 1
            continue

    if not is_success:
        return response

    # Find the first response from the chatbot that has text in it (some responses may not have text)
    for choice in response.choices:
        if "text" in choice:
            return choice.text

    # If no response with text is found, return the first response's content (which may be empty)
    return response.choices[0].message.content


def translate_with_OPENAI(source_skeleton, target_skeleton, is_buggy=False, stack_trace=None):
    persona = "I want you to act like a Java to Python translator expert. Make sure your translations are syntactically correct and satisfy all constrains in the prompt.\n\n"
    one_shot_learning = "Here is an example of a Java program skeleton:\n\n" \
                        "Java skeleton:\n\n" \
                        "// Imports Begin\n" \
                        "import java.util.*;\n" \
                        "// Imports End\n" \
                        "public class Calculator {\n" \
                        "    // Class Fields Begin\n" \
                        "    public int result;\n" \
                        "    // Class Fields End\n" \
                        "    \n" \
                        "    // Class Methods Begin\n" \
                        "    public int add(int a, int b) {}\n" \
                        "    public double add(double a, double b) {}\n" \
                        "    public double square(double a) {}\n" \
                        "    public String getResult(String expression) {}\n" \
                        "    // Class Methods End\n" \
                        "}\n\n" \
                        "Moreover, here is an example of incomplete Python skeleton:\n\n" \
                        "Python skeleton:\n\n" \
                        "# Imports Begin\n" \
                        "<placeholder>\n" \
                        "# Imports End\n" \
                        "class Calculator:\n" \
                        "    # Class Fields Begin\n" \
                        "    result: <placeholder>\n" \
                        "    # Class Fields End\n" \
                        "    \n" \
                        "    # Class Methods Begin\n" \
                        "    def add(self, a: <placeholder>, b: <placeholder>) -> <placeholder>:\n" \
                        "        pass\n" \
                        "    \n" \
                        "    def square(self, a: <placeholder>) -> <placeholder>:\n" \
                        "        pass\n" \
                        "    \n" \
                        "    def getResult(self, expression: <placeholder>) -> <placeholder>:\n" \
                        "        pass\n" \
                        "    # Class Methods End\n" \
                        "\n\n" \
                        "Here is the correct re-generated Python skeleton:\n\n" \
                        "```python\n" \
                        "from typing import Union\n" \
                        "class Calculator:\n" \
                        "    result: int\n" \
                        "    \n" \
                        "    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:\n" \
                        "        pass\n" \
                        "    \n" \
                        "    def square(self, a: float) -> float:\n" \
                        "        pass\n" \
                        "    \n" \
                        "    def getResult(self, expression: str) -> str:\n" \
                        "        pass\n" \
                        "```\n\n"

    objective = "Given the following Java program skeleton and incomplete Python skeleton, re-generate the Python skeleton after filling the <placeholder> tokens. " \
                "Make sure your generated code is inside ```python ... ``` and is syntactically correct. " \
                "You can assume all un-imported classes will be imported.\n\n"

    content = persona + objective + "Java skeleton:\n\n" + source_skeleton + "\n\nPython skeleton:\n\n" + target_skeleton + "\n\n"

    if is_buggy:
        content += "Your previous translation was syntactically incorrect with the following error:\n"
        content += stack_trace + "\n\n"
        content += "Please fix the error and re-generate the Python skeleton.\n\n"
    content = content.strip()

    message = [
        {"role": "system", "content": "Hello GPT-4, you are a helpful assistant. Please translate the programs correctly."},
        {"role": "user", "content": content}]
    response = send_message_to_openai(message)
    response = re.search(r"```python(.*)```", response, re.DOTALL).group(1)
    return response


def main(args):
    setup_api()

    with open(f"data/skeletons/{args.class_name}.json", "r") as f:
        skeletons = json.load(f)

    response = translate_with_OPENAI(source_skeleton=skeletons[args.from_lang], target_skeleton=skeletons[args.to_lang])

    max_fix_attempts = 5

    while True:
        stack_trace = ''
        try:
            tree = parser.suite(response)
        except SyntaxError as e:
            stack_trace += e.msg.strip() + '\n'
            stack_trace += e.text + '\n'
            stack_trace += ' ' * (e.offset - 1) + '^' + '\n'
            max_fix_attempts -= 1
        
        if max_fix_attempts == 0:
            break

        if stack_trace == '':
            break

        response = translate_with_OPENAI(source_skeleton=skeletons[args.from_lang], target_skeleton=skeletons[args.to_lang], is_buggy=True, stack_trace=stack_trace)

    os.makedirs(f"data/responses/GPT-4/{args.project_name}", exist_ok=True)
    with open(f"data/responses/GPT-4/{args.project_name}/{args.class_name}_{args.from_lang}_{args.to_lang}.txt", "w") as f:
        f.write(response)


if __name__ == '__main__':
    load_dotenv()
    parser_ = argparse.ArgumentParser(description='Translate a class skeleton')
    parser_.add_argument('--project_name', type=str, dest='project_name', help='project name')
    parser_.add_argument('--class_name', type=str, dest='class_name', help='class name')
    parser_.add_argument('--from_lang', type=str, dest='from_lang', help='language to translate from')
    parser_.add_argument('--to_lang', type=str, dest='to_lang', help='language to translate to')
    args = parser_.parse_args()
    main(args)
