import re
import ast


def l0_validation(generation):
    generation = generation.replace('```python', '```')
    pattern = r'```((?:[^`]|`[^`]|``[^`])*?)```'
    match = re.search(pattern, generation, re.DOTALL)

    if match:
        try:
            output = match.group(1)
            if not output.startswith('    '):
                output = '    ' + output.strip()
            ast.parse('class dummy:\n' + output)
            print(f'=======================PARSED=======================\n{output}\n' + '---' * 50, flush=True)
            return True, output.split('\n'), None
        except (SyntaxError, MemoryError) as e:
            print(f'=======================PARSE ERROR=======================\n{e}\n' + '---' * 50, flush=True)
            feedback = e
            return False, None, feedback
    else:
        return False, None, 'the model did not generate any code'
