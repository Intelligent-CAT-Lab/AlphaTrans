import re
import ast


def l0_validation(generation):
    generation = generation.replace('```python', '```')
    pattern = r'```([^`]+)```'
    match = re.search(pattern, generation, re.DOTALL)

    if match:
        try:
            ast.parse('class dummy:\n' + match.group(1))
            print(f'=======================PARSED=======================\n{match.group(1)}\n' + '---' * 50, flush=True)
            return True, match.group(1).split('\n'), None
        except (SyntaxError, MemoryError) as e:
            print(f'=======================PARSE ERROR=======================\n{e}\n' + '---' * 50, flush=True)
            feedback = e
            return False, None, feedback
    else:
        return False, None, 'the model did not generate any code'
