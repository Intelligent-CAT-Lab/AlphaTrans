import re
import ast
import json


def syntactic_validation(generation, fragment, args):
    exception_map = json.load(open('data/type_resolution/exception_map.json'))
    constant_map = json.load(open('data/type_resolution/constant_map.json'))

    generation = generation.replace('```python', '```')
    pattern = r'```((?:[^`]|`[^`]|``[^`])*?)```'
    match = re.search(pattern, generation, re.DOTALL)

    if match:
        try:
            output = match.group(1)

            if fragment['fragment_type'] == 'field': # remove import lines from generation
                generation_lines = output.strip().split('\n')
                current_index = 0
                while generation_lines[current_index].strip().startswith('import ') or \
                    generation_lines[current_index].strip().startswith('from ') or \
                    generation_lines[current_index].strip().startswith('class '):
                    
                    current_index += 1
                
                generation_lines = generation_lines[current_index:]
                output = '\n'.join(generation_lines)

            if not output.startswith('    '):
                output = '    ' + output.strip()

            ast.parse('class dummy:\n' + output)

            if args.debug:
                print(f'=======================PARSED=======================\n{output}\n' + '---' * 50, flush=True)

            for key in exception_map:
                if key in output:
                    output = output.replace(key, exception_map[key])
            
            for key in constant_map:
                if key in output:
                    output = output.replace(key, constant_map[key])

            return True, output.split('\n'), None

        except (SyntaxError, MemoryError) as e:
            if args.debug:
                print(f'=======================PARSE ERROR=======================\n{e}\n' + '---' * 50, flush=True)

            feedback = e.msg if hasattr(e, 'msg') else str(e)
            return False, None, feedback
    else:
        return False, None, 'the model did not generate any code'
