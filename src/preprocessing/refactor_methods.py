import os
import re
import sys

project = sys.argv[1]
os.system(f'rm -rf preprocessed_{project}')
temp_project_path = f'preprocessed_{project}'
os.makedirs(temp_project_path, exist_ok=True)
os.system(f'cp -r java_projects/{project} preprocessed_{project}/')

def get_overloaded_methods():
    methods_query_out = 'data/query_outputs/all_methods.txt'
    methods_lines = []
    with open(methods_query_out, 'r') as f:
        methods_lines = f.readlines()

    overloaded_methods = {}
    all_methods = {}
    for line in methods_lines[2:]:
        res_row = line.split('|')[1:-1]
        class_name, class_location, method_name, method_signature, method_location_start, method_location_end = [x.strip() for x in res_row]

        if class_location == method_location_start:
            continue

        if class_name == method_name: # skip constructors
            continue

        path = method_location_start[method_location_start.find(':')+1:method_location_start.find(':', method_location_start.find(':')+1)]
        path = path[path.find(project):]

        start_line = int(method_location_start[method_location_start.find(':', method_location_start.find(':')+1)+1:].split(':')[0])
        end_line = int(method_location_end[method_location_end.find(':', method_location_end.find(':')+1)+1:].split(':')[2])

        overloaded_methods.setdefault(path, {})
        all_methods.setdefault(path, {})
        overloaded_methods[path].setdefault(method_name, [])
        all_methods[path].setdefault(method_name, [])
        overloaded_methods[path][method_name].append((start_line, end_line, method_signature))
        all_methods[path][method_name].append((start_line, end_line, method_signature))

    for path_ in overloaded_methods.copy():
        for method in overloaded_methods[path_].copy():
            if len(overloaded_methods[path_][method]) == 1:
                overloaded_methods[path_].pop(method)
            else:
                overloaded_methods[path_][method].sort(key=lambda x: x[0])
        
        if len(overloaded_methods[path_]) == 0:
            overloaded_methods.pop(path_)

    for path_ in overloaded_methods:
        for method in overloaded_methods[path_]:

            for start_line, end_line, method_signature in overloaded_methods[path_][method]:

                file_path = f'preprocessed_{project}/' + path_
                with open(file_path, 'r') as f:
                    file_lines = f.readlines()
                
                current_method = file_lines[start_line-1:end_line]
                current_method[0] = current_method[0].replace(method, method + str(overloaded_methods[path_][method].index((start_line, end_line, method_signature))), 1)
                current_method = ''.join(current_method)

                file_lines[start_line-1:end_line] = [current_method]

                with open(file_path, 'w') as f:
                    f.writelines(file_lines)
    
    return overloaded_methods, all_methods


def get_overloaded_method_call_sites(overloaded_methods, all_methods):
    call_graph_query_out = 'data/query_outputs/method_call_graph.txt'
    call_graph_lines = []
    with open(call_graph_query_out, 'r') as f:
        call_graph_lines = f.readlines()

    overloaded_method_locations = {}
    current_index = 2
    while current_index < len(call_graph_lines):

        line = call_graph_lines[current_index]
        res_row = line.split('|')[1:-1]
        method_access_location, method_access_name, method_access_num_params, method_access_argument_location, method_access_signature, caller_name, caller_location, callee_name, callee_location = [x.strip() for x in res_row]

        if caller_location == callee_location:
            current_index += 1
            continue

        if callee_location.endswith(':0:0:0:0'):
            current_index += 1
            continue

        if caller_name in ['<clinit>']:
            current_index += 1
            continue
        
        if method_access_num_params == '0':

            callee_path = callee_location[callee_location.find(':')+1:callee_location.find(':', callee_location.find(':')+1)]
            callee_path = callee_path[callee_path.find(project):]

            caller_path = caller_location[caller_location.find(':')+1:caller_location.find(':', caller_location.find(':')+1)]
            caller_path = caller_path[caller_path.find(project):]

            method_access_path = method_access_location[method_access_location.find(':')+1:method_access_location.find(':', method_access_location.find(':')+1)]
            method_access_path = method_access_path[method_access_path.find(project):]

            caller_start_line = int(caller_location[caller_location.find(':', caller_location.find(':')+1)+1:].split(':')[0])
            callee_start_line = int(callee_location[callee_location.find(':', callee_location.find(':')+1)+1:].split(':')[0])

            method_access_start_line = int(method_access_location[method_access_location.find(':', method_access_location.find(':')+1)+1:].split(':')[0])
            method_access_end_line = int(method_access_location[method_access_location.find(':', method_access_location.find(':')+1)+1:].split(':')[2])

            method_access_start_column = int(method_access_location[method_access_location.find(':', method_access_location.find(':')+1)+1:].split(':')[1])
            method_access_end_column = int(method_access_location[method_access_location.find(':', method_access_location.find(':')+1)+1:].split(':')[3])

            if callee_path in overloaded_methods:

                if callee_name in overloaded_methods[callee_path]:

                    file_lines = []
                    with open(f'preprocessed_{project}/' + method_access_path, 'r') as f:
                        file_lines = f.readlines()

                    caller_method = 0
                    if caller_path in all_methods:
                        for s,e,sign in all_methods[caller_path][caller_name]:
                            if s == caller_start_line:
                                caller_method = (s,e,sign)
                                break
                                        
                    callee_method = 0
                    for s,e,sign in overloaded_methods[callee_path][callee_name]:
                        if s == callee_start_line:
                            callee_method = (s,e,sign)
                            break

                    method_suffix = overloaded_methods[callee_path][callee_name].index(callee_method)
                    target_substring = callee_name + '()'
                    suffixed_target_substring = target_substring.replace(callee_name, callee_name + str(method_suffix), 1)

                    overloaded_method_locations.setdefault(method_access_path, {})
                    overloaded_method_locations[method_access_path].setdefault(caller_name, [])
                    overloaded_method_locations[method_access_path][caller_name].append((target_substring, suffixed_target_substring, method_access_start_line, method_access_end_line))

            current_index += 1
        
        else:

            argument_location = []
            for line in call_graph_lines[current_index:current_index+int(method_access_num_params)]:
                res_row = line.split('|')[1:-1]
                method_access_location, method_access_name, method_access_num_params, method_access_argument_location, method_access_signature, caller_name, caller_location, callee_name, callee_location = [x.strip() for x in res_row]

                callee_path = callee_location[callee_location.find(':')+1:callee_location.find(':', callee_location.find(':')+1)]
                callee_path = callee_path[callee_path.find(project):]

                caller_path = caller_location[caller_location.find(':')+1:caller_location.find(':', caller_location.find(':')+1)]
                caller_path = caller_path[caller_path.find(project):]

                method_access_path = method_access_location[method_access_location.find(':')+1:method_access_location.find(':', method_access_location.find(':')+1)]
                method_access_path = method_access_path[method_access_path.find(project):]

                caller_start_line = int(caller_location[caller_location.find(':', caller_location.find(':')+1)+1:].split(':')[0])
                callee_start_line = int(callee_location[callee_location.find(':', callee_location.find(':')+1)+1:].split(':')[0])

                method_access_start_line = int(method_access_location[method_access_location.find(':', method_access_location.find(':')+1)+1:].split(':')[0])
                method_access_end_line = int(method_access_location[method_access_location.find(':', method_access_location.find(':')+1)+1:].split(':')[2])

                method_access_start_column = int(method_access_location[method_access_location.find(':', method_access_location.find(':')+1)+1:].split(':')[1])
                method_access_end_column = int(method_access_location[method_access_location.find(':', method_access_location.find(':')+1)+1:].split(':')[3])

                method_access_argument_start_line = int(method_access_argument_location[method_access_argument_location.find(':', method_access_argument_location.find(':')+1)+1:].split(':')[0])
                method_access_argument_end_line = int(method_access_argument_location[method_access_argument_location.find(':', method_access_argument_location.find(':')+1)+1:].split(':')[2])
                method_access_argument_start_column = int(method_access_argument_location[method_access_argument_location.find(':', method_access_argument_location.find(':')+1)+1:].split(':')[1])
                method_access_argument_end_column = int(method_access_argument_location[method_access_argument_location.find(':', method_access_argument_location.find(':')+1)+1:].split(':')[3])

                argument_location.append((method_access_argument_start_line, method_access_argument_start_column, method_access_argument_end_line, method_access_argument_end_column))
            
            if callee_path in overloaded_methods:

                if callee_name in overloaded_methods[callee_path]:

                    file_lines = []
                    with open(f'preprocessed_{project}/' + method_access_path, 'r') as f:
                        file_lines = f.readlines()

                    caller_method = 0
                    if caller_path in all_methods:
                        for s,e,sign in all_methods[caller_path][caller_name]:
                            if s == caller_start_line:
                                caller_method = (s,e,sign)
                                break
                                        
                    callee_method = 0
                    for s,e,sign in overloaded_methods[callee_path][callee_name]:
                        if s == callee_start_line:
                            callee_method = (s,e,sign)
                            break

                    method_suffix = overloaded_methods[callee_path][callee_name].index(callee_method)

                    target_substring = callee_name + '('
                    
                    if file_lines[argument_location[0][0]-1][argument_location[0][1]-2] == ' ':
                        target_substring += '\n' + ' ' * (argument_location[0][1] - 1)
                    
                    target_lines = file_lines[argument_location[0][0]-1:argument_location[-1][2]]

                    if len(target_lines) > 1:
                        start_line, start_column = argument_location[0][0], argument_location[0][1]
                        end_line, end_column = argument_location[-1][2], argument_location[-1][3]
                        target_lines = file_lines[start_line-1:end_line]
                        target_lines[0] = target_lines[0][start_column-1:]
                        target_lines[-1] = target_lines[-1][:end_column]
                        target_substring += ''.join(target_lines)
                    else:
                        start_line, start_column = argument_location[0][0], argument_location[0][1]
                        end_line, end_column = argument_location[-1][2], argument_location[-1][3]
                        target_lines = file_lines[start_line-1:end_line]
                        for i in range(start_column-1, end_column):
                            target_substring += target_lines[0][i]

                    try:
                        if file_lines[argument_location[-1][0]-1][argument_location[-1][3]] == '\n':
                            target_substring += '\n'
                            for char in file_lines[argument_location[-1][0]]:
                                if char == ' ':
                                    target_substring += char
                                else:
                                    break
                    except IndexError:
                        pass

                    target_substring = target_substring + ')'
                    suffixed_target_substring = target_substring.replace(callee_name, callee_name + str(method_suffix), 1)

                    overloaded_method_locations.setdefault(method_access_path, {})
                    overloaded_method_locations[method_access_path].setdefault(caller_name, [])
                    overloaded_method_locations[method_access_path][caller_name].append((target_substring, suffixed_target_substring, method_access_start_line, method_access_end_line))

            current_index += int(method_access_num_params)

    return overloaded_method_locations


def rewrite_overloaded_method_calls(overloaded_method_locations):

    for method_access_path in overloaded_method_locations:
        for caller in overloaded_method_locations[method_access_path]:

            for target_substring, suffixed_target_substring, method_access_start_line, method_access_end_line in overloaded_method_locations[method_access_path][caller]:

                file_lines = []
                with open(f'preprocessed_{project}/' + method_access_path, 'r') as f:
                    file_lines = f.readlines()

                caller_method_body = ''.join(file_lines[method_access_start_line-1:method_access_end_line])

                caller_method_body = caller_method_body.replace(target_substring, suffixed_target_substring, 1)

                file_lines[method_access_start_line-1:method_access_end_line] = [caller_method_body]

                with open(f'preprocessed_{project}/' + method_access_path, 'w') as f:
                    f.writelines(file_lines)


def rewrite_overridden_methods(overloaded_methods):
    overridden_methods_query_out = 'data/query_outputs/overridden_methods.txt'
    overridden_methods_lines = []
    with open(overridden_methods_query_out, 'r') as f:
        overridden_methods_lines = f.readlines()

    overridden_methods = {}
    for line in overridden_methods_lines[2:]:
        res_row = line.split('|')[1:-1]
        overridden_method, overridden_method_location, original_method, original_method_location = [x.strip() for x in res_row]
        
        overridden_method_path = overridden_method_location[overridden_method_location.find(':')+1:overridden_method_location.find(':', overridden_method_location.find(':')+1)]
        overridden_method_path = overridden_method_path[overridden_method_path.find(project):]

        original_method_path = original_method_location[original_method_location.find(':')+1:original_method_location.find(':', original_method_location.find(':')+1)]
        original_method_path = original_method_path[original_method_path.find(project):]

        overridden_method_start_line = int(overridden_method_location[overridden_method_location.find(':', overridden_method_location.find(':')+1)+1:].split(':')[0])
        overridden_method_end_line = int(overridden_method_location[overridden_method_location.find(':', overridden_method_location.find(':')+1)+1:].split(':')[2])

        original_method_start_line = int(original_method_location[original_method_location.find(':', original_method_location.find(':')+1)+1:].split(':')[0])
        original_method_end_line = int(original_method_location[original_method_location.find(':', original_method_location.find(':')+1)+1:].split(':')[2])

        index = 0
        if original_method_path in overloaded_methods:
            if original_method in overloaded_methods[original_method_path]:
                for s,e,sign in overloaded_methods[original_method_path][original_method]:
                    if s == original_method_start_line:
                        break
                    index += 1
            else:
                continue
        else:
            continue

        file_lines = []
        with open(f'preprocessed_{project}/' + overridden_method_path, 'r') as f:
            file_lines = f.readlines()

        overridden_method_body = ''.join(file_lines[overridden_method_start_line-1:overridden_method_end_line])
        if re.match(r'.*' + original_method + r'\d\(.*', overridden_method_body):
            continue

        overridden_method_body = overridden_method_body.replace(original_method, original_method + str(index), 1)
        file_lines[overridden_method_start_line-1:overridden_method_end_line] = [overridden_method_body]

        with open(f'preprocessed_{project}/' + overridden_method_path, 'w') as f:
            f.writelines(file_lines)


def main():
    overloaded_methods, all_methods = get_overloaded_methods()
    overloaded_method_locations = get_overloaded_method_call_sites(overloaded_methods, all_methods)
    rewrite_overloaded_method_calls(overloaded_method_locations)
    rewrite_overridden_methods(overloaded_methods)

main()
