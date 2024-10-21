import os
import json
from tree_sitter import Language, Parser
import argparse


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

    schemas_path = f'data/schemas{args.suffix}/{args.project_name}/'

    for schema_file in os.listdir(schemas_path):

        data = {}
        with open(f'{schemas_path}/{schema_file}', 'r') as f:
            data = json.load(f)

        for class_ in data['classes']:
            if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                continue

            global_variables = {}
            current_class = class_
            
            for field_ in data['classes'][current_class]['fields']:
                name = field_.split(':')[1]
                type_ = data['classes'][current_class]['fields'][field_]['types']
                assert len(type_) == 1
                global_variables[name] = type_[0][0]

            while data['classes'][current_class]['nested_inside'] != []:
                
                current_class = data['classes'][current_class]['nested_inside']

                for field_ in data['classes'][current_class]['fields']:
                    name = field_.split(':')[1]
                    type_ = data['classes'][current_class]['fields'][field_]['types']
                    assert len(type_) == 1
                    global_variables[name] = type_[0][0]
            
            for method_ in data['classes'][class_]['methods']:

                method_body = ''.join(data['classes'][class_]['methods'][method_]['body'])
                non_library_calls = [c[2].split(':')[1] for c in data['classes'][class_]['methods'][method_]['calls'] if ':' in c[2]]

                library_call_map = {}
                local_variables = {}
                code_constructs = []

                tree = parser.parse(bytes(method_body, "utf8"))
                root_node = tree.root_node

                def extract_api_calls(node):

                    if node.type.endswith('_statement'):
                        code_constructs.append(node.type) if node.type not in code_constructs else None

                    if node.type == 'method_invocation':
                        method_name_node = node.child_by_field_name('name')
                        receiver_node = node.child_by_field_name('object')
                        
                        if receiver_node:
                            class_name = receiver_node.text.decode('utf-8')
                        else:
                            class_name = 'unknown'
                        
                        if method_name_node and method_name_node.text.decode('utf-8') not in non_library_calls:
                            method_name = method_name_node.text.decode('utf-8')
                            library_call_map.setdefault(class_name, [])
                            library_call_map[class_name].append(method_name) if method_name not in library_call_map[class_name] else None
                    
                    # # Handle object instantiation and track variable-class mappings
                    # if node.type == 'object_creation_expression':
                    #     type_node = node.child_by_field_name('type')
                    #     variable_node = node.parent.child_by_field_name('name')  # Find the variable being assigned
                        
                    #     if type_node and variable_node:
                    #         class_name = type_node.text.decode('utf-8')
                    #         variable_name = variable_node.text.decode('utf-8')
                    #         # Store the variable and its class in the map
                    #         local_variables[variable_name] = class_name
                    #         # print(f"Class instantiation: {class_name}, Variable: {variable_name}")

                    if node.type == 'local_variable_declaration':
                        declarators = node.named_children[1:]
                        type_node = node.child_by_field_name('type')
                        if type_node:
                            class_name = type_node.text.decode('utf-8')
                            for declarator in declarators:
                                variable_node = declarator.child_by_field_name('name')
                                if variable_node:
                                    variable_name = variable_node.text.decode('utf-8')
                                    local_variables[variable_name] = class_name
                    
                    if node.type == 'formal_parameter':
                        type_node = node.child_by_field_name('type')
                        if type_node:
                            class_name = type_node.text.decode('utf-8')
                            variable_name = node.child_by_field_name('name').text.decode('utf-8')
                            local_variables[variable_name] = class_name

                    for child in node.children:
                        extract_api_calls(child)

                extract_api_calls(root_node)

                # print('Global Variables:', global_variables)
                # print('Local Variables:', local_variables)
                # print('Library calls:', library_call_map)
                # print('Code constructs:', code_constructs)
                # print('----------------------------------------------')

                # data['classes'][class_]['methods'][method_]['global_variables'] = global_variables
                # data['classes'][class_]['methods'][method_]['local_variables'] = local_variables
                # data['classes'][class_]['methods'][method_]['library_calls'] = library_call_map
                data['classes'][class_]['methods'][method_]['code_constructs'] = code_constructs
        
        with open(f'{schemas_path}/{schema_file}', 'w') as f:
            json.dump(data, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract Java API from a project')
    parser.add_argument('--project_name', type=str, required=True, help='Name of the project')
    parser.add_argument('--suffix', type=str, help='suffix')
    args = parser.parse_args()
    main(args)
