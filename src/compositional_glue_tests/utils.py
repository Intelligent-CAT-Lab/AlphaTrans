from collections import defaultdict
import subprocess
import json
from constants import *

default_type_value = defaultdict(lambda: "null")
default_type_value.update({
    "int": "0",
    "boolean": "false",
    "float": "0",
    "double": "0",
    "long": "0",
})

# load type handling information
with open('src/compositional_glue_tests/type_handling.json') as f:
    type_handling = json.load(f) 


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
