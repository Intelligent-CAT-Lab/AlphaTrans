import re
import ast


def l0_validation(generation, fragment):
    generation = generation.replace('```python', '```')
    pattern = r'```((?:[^`]|`[^`]|``[^`])*?)```'
    match = re.search(pattern, generation, re.DOTALL)

    if match:
        try:
            output = match.group(1)

            if fragment == 'field': # remove import lines from generation
                generation_lines = output.strip().split('\n')
                if generation_lines[0].strip().startswith('import') or generation_lines[0].strip().startswith('from'):
                    generation_lines = generation_lines[1:]
                output = '\n'.join(generation_lines)

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
