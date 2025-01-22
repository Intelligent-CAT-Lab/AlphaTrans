import re
import ast
import json
from typing import Optional


class MethodExtractor:
    """Extracts a Python method that matches a given signature."""
    
    def __init__(self, source_code: str):
        """
        Initialize with source code to analyze.
        
        Args:
            source_code (str): Python source code containing the method
        """
        self.source_code = source_code
        self.tree = ast.parse(source_code)
    
    def parse_signature(self, signature: str) -> tuple:
        """
        Parse a method signature string into its components.
        
        Args:
            signature (str): Method signature like "def method(arg: type) -> return_type:"
            
        Returns:
            tuple: (method_name, args_string, return_type)
        """
        # Remove 'def' and any whitespace
        signature = signature.strip()
        if signature.startswith('def '):
            signature = signature[4:].strip()
            
        # Extract method name and arguments
        match = re.match(r'(\w+)\s*\((.*?)\)\s*(?:->\s*([^:]+)\s*)?:', signature)
        if not match:
            raise ValueError("Invalid method signature format")
            
        method_name = match.group(1)
        args_string = match.group(2).strip()
        return_type = match.group(3).strip() if match.group(3) else None
        
        return method_name, args_string, return_type
    
    def extract_method(self, signature: str) -> Optional[str]:
        """
        Extract a method matching the given signature.
        
        Args:
            signature (str): The complete method signature to match
            
        Returns:
            Optional[str]: The extracted method or None if not found
        """
        try:
            method_name, args_string, return_type = self.parse_signature(signature)
        except ValueError as e:
            print(f"Error parsing signature: {e}")
            return None
            
        class MethodVisitor(ast.NodeVisitor):
            def __init__(self, target_name: str, source_code: str):
                self.target_name = target_name
                self.found_method = None
                self.source_lines = source_code.splitlines()
            
            def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
                if node.name == self.target_name:
                    # Extract the method's source code
                    start_line = node.lineno - 1
                    end_line = node.end_lineno
                    method_lines = self.source_lines[start_line:end_line]
                    self.found_method = '\n'.join(method_lines)
        
        visitor = MethodVisitor(method_name, self.source_code)
        visitor.visit(self.tree)
        return visitor.found_method
    

def syntactic_validation(generation, fragment, args, signature):
    exception_map = json.load(open('data/type_resolution/exception_map.json'))
    constant_map = json.load(open('data/type_resolution/constant_map.json'))

    generation = generation.replace('```python', '```')
    pattern = r'```((?:[^`]|`[^`]|``[^`])*?)```'
    match = re.search(pattern, generation, re.DOTALL)

    if match:
        try:
            output = match.group(1)

            has_annotation = False
            if signature is not None and '@staticmethod' in signature:
                has_annotation = True
                signature = signature.replace('@staticmethod', '')
                output = output.replace('@staticmethod', '')

            if signature is not None:

                if output.strip().startswith('def '):
                    output = f'class dummy:\n    {output}'

                method_extractor = MethodExtractor(output)
                extracted_method = method_extractor.extract_method(signature)
                if extracted_method is not None:
                    output = extracted_method
                else:
                    return False, None, 'the model did not generate any code'

            if fragment['fragment_type'] == 'field': # remove import lines from generation
                generation_lines = output.strip().split('\n')
                current_index = 0
                while generation_lines[current_index].strip().startswith('import ') or \
                    generation_lines[current_index].strip().startswith('from ') or \
                    generation_lines[current_index].strip().startswith('class '):
                    
                    current_index += 1
                
                generation_lines = generation_lines[current_index:]
                output = '\n'.join(generation_lines)

                if '=' not in output:
                    return False, None, 'the model did not generate any code'

            if not output.startswith('    '):
                output = '    ' + output.strip()
            
            if has_annotation:
                output = '    @staticmethod\n' + output

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
