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


def type_mapping(obj: str, target_type: str) -> str:
    # handle arrays separately
    # TODO: This may not work in general
    if target_type.endswith("[]"):        
        return f"IntegrationUtils.valueToArray({obj}, {target_type}.class)"
    
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
    try:
        subprocess.run(['java', '-jar', 'src/compositional_glue_tests/google-java-format-1.20.0-all-deps.jar', '--skip-removing-unused-imports', '-r', file], check=True)
    except Exception as e:
        print(f"Error formatting {file}: {e}")
    return

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
