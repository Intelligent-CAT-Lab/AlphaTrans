import json
import os
from src.icl.construct_icl_pool import extract_complex_statements
from tree_sitter import Language, Parser


def rank_icl(project_name, k, sort_by, suffix, identifier):
    prefix_ = f'data/schemas{suffix}'
    schemas_path = f'{prefix_}/{project_name}/'

    icl_pool = {}
    with open('data/icl_pool/icl_pool.json', 'r') as f:
        icl_pool = json.load(f)
    
    icl_pool = [x for x in icl_pool if x['project_name'] != project_name]

    icl_library_calls = {i: [f'{x[1]}.{x[2]}' for x in icl_pool[i]['library_calls'] if x[0] == 'library'] for i in range(len(icl_pool))}

    icl_ranks = {i: 0 for i in range(len(icl_pool))}

    total_fragments = 0
    total_no_api_calls = 0
    total_no_code_constructs = 0
    matched_fragments = 0
    total_matched_icls = 0

    matched_icl = []

    for schema_file in os.listdir(schemas_path):

        if 'ESTest' in schema_file:
            continue

        data = {}
        with open(f'{schemas_path}/{schema_file}', 'r') as f:
            data = json.load(f)

        for class_ in data['classes']:

            if 'new' in class_ or '{' in class_: # skip nested and nameless classes
                continue

            for method_ in data['classes'][class_]['methods']:

                if identifier != f"{schema_file.replace('.json', '')}|{class_}|{method_}":
                    continue

                total_fragments += 1
                
                library_calls = [x for x in data['classes'][class_]['methods'][method_]['calls'] if x[0] == 'library']
                library_calls_list = [f'{x[1]}.{x[2]}' for x in library_calls]

                if library_calls_list == []:
                    total_no_api_calls += 1
                    continue

                # print(schema_file, class_, method_)
                # print('source code:')
                # print(''.join(data['classes'][class_]['methods'][method_]['body']))
                
                if sort_by == 'library_api':

                    for i in range(len(icl_pool)):

                        # print(set(icl_library_calls[i]), set(library_calls_list))
                        icl_ranks[i] = len(set(icl_library_calls[i]) & set(library_calls_list))

                        if icl_ranks[i] != 0:
                            total_matched_icls += 1
                    
                    icl_ranks = {k: v for k, v in sorted(icl_ranks.items(), key=lambda item: item[1], reverse=True)}

                    # print('library calls:', library_calls_list)
                    # print('$' * 50)
                    # print('matched icls:')
                    counted = False
                    for i, j in list(icl_ranks.items())[:k]:
                        if j != 0 and not counted:
                            matched_fragments += 1
                            counted = True
                        
                        matched_icl.append(icl_pool[i])
                        # print(library_calls_list)
                        # print(icl_library_calls[i])
                        # print(icl_ranks[i])
                        # print('\n'.join(icl_pool[i]['source_code']))
                        # print('matching library calls:', set(icl_library_calls[i]) & set(library_calls_list))
                        # print('#' * 50)

                elif sort_by == 'code_constructs':
                    source_code = ''.join(data['classes'][class_]['methods'][method_]['body'])

                    # extract cc later in schemas
                    JAVA_LANGUAGE = Language('misc/parser/my-languages.so', 'java')
                    parser = Parser()
                    parser.set_language(JAVA_LANGUAGE)

                    tree = parser.parse(bytes(source_code, 'utf-8'))                    
                    statements = extract_complex_statements(tree.root_node, bytes(source_code, 'utf-8'))

                    code_constructs_list = [x['label'] for x in statements]

                    if code_constructs_list == []:
                        total_no_code_constructs += 1
                        continue

                    for i in range(len(icl_pool)):                        

                        icl_ranks[i] = len(set(icl_pool[i]['code_constructs'].keys()) & set(code_constructs_list))

                        if icl_ranks[i] != 0:
                            total_matched_icls += 1
                    
                    icl_ranks = {k: v for k, v in sorted(icl_ranks.items(), key=lambda item: item[1], reverse=True)}

                    # print('code constructs:', code_constructs_list)
                    # print('$' * 50)
                    # print('matched icls:')
                    counted = False
                    for i, j in list(icl_ranks.items())[:k]:
                        if j != 0 and not counted:
                            matched_fragments += 1
                            counted = True
                        
                        matched_icl.append(icl_pool[i])
                        # print('\n'.join(icl_pool[i]['source_code']))
                        # print('matching code constructs:', set(icl_pool[i]['code_constructs'].keys()) & set(code_constructs_list))
                        # print('#' * 50)

                # print('\n\n\n\n\n\n\n\n------------------------\n\n\n\n\n\n\n\n')
    
    # print(f'total_fragments: {total_fragments}')
    # print(f'matched_fragments: {matched_fragments}')
    # print(f'total_no_api_calls: {total_no_api_calls}')
    # print(f'% matched: {round((matched_fragments / total_fragments) * 100, 2)}')
    # print(f'% total_no_api_calls: {round((total_no_api_calls / total_fragments) * 100, 2)}')
    # print(f'% total_no_code_constructs: {round((total_no_code_constructs / total_fragments) * 100, 2)}')
    # print(f'% total_matched_icls: {round(total_matched_icls / total_fragments, 2)}')

    return matched_icl


if __name__ == '__main__':
    res = rank_icl('commons-cli', 1, 'library_api', '_decomposed_tests', 'commons-cli.src.main.org.apache.commons.cli.CommandLine|CommandLine|438-440:iterator')
    print(res)
    print(len(res))
