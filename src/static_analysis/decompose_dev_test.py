from tree_sitter import Language, Parser
import os
import argparse
import json


def extract_text_by_bytes(code, start_byte, end_byte):
    """
    Extracts text from the code using byte offsets.
    """
    # Get byte sequence from the code
    byte_sequence = code.encode('utf8')
    # Extract the relevant byte range and decode back to string
    text = byte_sequence[start_byte:end_byte].decode('utf8')
    return text.strip()


def get_invoked_expressions(code, node):
    """
    Extracts full method invocation expressions from the syntax tree node.
    """
    expressions = []

    # Recursive helper to build expressions
    def build_expression(node):
        # If the node is a method invocation, we will try to build the full expression
        if node.type == 'method_invocation':
            parts = []
            # Collect method call parts including receiver and arguments
            for child in node.children:
                if child.type == 'identifier':
                    # Append the method name
                    parts.append(extract_text_by_bytes(code, child.start_byte, child.end_byte))
                elif child.type == 'argument_list':
                    # Append the argument list
                    if extract_text_by_bytes(code, child.start_byte, child.end_byte) == '()':
                        parts.append('()')
                    else:
                        parts.append(''.join(extract_text_by_bytes(code, arg.start_byte, arg.end_byte) for arg in child.children))
                else:
                    # For other nodes (e.g., the receiver object), recursively build their expressions
                    parts.append(build_expression(child))
            # Join parts to form the full expression
            return ''.join(parts)
        elif node.type in {'method_invocation', 'identifier'}:
            # Continue building for method chains or identifiers
            return extract_text_by_bytes(code, node.start_byte, node.end_byte) + ''.join(build_expression(child) for child in node.children)
        else:
            # For any other node types, return the extracted text
            return extract_text_by_bytes(code, node.start_byte, node.end_byte)

    # Begin traversal
    if node.type in {'method_invocation', 'identifier'}:
        full_expression = build_expression(node)
        if full_expression:
            expressions.append(full_expression)

    # Recursively check the children
    for child in node.children:
        expressions.extend(get_invoked_expressions(code, child))

    return expressions


def get_invoked_method_names(code, node):
    """
    Extracts all method names from a method invocation node.
    """
    method_names = []

    # Check if the current node is a method invocation and has an identifier child for the method name
    if node.type == 'method_invocation':
        for child in node.children:
            if child.type == 'identifier':
                method_names.append(extract_text_by_bytes(code, child.start_byte, child.end_byte))

    # Recursively check the children for method names
    for child in node.children:
        method_names.extend(get_invoked_method_names(code, child))

    return method_names


def has_method_invocation(code, node, main_application_methods):
    """
    Recursively checks if a node or any of its children contains a method invocation.
    Returns a tuple containing a boolean indicating if a method invocation was found
    and a list of application methods that were invoked.
    """
    found = False
    application_methods = []
    invocation_expressions = []

    if node.type == 'method_invocation':
        # Extract method names
        method_names = get_invoked_method_names(code, node)
        method_expressions = get_invoked_expressions(code, node)
        method_expressions = [x for x in method_expressions if '(' in x]

        for method_name in method_names:
            if method_name in main_application_methods and f'{method_name}(' in extract_text_by_bytes(code, node.start_byte, node.end_byte):
                application_methods.append(method_name)
        
        invocation_expressions.extend(method_expressions)

        # If we found any application methods in this node, set found to True
        if application_methods:
            found = True

    # Check all children and recursively search their children
    for child in node.children:
        child_found, child_application_methods, child_invocation_expressions = has_method_invocation(code, child, main_application_methods)
        
        # If any child node has a method invocation, update found and extend application_methods
        if child_found:
            found = True
            application_methods.extend(child_application_methods)
            invocation_expressions.extend(child_invocation_expressions)

    return found, application_methods, invocation_expressions


def is_assert_statement(code, node):
    """
    Checks if a given statement node is an assert statement.
    """
    if node.type == 'expression_statement':
        # Check if the statement is an assert statement
        for child in node.children:
            if child.type == 'method_invocation':
                method_names = get_invoked_method_names(code, child)
                if any(['assert' in method_name for method_name in method_names]):
                    return True
    return False


def has_constructor_call(code, node, main_application_methods):
    """
    Recursively checks if a node or any of its children contains a constructor call.
    """
    if node.type == 'object_creation_expression':
        # extract class name of instantiated object
        class_name_node = node.child_by_field_name('type')
        class_name = extract_text_by_bytes(code, class_name_node.start_byte, class_name_node.end_byte)
        if '.' in class_name:
            class_name = class_name.split('.')[-1]
        if class_name in main_application_methods:
            return True
        return False

    # Check all children and recursively search their children
    for child in node.children:
        if has_constructor_call(code, child, main_application_methods):
            return True

    return False

def extract_method_statements(node, code, main_application_methods):
    """
    Extracts statements from a given method declaration node.
    Returns a list of statement strings.
    """
    statements = []
    if node.type == 'method_declaration':
        # Extract statements from the method body
        block_node = node.child_by_field_name('body')
        if block_node:
            for statement in block_node.children:
                # Check if the statement is of a type that contains method invocations or declarations
                if statement.type in ['local_variable_declaration'] or statement.type.endswith('statement'):

                    method_invocation = False
                    constructor_call = False
                    assert_statement = False

                    # Check if the child node represents a method invocation
                    status, invoked_methods, invoked_expressions = has_method_invocation(code, statement, main_application_methods)

                    # sort invoked expressions based on length
                    invoked_expressions = list(set(invoked_expressions))
                    invoked_expressions = sorted(invoked_expressions, key=lambda x: len(x))

                    if status:
                        method_invocation = True
                    # Check if the child node represents a constructor call (object creation)
                    if has_constructor_call(code, statement, main_application_methods):
                        constructor_call = True
                    
                    if is_assert_statement(code, statement):
                        assert_statement = True
                    
                    last_index = -1
                    if assert_statement:
                        last_index = -2

                    for expression in invoked_expressions[:last_index]:
                        if '@Override' in extract_text_by_bytes(code, statement.start_byte, statement.end_byte):
                            continue
                        if statement.type in ['try_statement', 'enhanced_for_statement', 'try_with_resources_statement',
                                              'for_statement', 'while_statement', 'if_statement', 'do_statement']:
                            continue
                        if len(set(invoked_methods)) == 1:
                            continue
                        if f'-> {expression}' in extract_text_by_bytes(code, statement.start_byte, statement.end_byte):
                            continue
                        if 'public void' in extract_text_by_bytes(code, statement.start_byte, statement.end_byte):
                            continue

                        expression_invoked_methods = []
                        for method in main_application_methods:
                            if f'{method}(' in expression:
                                expression_invoked_methods.append(method)
                        
                        statements.append({'text': f'{expression};', 'method_invocation': True, 'constructor_call': False, 'assert_statement': False, 'invoked_methods': set(expression_invoked_methods)})

                    # check if the statement has a method invocation
                    statements.append({'text': extract_text_by_bytes(code, statement.start_byte, statement.end_byte),
                                       'method_invocation': method_invocation,
                                       'constructor_call': constructor_call,
                                       'assert_statement': assert_statement,
                                       'invoked_methods': set(invoked_methods)})
                    
    return statements


def is_test_method(test_file, node, code):
    """
    Checks if a given method node is annotated with @Test.
    """
    # Check for annotations preceding the method declaration
    test_status, annotation_text = False, None
    if node.type == 'method_declaration':
        method_name_node = node.child_by_field_name('name')
        method_name = extract_text_by_bytes(code, method_name_node.start_byte, method_name_node.end_byte)
        test_class_path = test_file[test_file.find('src/test/java/')+14:].replace('/', '.').replace('.java', '')
        project_name = test_file.split('/')[2]
        
        with open(f'data/source_test_execution/{project_name}/tests.json', 'r') as f:
            executed_tests = json.load(f)
    
        if test_class_path in executed_tests:
            executed_test_names = executed_tests[test_class_path]
            executed_test_names = [x.split('(')[0] for x in executed_test_names]
            if method_name in executed_test_names:
                test_status = True

    for sibling in node.children:
        if sibling.type == 'modifiers':
            for annotation in sibling.children:
                if annotation.type in ['marker_annotation', 'annotation']:
                    annotation_text = extract_text_by_bytes(code, annotation.start_byte, annotation.end_byte)
                    if '@Test' in annotation_text:
                        test_status = True
    
    return test_status, annotation_text

def is_ignore_method(node, code):
    """
    Checks if a given method node is annotated with @Ignore.
    """
    # Check for annotations preceding the method declaration
    for sibling in node.children:
        if sibling.type == 'modifiers':
            for annotation in sibling.children:
                if annotation.type in ['marker_annotation', 'annotation']:
                    annotation_text = extract_text_by_bytes(code, annotation.start_byte, annotation.end_byte)
                    if '@Ignore' in annotation_text.strip():
                        return True
    return False

def is_disabled_method(node, code):
    """
    Checks if a given method node is annotated with @Disabled.
    """
    # Check for annotations preceding the method declaration
    for sibling in node.children:
        if sibling.type == 'modifiers':
            for annotation in sibling.children:
                if annotation.type in ['marker_annotation', 'annotation']:
                    annotation_text = extract_text_by_bytes(code, annotation.start_byte, annotation.end_byte)
                    if '@Disabled' in annotation_text.strip() or '@EnabledOnOs(OS.WINDOWS)' == annotation_text.strip():
                        return True
    return False


def get_throws(node, code):
    """
    Extracts the exceptions thrown by a method.
    """
    throws = []
    for child in node.children:
        if child.type == 'throws':
            for exception in child.children:
                throws.append(extract_text_by_bytes(code, exception.start_byte, exception.end_byte))
    return throws


def find_test_methods(test_file, node, code, main_application_methods):
    """
    Finds test methods in the AST and extracts their statements.
    Returns a dictionary mapping method names to their list of statement strings.
    """
    methods = {}
    # Search for method declarations in the node's children
    for child in node.children:
        is_test_method_status, annotation_text = is_test_method(test_file, child, code)
        if child.type == 'method_declaration' and is_test_method_status and not is_disabled_method(child, code):
            method_name_node = child.child_by_field_name('name')
            method_name = extract_text_by_bytes(code, method_name_node.start_byte, method_name_node.end_byte)
            # extract throws            
            throws = get_throws(child, code)
            # Extract statements for the test method
            statements = extract_method_statements(child, code, main_application_methods)
            methods[method_name] = {'statements': statements, 'throws': throws, 'annotation': '@Test' if annotation_text is None else annotation_text}
        # Recursively search within nested nodes
        methods.update(find_test_methods(test_file, child, code, main_application_methods))
    return methods

def generate_new_test_methods(method_name, statements_throws, ignore=False):
    """
    Generates new test methods from a list of statements.
    Returns a list of new test method strings.
    """
    new_methods = []
    gobbled_method_statements = []

    i = 0
    while i < len(statements_throws['statements']):
        current_statement = statements_throws['statements'][i]

        # # Rule 1: Handle assertment_statement
        # if current_statement['assert_statement']:
        #     gobbled_method_statements.append([current_statement])

        # Rule 2: Handle constructor_call
        if current_statement['constructor_call']:
            gobbled_method_statements.append([current_statement])

        # Rule 4: Handle method_invocation
        elif current_statement['method_invocation']:
            merged_statements = [current_statement]
            invoked_methods_set = current_statement['invoked_methods']

            # Combine with neighboring dictionaries if invoked_methods matches
            j = i + 1
            while (
                j < len(statements_throws['statements'])
                and statements_throws['statements'][j]['method_invocation']
                and statements_throws['statements'][j]['invoked_methods'] == invoked_methods_set
            ):
                merged_statements.append(statements_throws['statements'][j])
                j += 1

            gobbled_method_statements.append(merged_statements)
            i = j - 1  # Update the index to skip merged statements

        # Rule 3: Combine standalone statements with subsequent statements
        else:
            combined_statements = [current_statement]

            # Look ahead to combine with next statement(s)
            j = i + 1
            while j < len(statements_throws['statements']):
                next_statement = statements_throws['statements'][j]
                if next_statement['assert_statement'] or next_statement['constructor_call'] or next_statement['method_invocation']:
                    # Stop combining if a standalone statement should be separate
                    combined_statements.append(next_statement)
                    j += 1
                    break
                combined_statements.append(next_statement)
                j += 1

            gobbled_method_statements.append(combined_statements)
            i = j - 1  # Update the index to skip combined statements

        i += 1

    # Generate new test methods from the gobbled statements
    for i, statement_group in enumerate(gobbled_method_statements):
        new_method_name = f"{method_name}_test{i}_decomposed"

        accumulated_statements = [x['text'] for group in gobbled_method_statements[:i+1] for x in group]
        method_code = "\n        ".join(accumulated_statements)
        
        if ignore:
            new_method = f"{statements_throws['annotation']}\n    @Ignore\n    public void {new_method_name}() {' '.join(statements_throws['throws'])} {{\n        {method_code}\n    }}"
        else:
            new_method = f"{statements_throws['annotation']}\n    public void {new_method_name}() {' '.join(statements_throws['throws'])} {{\n        {method_code}\n    }}"
        
        new_methods.append(new_method)
    
    return new_methods


def insert_methods_into_class(root_node, methods, code):
    """
    Inserts generated methods into the Java class in the AST and regenerates the Java code.
    """
    class_node = None
    # Find the class declaration node to insert new methods
    for child in root_node.children:
        if child.type == 'class_declaration':
            class_node = child
            break

    if class_node:
        class_start = class_node.start_byte
        class_end = class_node.end_byte

        # Extract existing class content before insertion point
        class_code = extract_text_by_bytes(code, class_start, class_end)

        # Find where to insert methods (before last closing brace of the class)
        insert_pos = class_code.rfind('}')
        class_code = class_code[:insert_pos].strip()

        # Insert new methods before the class closing brace
        new_methods_code = "\n\n    ".join(methods)
        new_class_code = f"{class_code}\n\n    {new_methods_code}\n}}"

        # Replace the class code in the original Java code
        new_java_code = code[:class_start] + new_class_code + code[class_end:]
        return new_java_code

    return code


def get_test_method_bodies(node, code, test_methods):
    """
    Comments out test methods in the AST.
    """
    removed_methods = {}
    # Search for method declarations in the node's children
    for child in node.children:
        if child.type == 'method_declaration':
            method_name_node = child.child_by_field_name('name')
            method_name = extract_text_by_bytes(code, method_name_node.start_byte, method_name_node.end_byte)
            
            if method_name in test_methods:
                method_start = child.start_byte
                method_end = child.end_byte
                method_code = extract_text_by_bytes(code, method_start, method_end)

                removed_methods[method_name] = {'code': method_code}

        # Recursively search within nested nodes
        removed_methods.update(get_test_method_bodies(child, code, test_methods))
    
    return removed_methods


def find_ignored_test_methods(test_file, node, code):
    """
    Finds ignored test methods in the AST and extracts their statements.
    Returns a dictionary mapping method names to their list of statement strings.
    """
    methods = {}
    # Search for method declarations in the node's children
    for child in node.children:
        is_test_method_status, annotation_text = is_test_method(test_file, child, code)
        if child.type == 'method_declaration' and is_ignore_method(child, code) and is_test_method_status:
            method_name_node = child.child_by_field_name('name')
            method_name = extract_text_by_bytes(code, method_name_node.start_byte, method_name_node.end_byte)

            throws = get_throws(child, code)
            # Extract statements for the test method
            statements = extract_method_statements(child, code, [])
            methods[method_name] = {'statements': statements, 'throws': throws, 'annotation': '@Test' if annotation_text is None else annotation_text}
        # Recursively search within nested nodes
        methods.update(find_ignored_test_methods(test_file, child, code))
    return methods


def get_superclass_name(node, code):
    """
    Extracts the superclass name from the class declaration node.
    """
    # Find the class declaration node
    for child in node.children:
        if child.type == 'class_declaration':
            # Look for the superclass specification
            superclass_node = child.child_by_field_name('superclass')
            if superclass_node:
                # Extract and return the superclass name
                superclass_name = extract_text_by_bytes(code, superclass_node.start_byte, superclass_node.end_byte)
                return superclass_name
    return None


def get_class_method_names(node, code):
    """
    Extracts all method names from a class declaration node.
    """
    method_names = []
    # recursively search for method declarations
    for child in node.children:
        if child.type == 'method_declaration' or child.type == 'constructor_declaration':
            method_name_node = child.child_by_field_name('name')
            method_name = extract_text_by_bytes(code, method_name_node.start_byte, method_name_node.end_byte)
            method_names.append(method_name)
        method_names.extend(get_class_method_names(child, code))
    
    return method_names


def get_main_application_methods(args, parser):

    main_application_methods = set()

    src_path = f'java_projects/cleaned_final_projects_decomposed_tests/{args.project_name}/src'
    src_files = []
    for root, dirs, files in os.walk(src_path):
        for file in files:
            if file.endswith('.java') and 'ESTest' not in file and 'scaffolding' not in file:
                src_files.append(os.path.join(root, file))

    for src_file in src_files:
        java_code = ''
        with open(src_file, 'r') as f:
            java_code = f.read()
        
        tree = parser.parse(bytes(java_code, "utf8"))

        for node in tree.root_node.children:
            if node.type == 'class_declaration':
                class_name_node = node.child_by_field_name('name')
                class_name = extract_text_by_bytes(java_code, class_name_node.start_byte, class_name_node.end_byte)
                main_application_methods.add(class_name)

                method_names = get_class_method_names(node, java_code)
                main_application_methods.update(method_names)

    return main_application_methods


def main(args):
    if not os.path.exists('misc/parser/java-language.so'):
        lib_dir = 'misc/sitter-libs'
        libs = [os.path.join(lib_dir, d) for d in os.listdir(lib_dir)]

        Language.build_library(
            # Store the library in the `build` directory
            'misc/parser/java-language.so',
            libs,
        )

    JAVA_LANGUAGE = Language('misc/parser/java-language.so', 'java')
    parser = Parser()
    parser.set_language(JAVA_LANGUAGE)

    test_code_path = f'java_projects/cleaned_final_projects_decomposed_tests/{args.project_name}/src/test'
    # find all test files recursively in the test directory
    test_files = []
    for root, dirs, files in os.walk(test_code_path):
        for file in files:
            if file.endswith('.java'):
                test_files.append(os.path.join(root, file))
    
    main_application_methods = get_main_application_methods(args, parser)
    
    decomposed_method_details = {}
    ignored_test_methods = {}
    for test_file in test_files:

        decomposed_method_details.setdefault(test_file, {})
        ignored_test_methods.setdefault(test_file, {})

        java_code = ''
        with open(test_file, 'r') as f:
            java_code = f.read()

        tree = parser.parse(bytes(java_code, "utf8"))

        root_node = tree.root_node

        ignored_test_methods[test_file] = find_ignored_test_methods(test_file, root_node, java_code)

        # Extract test methods and their statements
        test_methods = find_test_methods(test_file, root_node, java_code, main_application_methods)

        # Generate new test methods for each original method's statements
        all_new_methods = []
        for method_name, statements_throws in test_methods.items():
            new_methods = generate_new_test_methods(method_name, statements_throws)
            decomposed_method_details[test_file][method_name] = new_methods
            all_new_methods.extend(new_methods)

        removed_method_bodies = get_test_method_bodies(root_node, java_code, test_methods)

        for method_name, method_details in removed_method_bodies.items():
            java_code = java_code.replace(method_details['code'], '')

        # Insert the newly generated methods into the class
        new_java_code = insert_methods_into_class(root_node, all_new_methods, java_code)

        # import org.junit.Test;
        new_java_code = new_java_code.split('\n')
        import_line_index = 0
        for line in new_java_code:
            if line.strip().startswith('import') or line.strip().startswith('package'):
                break
            else:
                import_line_index += 1
        
        new_java_code.insert(import_line_index+1, 'import org.junit.Test;') if ('import org.junit.Test;' not in '\n'.join(new_java_code) and 'import org.junit.jupiter.api.Test;' not in '\n'.join(new_java_code)) and '@Test' in '\n'.join(new_java_code) else None
        new_java_code = '\n'.join(new_java_code)

        # Output the newly generated Java code
        with open(test_file, 'w') as f:
            f.write(new_java_code)
    
    for test_file in ignored_test_methods:
        if ignored_test_methods[test_file] == {}:
            continue

        ignored_methods_actual_name = ignored_test_methods[test_file].keys()

        java_code = ''
        with open(test_file, 'r') as f:
            java_code = f.read()

        tree = parser.parse(bytes(java_code, "utf8"))

        root_node = tree.root_node

        super_class = get_superclass_name(root_node, java_code)

        if super_class is None:
            continue

        super_class = super_class.replace('extends', '').strip()
        super_class_test_file = [f for f in test_files if f.endswith(f'{super_class}.java')][0]

        for ignored_method in ignored_methods_actual_name:
            for i in range(len(decomposed_method_details[super_class_test_file][ignored_method])):
                new_ignored_method_body = f'@Test\n    @Ignore\n    public void {ignored_method}_test{i}_decomposed() throws Exception {{\n        // Ignored test method\n    }}\n\n'

                # Insert the newly generated methods into the class. replace the last } with new_ignored_method_body
                java_code = java_code[:java_code.rfind('}')] + new_ignored_method_body + '}'

        # Output the newly generated Java code
        with open(test_file, 'w') as f:
            f.write(java_code)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Decompose Java test methods')
    parser.add_argument('--project_name', type=str, help='Name of the project')
    args = parser.parse_args()
    main(args)
