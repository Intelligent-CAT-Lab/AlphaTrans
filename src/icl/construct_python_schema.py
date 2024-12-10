import json
import os
import argparse
from tree_sitter import Language, Parser


def extract_text_by_bytes(code, start_byte, end_byte):
    """
    Extracts text from the code using byte offsets.
    """
    # Get byte sequence from the code
    byte_sequence = code.encode('utf8')
    # Extract the relevant byte range and decode back to string
    text = byte_sequence[start_byte:end_byte].decode('utf8')
    return text.strip()


def extract_classes_and_methods(filename, parser):
    # Read the Python file
    with open(filename, 'r') as f:
        source_code = f.read()

    # Parse the code using Tree-sitter
    tree = parser.parse(bytes(source_code, "utf8"))
    root_node = tree.root_node

    classes_and_methods = {}

    # Traverse the syntax tree
    def traverse_node(node, parent_class=None):
        if node.type == 'class_definition':
            # Extract class name
            class_name_node = node.child_by_field_name('name')
            class_name = extract_text_by_bytes(source_code, class_name_node.start_byte, class_name_node.end_byte)
            # Initialize empty method list for the class
            classes_and_methods[class_name] = {}

            # Traverse the class body to find methods
            class_body_node = node.child_by_field_name('body')
            for child in class_body_node.children:
                traverse_node(child, class_name)

        elif node.type == 'function_definition' and parent_class:
            # Extract method name
            method_name_node = node.child_by_field_name('name')
            method_name = extract_text_by_bytes(source_code, method_name_node.start_byte, method_name_node.end_byte)
            
            # Extract method signature (including parameters)
            signature_start = node.start_byte
            signature_end = node.child_by_field_name('body').start_byte  # end of signature is start of body
            method_signature = extract_text_by_bytes(source_code, signature_start, signature_end)

            # Extract method body
            method_body_node = node.child_by_field_name('body')
            method_body = extract_text_by_bytes(source_code, method_body_node.start_byte, method_body_node.end_byte)

            # Store method name and body in a dictionary
            classes_and_methods[parent_class].setdefault(method_name, {})
            classes_and_methods[parent_class][method_name]['method_signature'] = "    " + method_signature
            classes_and_methods[parent_class][method_name]['method_body'] = ("    " + method_signature).split('\n') + ("        " + method_body).split('\n')

        # Traverse children nodes recursively
        for child in node.children:
            traverse_node(child, parent_class)

    # Start traversal from the root node
    traverse_node(root_node)

    return classes_and_methods


def main(args):

    lib_dir = 'misc/sitter-libs'
    libs = [os.path.join(lib_dir, d) for d in os.listdir(lib_dir)]

    # Build the Python grammar
    Language.build_library(
        'misc/parser/my-languages.so',  # Output library
        libs  # Grammar for Python
    )

    PY_LANGUAGE = Language('misc/parser/my-languages.so', 'python')

    # Initialize the parser with Python language
    parser = Parser()
    parser.set_language(PY_LANGUAGE)

    os.makedirs('data/icl_pool', exist_ok=True)
    for project_name in ['commons-csv', 'commons-fileupload', 'commons-validator', 'commons-cli']:

        for type_ in ['manual', 'partial']:

            test_code_path = f'data/manually_verified_translations/{project_name}/{type_}_translation/src/'
            # find all test files recursively in the test directory
            source_files = []
            for root, dirs, files in os.walk(test_code_path):
                for file in files:
                    if file.endswith('.py'):
                        source_files.append(os.path.join(root, file))

            analysis_results = {}
            for filename in source_files:
                result = extract_classes_and_methods(filename, parser)
                formatted_filename = filename[filename.find('src/'):]
                analysis_results[formatted_filename] = result

            with open(f'data/icl_pool/{project_name}_analysis_results_{type_}.json', 'w') as f:
                json.dump(analysis_results, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Construct Python schema for ICL pool')
    args = parser.parse_args()
    main(args)
