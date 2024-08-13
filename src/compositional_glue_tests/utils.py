import subprocess
import json
import re
from src.compositional_glue_tests.constants import *


IMMUTABLES =  ['int', 'double', 'float', 'long', 'boolean', 'char', 'String']


def type_mapping(obj: str, target_type: str, include_idMap=False, calling_from_python=False, target_object=None, idMap_name="idMap") -> str:
    """
    Return the code to convert a python Value to a Java object.
    
    obj: The python Value (expression) to be converted.
    target_type: The target Java type.
    include_idMap: If True, include idMap in the conversion.
    calling_from_python: Whether this will be called from Python (so that the JavaHandler is used).
    target_object: The target object which will receive the converted value.    
    """
    target_type_reduced = None

    # handle arrays separately
    if target_type.endswith("[]"):
        if calling_from_python:
            return obj # TODO: handle arrays in Python when doing the conversion! (remove this line)

        # if the target type is an array, ensure there is no <...> in the type
        if "<" in target_type:
            target_type = target_type[:target_type.index("<")] + "[]"
          
        target_type_reduced = target_type[:-2].strip()
    
    caller = "JavaHandler.valueToObject" if calling_from_python else "IntegrationUtils.valueToObject"

    return "{caller}({args})".format(
        caller=caller,
        args=", ".join([
            obj,
            f'"{target_type}"'
        ]
        + ([idMap_name] if include_idMap else [])
        + ([f'{target_type_reduced}.class'] if target_type_reduced else [])
        + ([target_object] if target_object else [])
    ))

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


def topological_sort(graph: list[tuple[str, str]]) -> list[str]:
    """
    Provides a topological sort of the graph.

    Args:
        graph: A list of tuples where each tuple contains two strings representing the source and target nodes.

    Returns:
        A list of strings representing the nodes in topological order.
    """
    # create a dictionary with the nodes as keys and their dependencies as values
    graph_dict = {}
    for edge in graph:
        if edge[0] not in graph_dict:
            graph_dict[edge[0]] = []
        graph_dict[edge[0]].append(edge[1])

    # create a dictionary with the nodes as keys and their indegree as values
    indegree_dict = {}
    for edge in graph:
        if edge[1] not in indegree_dict:
            indegree_dict[edge[1]] = 0
        if edge[0] not in indegree_dict:
            indegree_dict[edge[0]] = 0
        indegree_dict[edge[1]] += 1

    # create a list of nodes with indegree 0
    zero_indegree = [node for node in indegree_dict if indegree_dict[node] == 0]

    # create a list to store the sorted nodes
    sorted_nodes = []

    # loop over the nodes with indegree 0
    while zero_indegree:
        node = zero_indegree.pop()
        sorted_nodes.append(node)

        # loop over the nodes that depend on the current node
        if node in graph_dict:
            for dependent_node in graph_dict[node]:
                indegree_dict[dependent_node] -= 1
                if indegree_dict[dependent_node] == 0:
                    zero_indegree.append(dependent_node)

    return sorted_nodes


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


def schema_filter(schema_file_name: str):
    schema_name = schema_file_name.split('.')[-2].split('_python_partial')[0].strip()
    return (schema_file_name.endswith('_python_partial.json')
        and (
            'src.main.' in schema_file_name # consider only the main schemas
            or ('src.test.' in schema_file_name and 'Test' not in schema_name) # or test schemas without 'Test' in their name
        ))


def get_enum_field_body(field_name: str, field_schema: dict, schema_data: dict) -> str:
    """
    Returns the body of an enum field after traversing the class body
    to capture any trailing ';'.
    """
    with open(schema_data['path'], 'r') as f:
        lst = f.readlines()

    start = field_schema['start']
    end = field_schema['end']
    field_body = "".join(lst[start-1:end])

    field_body = publicize_methods_of_anoymous_classes(field_body)

    # return immediately if the field body ends with ';'
    if field_body.strip().endswith(";"):
        return field_body

    # loop over all the lines until we find a non-empty line
    i = end
    line = lst[i]
    while not line.strip():
        i += 1
        line = lst[i]
    
    # check what the first non-whitespace character is
    if line.strip()[0] == ';':
        field_body += ';'       
            
    return field_body


def publicize_methods_of_anoymous_classes(body: str) -> str:
    """
    Publicize methods of anonymous classes.
    """
    # find overridden methods in the field body (if the field is an anonymous class)
    if "@Override" in body:
        # get all positions of @Override in the field body
        override_pos = [m.start() for m in re.finditer('@Override', body)]
        
        for pos in override_pos:
            # get the method signature
            method_signature_start = pos + len("@Override")
            method_signature_end = body.find("{", method_signature_start)
            method_signature = body[method_signature_start:method_signature_end].strip()
            
            # check if the method is public and make it so if it is not
            if "public" not in method_signature:
                # check if the method was private or protected
                if "private" in method_signature:
                    method_signature = method_signature.replace("private", "public")
                elif "protected" in method_signature:
                    method_signature = method_signature.replace("protected", "public")
                else:
                    method_signature = "public " + method_signature
                    
            body = body[:method_signature_start] + "\n" + method_signature + body[method_signature_end:]

    return body


def add_obj_to_clone_method(method_content: str, class_obj: dict) -> str:
    """
    Modify the method body (assuming that the method is a clone method) to account
    for the embedded python object too.
    """
    clone_method_content = [] # this list will be flattened later

    # first search for all return statements and get their positions
    return_statement_matches = re.compile(r"return\s+.*;").finditer(method_content)

    for return_statement_match in return_statement_matches:
        return_statement = return_statement_match.group()
        return_statement_start_pos = return_statement_match.start()
        return_statement_end_pos = return_statement_match.end()

        return_value = return_statement[6:-1].strip()
        
        # check if the return value already has a type cast to the class itself
        if not return_value.startswith("(" + class_obj["name"]):
            # and if not, perform the cast
            return_value = f"({class_obj['name']}) " + return_value

        handling_code = f"""{class_obj['name']} cloneResult = {return_value};
        if (cloneResult != null) {{
            cloneResult.setPythonObject(IntegrationUtils.createDefaultPythonObject({class_obj['classref']}));
            cloneResult.jToPy();
        }}"""

        clone_method_content.extend([
            method_content[:return_statement_start_pos],
            handling_code,
            "return cloneResult;",
            method_content[return_statement_end_pos:]
        ])

    return "".join(clone_method_content)
