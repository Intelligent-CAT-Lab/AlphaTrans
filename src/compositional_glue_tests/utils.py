import subprocess
import json
from src.compositional_glue_tests.constants import *


class default_type_value_class(dict):
    constants = {
        "char": "'\\0'",
        "int": "0",
        "boolean": "false",
        "float": "0",
        "double": "0",
        "long": "0",
    }
    
    def __getitem__(self, key):
        if key in self.constants:
            return self.constants[key]
        
        return "null"
    
default_type_value = default_type_value_class()

IMMUTABLES =  ['int', 'double', 'float', 'long', 'boolean', 'char', 'String']


def type_mapping(obj: str, target_type: str, include_idMap=False, calling_from_python=False) -> str:
    # handle arrays separately
    # TODO: This may not work in general
    if target_type.endswith("[]"):        
        if calling_from_python:
            return obj
        else:
            return f"IntegrationUtils.valueToArray({obj}, {target_type}.class)"
    
    if include_idMap:
        if calling_from_python:
            return obj # TODO: include idMap
        else:
            return f"IntegrationUtils.valueToObject({obj}, \"{target_type}\", idMap)"
    
    if calling_from_python:
        return f"JavaHandler.valueToObject({obj}, \"{target_type}\")"
    else:
        return f"IntegrationUtils.valueToObject({obj}, \"{target_type}\")"

# load type handling information
with open('src/compositional_glue_tests/type_handling.json') as f:
    type_handling = json.load(f)
    
# load exception handling information
with open('src/compositional_glue_tests/exception_handling.json') as f:
    exception_handling = json.load(f)

def write_to_file(file, content):
    with open(file, "w") as f:
        f.write(content)

    # format java file
    if file.endswith(".java"):
        try:
            subprocess.run(['java', '-jar', 'src/compositional_glue_tests/google-java-format-1.20.0-all-deps.jar', '--skip-removing-unused-imports', '-r', file], check=True)
        except Exception as e:
            print(f"Error formatting {file}: {e}")

def pre_order_traversal(relation: list[tuple[str, str | None]]) -> list[str]:
    """
    Performs a pre-order traversal of the tree represented by the parent list

    Args:
        parent_list: A list of tuples representing parent relations (child, parent).
        The parent of the root node should be None. There should be only one root node.

    Returns:
        A list containing the nodes visited in pre-order.
    """
    visited = []
    
    root = [child for child, parent in relation if parent is None][0]
    stack = [root]

    while stack:
        current_node = stack.pop()
        visited.append(current_node)

        children = [child for child, parent in relation if parent == current_node]
        stack.extend(children[::-1])  # Add children in reverse order for pre-order

    return visited


def get_java_class_declaration(schema_data: dict, class_name: str):
    java_class_declaration = None
    with open(schema_data['path'], 'r') as f:
        lst = f.readlines()
        start = schema_data['classes'][class_name]['start']
        end = schema_data['classes'][class_name]['end']
        java_class_declaration = "".join(lst[start-1:end])
        
        # if the declaration does not contain a '{', look at more lines
        # since the schema may not be correct
        if "{" not in java_class_declaration:
            # find the first line with '{'
            extension = ""
            for i in range(end, len(lst)):
                if "{" in lst[i]:
                    extension += lst[i][:lst[i].index("{")+1]
                    break
                extension += lst[i]
            
            java_class_declaration += extension
        
        # if the declaration ends in '}', remove it
        if java_class_declaration.strip().endswith("}"):
            java_class_declaration = java_class_declaration.strip()[0:-1]
        
    return java_class_declaration


def get_method_parameter_types(method_schema_data: dict):
    """
    Returns a list of types of the method parameters.    
    (Adapted from Ali's create_skeleton.py::split_with_nested_commas)
    """
    s = method_schema_data["signature"][method_schema_data["signature"].find('(')+1:method_schema_data["signature"].find(')')]
    
    result = []
    stack = []
    start = 0

    for i, c in enumerate(s):
        if c == ',' and not stack:
            result.append(s[start:i].strip())
            start = i + 1
        elif c == '<':
            stack.append(c)
        elif c == '>':
            stack.pop()

    result.append(s[start:].strip())
    return list(filter(None, result))
