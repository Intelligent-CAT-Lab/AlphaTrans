import sys
import os

projects_dir = sys.argv[1]
project = sys.argv[2]
os.system(f'rm -rf java_projects/preprocessed_1/{project}')
temp_project_path = f'java_projects/preprocessed_1/'
os.makedirs(temp_project_path, exist_ok=True)
os.system(f'cp -r {projects_dir}/{project} {temp_project_path}')


def get_args(line):
    arguments = []
    inside_string = False
    inside_parenthesis = False
    arg = ''
    for char in line[line.find('(')+1:]:
        if (char == '"' or char == "'"):
            if len(arg) > 0 and arg[-1] != "\\":
                inside_string = not inside_string
                arg += char
                continue
            else:
                arg += char
                inside_string = not inside_string
                continue

        if char == '(' and not inside_string and not inside_parenthesis:
            arg += char
            inside_parenthesis = not inside_parenthesis
            continue            
        if char == ')' and not inside_string and inside_parenthesis:
            arg += char
            inside_parenthesis = not inside_parenthesis
            continue
        if char == ',' and not inside_string and not inside_parenthesis:
            arguments.append(arg.strip())
            arg = ''
            continue
        if char == ')' and not inside_string and not inside_parenthesis:
            arguments.append(arg.strip())
            arg = ''
            break
        
        arg += char

    return arguments


def get_overloaded_constructors():
    constructors_lines = []
    with open(f'data/query_outputs/{project}/{project}_all_constructors.txt', 'r') as f:
        constructors_lines = f.readlines()

    constructors_lines = [x for x in constructors_lines if x.split('|')[7].strip() in ['super(...)', 'this(...)']]

    overloaded_constructors = {}
    index = 0
    while index < len(constructors_lines):    
        line = constructors_lines[index]
        res_row = line.split('|')[1:-1]
        constructor_name, constructor_location_start, constructor_location_end, constructor_signature, num_params, param_location, call, call_location = [x.strip() for x in res_row]

        if constructor_name.strip() == '':
            index += 1
            continue

        if num_params == '0':

            path = constructor_location_start[constructor_location_start.find(':')+1:constructor_location_start.find(':', constructor_location_start.find(':')+1)]
            path = path[path.find(f'/{project}/')+1:]

            with open(temp_project_path + '/' + path, 'r') as f:
                file_lines = f.readlines()

            constructor_start_line = int(constructor_location_start[constructor_location_start.find(':', constructor_location_start.find(':')+1)+1:].split(':')[0])
            constructor_end_line = int(constructor_location_end[constructor_location_end.find(':', constructor_location_end.find(':')+1)+1:].split(':')[2])

            call_location = call_location[call_location.find(':', call_location.find(':')+1)+1:].split(':')

            overloaded_constructors.setdefault(path, {})
            overloaded_constructors[path].setdefault(constructor_signature, {})
            overloaded_constructors[path][constructor_signature]['constructor_start_line'] = constructor_start_line
            overloaded_constructors[path][constructor_signature]['constructor_end_line'] = constructor_end_line
            overloaded_constructors[path][constructor_signature]['constructor_parameters'] = []
            overloaded_constructors[path][constructor_signature]['constructor_content_lines'] = file_lines[constructor_start_line-1:constructor_end_line]
            overloaded_constructors[path][constructor_signature]['calling_method'] = call
            overloaded_constructors[path][constructor_signature]['call_site_start_line'] = int(call_location[0])
            overloaded_constructors[path][constructor_signature]['call_site_start_col'] = int(call_location[1])
            overloaded_constructors[path][constructor_signature]['call_site_end_line'] = int(call_location[2])
            overloaded_constructors[path][constructor_signature]['call_site_end_col'] = int(call_location[3])
            overloaded_constructors[path][constructor_signature]['call_site_lines'] = file_lines[int(call_location[0])-1:int(call_location[2])]
            index += 1

        else:

            for line in constructors_lines[index:index+int(num_params)]:
                res_row = line.split('|')[1:-1]
                constructor_name, constructor_location_start, constructor_location_end, constructor_signature, num_params, param_location, call, call_location = [x.strip() for x in res_row]

                path = constructor_location_start[constructor_location_start.find(':')+1:constructor_location_start.find(':', constructor_location_start.find(':')+1)]
                path = path[path.find(f'/{project}/')+1:]

                with open(temp_project_path + '/' + path, 'r') as f:
                    file_lines = f.readlines()

                constructor_start_line = int(constructor_location_start[constructor_location_start.find(':', constructor_location_start.find(':')+1)+1:].split(':')[0])
                constructor_end_line = int(constructor_location_end[constructor_location_end.find(':', constructor_location_end.find(':')+1)+1:].split(':')[2])

                param_location = param_location[param_location.find(':', param_location.find(':')+1)+1:].split(':')
                call_location = call_location[call_location.find(':', call_location.find(':')+1)+1:].split(':')

                overloaded_constructors.setdefault(path, {})
                overloaded_constructors[path].setdefault(constructor_signature, {})
                overloaded_constructors[path][constructor_signature]['constructor_start_line'] = constructor_start_line
                overloaded_constructors[path][constructor_signature]['constructor_end_line'] = constructor_end_line
                overloaded_constructors[path][constructor_signature].setdefault('constructor_parameters', [])
                overloaded_constructors[path][constructor_signature]['constructor_parameters'].append(''.join(file_lines[int(param_location[0])-1:int(param_location[2])])[int(param_location[1])-1:int(param_location[3])])
                overloaded_constructors[path][constructor_signature]['constructor_content_lines'] = file_lines[constructor_start_line-1:constructor_end_line]
                overloaded_constructors[path][constructor_signature]['calling_method'] = call
                overloaded_constructors[path][constructor_signature]['call_site_start_line'] = int(call_location[0])
                overloaded_constructors[path][constructor_signature]['call_site_start_col'] = int(call_location[1])
                overloaded_constructors[path][constructor_signature]['call_site_end_line'] = int(call_location[2])
                overloaded_constructors[path][constructor_signature]['call_site_end_col'] = int(call_location[3])
                overloaded_constructors[path][constructor_signature][f'call_site_lines'] = file_lines[int(call_location[0])-1:int(call_location[2])]

            index += int(num_params)


    for path in overloaded_constructors.copy():
        key_freqs = {}
        for constructor in overloaded_constructors[path].copy():
            constructor_name = constructor.split('(')[0]
            key_freqs.setdefault(constructor_name, 0)
            key_freqs[constructor_name] += 1

        constructor_id = 0
        for constructor in overloaded_constructors[path].copy():
            constructor_name = constructor.split('(')[0]
            if key_freqs[constructor_name] == 1:
                del overloaded_constructors[path][constructor]

                if len(overloaded_constructors[path]) == 0:
                    del overloaded_constructors[path]            
            else:
                overloaded_constructors[path][constructor]['constructor_id'] = constructor_id
                constructor_id += 1

    return overloaded_constructors


def get_constructor_call_sites():
    constructor_call_graph_lines = []
    with open(f'data/query_outputs/{project}/{project}_constructor_call_graph.txt', 'r') as f:
        constructor_call_graph_lines = f.readlines()

    constructor_call_sites = {}
    index = 0
    while index < len(constructor_call_graph_lines):
        line = constructor_call_graph_lines[index]
        res_row = line.split('|')[1:-1]
        _, called_constructor_signature, constructor_call_location, num_args, _ = [x.strip() for x in res_row]

        if num_args == '0':
            path = constructor_call_location[constructor_call_location.find(':')+1:constructor_call_location.find(':', constructor_call_location.find(':')+1)]
            path = path[path.find(f'/{project}/')+1:]

            with open(temp_project_path + '/' + path, 'r') as f:
                file_lines = f.readlines()

            constructor_call_location = constructor_call_location[constructor_call_location.find(':', constructor_call_location.find(':')+1)+1:].split(':')

            constructor_call_sites.setdefault(path, {})
            unique_key = f'{constructor_call_location[0]}.{constructor_call_location[1]}.{constructor_call_location[2]}.{constructor_call_location[3]}'
            constructor_call_sites[path].setdefault(unique_key, {})

            constructor_call_sites[path][unique_key]['constructor_call_site_lines'] = file_lines[int(constructor_call_location[0])-1:int(constructor_call_location[2])]
            constructor_call_sites[path][unique_key]['constructor_call_site_start_line'] = int(constructor_call_location[0])
            constructor_call_sites[path][unique_key]['constructor_call_site_start_col'] = int(constructor_call_location[1])
            constructor_call_sites[path][unique_key]['constructor_call_site_end_line'] = int(constructor_call_location[2])
            constructor_call_sites[path][unique_key]['constructor_call_site_end_col'] = int(constructor_call_location[3])
            constructor_call_sites[path][unique_key]['called_constructor_signature'] = called_constructor_signature
            constructor_call_sites[path][unique_key]['constructor_call_arugments'] = []

            index += 1
        
        else:
            for line in constructor_call_graph_lines[index:index+int(num_args)]:
                res_row = line.split('|')[1:-1]
                _, called_constructor_signature, constructor_call_location, num_args, argument_location = [x.strip() for x in res_row]

                path = constructor_call_location[constructor_call_location.find(':')+1:constructor_call_location.find(':', constructor_call_location.find(':')+1)]
                path = path[path.find(f'/{project}/')+1:]

                with open(temp_project_path + '/' + path, 'r') as f:
                    file_lines = f.readlines()
                
                constructor_call_location = constructor_call_location[constructor_call_location.find(':', constructor_call_location.find(':')+1)+1:].split(':')
                argument_location = argument_location[argument_location.find(':', argument_location.find(':')+1)+1:].split(':')

                constructor_call_sites.setdefault(path, {})
                unique_key = f'{constructor_call_location[0]}.{constructor_call_location[1]}.{constructor_call_location[2]}.{constructor_call_location[3]}'
                constructor_call_sites[path].setdefault(unique_key, {})
                
                constructor_call_sites[path][unique_key]['constructor_call_site_lines'] = file_lines[int(constructor_call_location[0])-1:int(constructor_call_location[2])]
                constructor_call_sites[path][unique_key]['constructor_call_site_start_line'] = int(constructor_call_location[0])
                constructor_call_sites[path][unique_key]['constructor_call_site_start_col'] = int(constructor_call_location[1])
                constructor_call_sites[path][unique_key]['constructor_call_site_end_line'] = int(constructor_call_location[2])
                constructor_call_sites[path][unique_key]['constructor_call_site_end_col'] = int(constructor_call_location[3])
                constructor_call_sites[path][unique_key]['called_constructor_signature'] = called_constructor_signature
                constructor_call_sites[path][unique_key].setdefault('constructor_call_arugments', [])

                if argument_location[0] == argument_location[2]:
                    constructor_call_sites[path][unique_key]['constructor_call_arugments'].append(''.join(file_lines[int(argument_location[0])-1:int(argument_location[2])])[int(argument_location[1])-1:int(argument_location[3])])
                else:
                    argument_lines = file_lines[int(argument_location[0])-1:int(argument_location[2])]
                    argument_lines[0] = argument_lines[0][int(argument_location[1])-1:]
                    argument_lines[-1] = argument_lines[-1][:int(argument_location[3])]
                    constructor_call_sites[path][unique_key]['constructor_call_arugments'].append(''.join(argument_lines))
            
            index += int(num_args)

    return constructor_call_sites


def rewrite_overloaded_constructors(overloaded_constructors):

    new_constructors = {}
    single_statement_dependent_constructors = {}
    single_statement_super_constructors = {}
    multiple_statement_dependent_constructors = {}
    independent_constructors = {}
    parameters_union = {}

    for path in overloaded_constructors:
        parameters_union.setdefault(path, [])

        for overloaded_constructor in overloaded_constructors[path]:
            parameters_union[path].extend(overloaded_constructors[path][overloaded_constructor]['constructor_parameters'])

            overloaded_constructor_body = ''.join(overloaded_constructors[path][overloaded_constructor]['constructor_content_lines'])
            overloaded_constructor_body_statements = []
            current_statement = []
            for l in overloaded_constructor_body[overloaded_constructor_body.find('{')+1:overloaded_constructor_body.rfind('}')].split('\n'):
                if l.strip() == '':
                    continue

                if l.endswith(';'):
                    current_statement.append(l)
                    overloaded_constructor_body_statements.append(current_statement)
                    current_statement = []
                elif l.endswith('}'):
                    if current_statement != []:
                        current_statement.append(l)
                        overloaded_constructor_body_statements.append(current_statement)
                        current_statement = []
                    else:
                        overloaded_constructor_body_statements[-1].append(l)
                else:
                    current_statement.append(l)

            if len(overloaded_constructor_body_statements) == 1 and 'this(' in overloaded_constructor_body:

                single_statement_dependent_constructors.setdefault(path, {})
                overloaded_constructors[path][overloaded_constructor]['body_statements'] = overloaded_constructor_body_statements
                single_statement_dependent_constructors[path][overloaded_constructor] = overloaded_constructors[path][overloaded_constructor]
            
            if len(overloaded_constructor_body_statements) == 1 and 'super(' in overloaded_constructor_body:
                    
                single_statement_super_constructors.setdefault(path, {})
                overloaded_constructors[path][overloaded_constructor]['body_statements'] = overloaded_constructor_body_statements
                single_statement_super_constructors[path][overloaded_constructor] = overloaded_constructors[path][overloaded_constructor]

            if len(overloaded_constructor_body_statements) > 1 and 'this(' in overloaded_constructor_body:

                multiple_statement_dependent_constructors.setdefault(path, {})
                overloaded_constructors[path][overloaded_constructor]['body_statements'] = overloaded_constructor_body_statements                
                multiple_statement_dependent_constructors[path][overloaded_constructor] = overloaded_constructors[path][overloaded_constructor]

            if 'this(' not in overloaded_constructor_body and 'super(' not in overloaded_constructor_body:
                    
                independent_constructors.setdefault(path, {})
                independent_constructors[path][overloaded_constructor] = overloaded_constructors[path][overloaded_constructor]

        parameters_union = {k:list(set(v)) for k,v in parameters_union.items()}

    # <rule 0> if there are n constructors, and at least 1 constructor is independent, then remove independent constructors and add them to new constructor
    for path in independent_constructors:
        for overloaded_constructor in independent_constructors[path]:

            if 'rewrite_details' in independent_constructors[path][overloaded_constructor]:
                raise Exception('rewrite_details already exists')

            independent_constructors[path][overloaded_constructor].setdefault('rewrite_details', {})
            independent_constructors[path][overloaded_constructor]['rewrite_details']['action'] = 'comment'
            independent_constructors[path][overloaded_constructor]['rewrite_details']['overloaded_constructor_type'] = 'independent'
            independent_constructors[path][overloaded_constructor]['rewrite_details']['called_constructor'] = 'none'

            new_constructors.setdefault(path, {})
            new_constructors[path][overloaded_constructor] = independent_constructors[path][overloaded_constructor]
    # <rule 0> ends here

    # <rule 1> if there are n constructors, and at least 1 constructor is single statement dependent, then rewrite the single statement dependent constructors as static methods
    for path in single_statement_dependent_constructors:
        called_constructor = None
        for overloaded_constructor in overloaded_constructors[path]:
            if overloaded_constructor not in single_statement_dependent_constructors[path] \
                and set(overloaded_constructors[path][overloaded_constructor]['constructor_parameters']) == set(parameters_union[path]) \
                and len(single_statement_dependent_constructors[path]) + 1 == len(overloaded_constructors[path]):

                called_constructor = overloaded_constructor
                break

        for overloaded_constructor in single_statement_dependent_constructors[path]:
            if 'rewrite_details' in single_statement_dependent_constructors[path][overloaded_constructor]:
                raise Exception('rewrite_details already exists')

            single_statement_dependent_constructors[path][overloaded_constructor].setdefault('rewrite_details', {})
            single_statement_dependent_constructors[path][overloaded_constructor]['rewrite_details']['action'] = 'static method'
            single_statement_dependent_constructors[path][overloaded_constructor]['rewrite_details']['overloaded_constructor_type'] = 'single statement dependent'
            single_statement_dependent_constructors[path][overloaded_constructor]['rewrite_details']['called_constructor'] = called_constructor

        if called_constructor is None:
            continue

        overloaded_constructors[path][called_constructor].setdefault('rewrite_details', {})
        overloaded_constructors[path][called_constructor]['rewrite_details']['action'] = 'public constructor'
        overloaded_constructors[path][called_constructor]['rewrite_details']['overloaded_constructor_type'] = 'single statement constructor callee'
        overloaded_constructors[path][called_constructor]['rewrite_details']['called_constructor'] = 'none'

        new_constructors.setdefault(path, {})
        new_constructors[path][called_constructor] = overloaded_constructors[path][called_constructor]
    # <rule 1> ends here

    # <rule 1.1> if there are n constructors, and all constructors are single statement super, then rewrite the single statement super constructor with least params as static methods
    for path in single_statement_super_constructors:

        if not len(single_statement_super_constructors[path].keys()) == 2:
            continue

        least_param_constructor = [100, None]
        most_param_constructor = [0, None]
        for overloaded_constructor in single_statement_super_constructors[path]:
            if len(single_statement_super_constructors[path][overloaded_constructor]['constructor_parameters']) < least_param_constructor[0]:
                least_param_constructor[0] = len(single_statement_super_constructors[path][overloaded_constructor]['constructor_parameters'])
                least_param_constructor[1] = overloaded_constructor
            if len(single_statement_super_constructors[path][overloaded_constructor]['constructor_parameters']) > most_param_constructor[0]:
                most_param_constructor[0] = len(single_statement_super_constructors[path][overloaded_constructor]['constructor_parameters'])
                most_param_constructor[1] = overloaded_constructor

        overloaded_constructors[path][least_param_constructor[1]].setdefault('rewrite_details', {})
        overloaded_constructors[path][least_param_constructor[1]]['rewrite_details']['action'] = 'static method'
        overloaded_constructors[path][least_param_constructor[1]]['rewrite_details']['overloaded_constructor_type'] = 'single statement dependent'
        overloaded_constructors[path][least_param_constructor[1]]['rewrite_details']['called_constructor'] = most_param_constructor[1]
        params = ', '.join([x.split()[-1] for x in overloaded_constructors[path][least_param_constructor[1]]['constructor_parameters']])
        null_params = params
        for i in range(most_param_constructor[0] - least_param_constructor[0]):
            null_params += ', null'
        overloaded_constructors[path][least_param_constructor[1]]['constructor_content_lines'][1] = overloaded_constructors[path][least_param_constructor[1]]['constructor_content_lines'][1].replace(f'super({params});', f'this({null_params});')

        overloaded_constructors[path][most_param_constructor[1]].setdefault('rewrite_details', {})
        overloaded_constructors[path][most_param_constructor[1]]['rewrite_details']['action'] = 'public constructor'
        overloaded_constructors[path][most_param_constructor[1]]['rewrite_details']['overloaded_constructor_type'] = 'single statement constructor callee'
        overloaded_constructors[path][most_param_constructor[1]]['rewrite_details']['called_constructor'] = 'none'

        new_constructors.setdefault(path, {})
        new_constructors[path][most_param_constructor[1]] = overloaded_constructors[path][most_param_constructor[1]]
    # <rule 1.1> ends here

    # <rule 2> if there are n constructors, and at least 1 constructor is multiple statement dependent, then remove multiple statement dependent constructors and add a factory method
    for path in multiple_statement_dependent_constructors:
        called_constructor = None
        for overloaded_constructor in overloaded_constructors[path]:
            if overloaded_constructor not in multiple_statement_dependent_constructors[path] \
                and len(multiple_statement_dependent_constructors[path]) + 1 == len(overloaded_constructors[path]):

                called_constructor = overloaded_constructor
                break

        if called_constructor is None:
            continue

        for overloaded_constructor in multiple_statement_dependent_constructors[path]:
            if 'rewrite_details' in multiple_statement_dependent_constructors[path][overloaded_constructor]:
                raise Exception('rewrite_details already exists')

            multiple_statement_dependent_constructors[path][overloaded_constructor].setdefault('rewrite_details', {})
            multiple_statement_dependent_constructors[path][overloaded_constructor]['rewrite_details']['action'] = 'factory method'
            multiple_statement_dependent_constructors[path][overloaded_constructor]['rewrite_details']['overloaded_constructor_type'] = 'multiple statement dependent'
            multiple_statement_dependent_constructors[path][overloaded_constructor]['rewrite_details']['called_constructor'] = called_constructor

        if 'rewrite_details' in overloaded_constructors[path][called_constructor]:
            raise Exception('rewrite_details already exists')

        overloaded_constructors[path][called_constructor].setdefault('rewrite_details', {})
        overloaded_constructors[path][called_constructor]['rewrite_details']['action'] = 'factory method callee'
        overloaded_constructors[path][called_constructor]['rewrite_details']['overloaded_constructor_type'] = 'multiple statement constructor callee'
        overloaded_constructors[path][called_constructor]['rewrite_details']['called_constructor'] = 'none'

        new_constructors.setdefault(path, {})
        new_constructors[path][called_constructor] = overloaded_constructors[path][called_constructor]
    # <rule 2> ends here

    for path in overloaded_constructors:

        all_independent = True
        for overloaded_constructor in overloaded_constructors[path]:
            if 'rewrite_details' not in overloaded_constructors[path][overloaded_constructor]:
                raise Exception('rewrite_details not found')
        
            if overloaded_constructors[path][overloaded_constructor]['rewrite_details']['overloaded_constructor_type'] != 'independent':
                all_independent = False
                break
        
        if all_independent:

            new_constructors[path]['new_constructor'] = {}
            new_constructors[path]['new_constructor']['new_constructor_body'] = []
            new_parameters = ['int constructorId'] + parameters_union[path]
            new_constructors[path]['new_constructor']['new_constructor_body'].append(f'public {path.split("/")[-1].split(".")[0]}({", ".join(new_parameters)}) {{\n')

            keys = list(overloaded_constructors[path].keys())
            first_overloaded_constructor = keys[0]
            last_overloaded_constructor = keys[-1]
            new_constructors[path]['new_constructor']['new_constructor_body'].append(f'    if (constructorId == {overloaded_constructors[path][first_overloaded_constructor]["constructor_id"]}) {{\n')
            constructor_content_raw = ''.join(overloaded_constructors[path][first_overloaded_constructor]['constructor_content_lines'])
            new_constructors[path]['new_constructor']['new_constructor_body'].append(constructor_content_raw[constructor_content_raw.find('{')+1:constructor_content_raw.rfind('}')])
            new_constructors[path]['new_constructor']['new_constructor_body'].append('    }\n')

            for overloaded_constructor in overloaded_constructors[path]:
                if overloaded_constructor == first_overloaded_constructor or overloaded_constructor == last_overloaded_constructor:
                    continue
                new_constructors[path]['new_constructor']['new_constructor_body'].append(f'    else if (constructorId == {overloaded_constructors[path][overloaded_constructor]["constructor_id"]}) {{\n')
                constructor_content_raw = ''.join(overloaded_constructors[path][overloaded_constructor]['constructor_content_lines'])
                new_constructors[path]['new_constructor']['new_constructor_body'].append(constructor_content_raw[constructor_content_raw.find('{')+1:constructor_content_raw.rfind('}')])
                new_constructors[path]['new_constructor']['new_constructor_body'].append('    }\n')

            new_constructors[path]['new_constructor']['new_constructor_body'].append('    else {\n')
            constructor_content_raw = ''.join(overloaded_constructors[path][last_overloaded_constructor]['constructor_content_lines'])
            new_constructors[path]['new_constructor']['new_constructor_body'].append(constructor_content_raw[constructor_content_raw.find('{')+1:constructor_content_raw.rfind('}')])
            new_constructors[path]['new_constructor']['new_constructor_body'].append('    }\n')
            new_constructors[path]['new_constructor']['new_constructor_body'].append('}\n')
            new_constructors[path]['new_constructor']['new_constructor_signature'] = new_parameters

            continue

        all_single_statement_dependent = False
        called_constructor = None
        for overloaded_constructor in overloaded_constructors[path]:
            if 'rewrite_details' not in overloaded_constructors[path][overloaded_constructor]:
                raise Exception('rewrite_details not found')
        
            if overloaded_constructors[path][overloaded_constructor]['rewrite_details']['overloaded_constructor_type'] == 'single statement constructor callee' \
                and overloaded_constructors[path][overloaded_constructor]['rewrite_details']['action'] == 'public constructor':
                all_single_statement_dependent = True
                called_constructor = overloaded_constructor
                break
        
        if all_single_statement_dependent:

            new_constructors[path]['new_constructor'] = {}
            new_constructors[path]['new_constructor']['new_constructor_body'] = []

            new_parameters = ['int constructorId'] + parameters_union[path]
            constructor_name = called_constructor.split('(')[0]
            overloaded_constructors[path][called_constructor]['constructor_content_lines'][0] = overloaded_constructors[path][called_constructor]['constructor_content_lines'][0].replace('private ' + constructor_name, 'public ' + constructor_name)

            new_constructors[path]['new_constructor']['new_constructor_body'].extend(overloaded_constructors[path][called_constructor]['constructor_content_lines'])

            for overloaded_constructor in overloaded_constructors[path]:
                if overloaded_constructor == called_constructor:
                    continue
                overloaded_constructor_body = ''.join(overloaded_constructors[path][overloaded_constructor]['constructor_content_lines'])
                overloaded_constructor_body = overloaded_constructor_body.replace('public ' + constructor_name, f'public static {constructor_name} {constructor_name}{overloaded_constructors[path][overloaded_constructor]["constructor_id"]}')
                overloaded_constructor_body = overloaded_constructor_body.replace('this(', f'return new {constructor_name}(')
                new_constructors[path]['new_constructor']['new_constructor_body'].extend(overloaded_constructor_body)
            
            new_constructors[path]['new_constructor']['new_constructor_signature'] = new_parameters

            continue

        all_multiple_statement_dependent = False
        called_constructor = None
        for overloaded_constructor in overloaded_constructors[path]:
            if 'rewrite_details' not in overloaded_constructors[path][overloaded_constructor]:
                raise Exception('rewrite_details not found')
        
            if overloaded_constructors[path][overloaded_constructor]['rewrite_details']['overloaded_constructor_type'] == 'multiple statement constructor callee' \
                and overloaded_constructors[path][overloaded_constructor]['rewrite_details']['action'] == 'factory method callee':
                all_multiple_statement_dependent = True
                called_constructor = overloaded_constructor
                break
        
        if all_multiple_statement_dependent:

            new_constructors[path]['new_constructor'] = {}
            new_constructors[path]['new_constructor']['new_constructor_body'] = []

            new_parameters = ['int constructorId'] + parameters_union[path]
            constructor_name = called_constructor.split('(')[0]
            new_constructors[path]['new_constructor']['new_constructor_body'].append(f'public {path.split("/")[-1].split(".")[0]}({", ".join(new_parameters)}) {{\n')

            called_constructor_body = ''.join(overloaded_constructors[path][called_constructor]['constructor_content_lines'])
            new_constructors[path]['new_constructor']['new_constructor_body'].append(called_constructor_body[called_constructor_body.find('{')+1:called_constructor_body.rfind('}')])

            this_statement_body = []
            this_constructor = ''
            for overloaded_constructor in overloaded_constructors[path]:

                if overloaded_constructor == called_constructor:
                    continue

                body_without_this_statement = []
                for statement in overloaded_constructors[path][overloaded_constructor]['body_statements']:
                    is_this_statement = False
                    for partial_statement in statement:
                        if 'this(' in partial_statement:
                            is_this_statement = True
                            this_statement_body.extend(statement)
                            this_constructor = overloaded_constructor
                            break
                    if not is_this_statement:
                        body_without_this_statement.extend(statement)

                new_constructors[path]['new_constructor']['new_constructor_body'].append(f'    if (constructorId == {overloaded_constructors[path][overloaded_constructor]["constructor_id"]}) {{\n')
                constructor_content_raw = ''.join(overloaded_constructors[path][overloaded_constructor]['constructor_content_lines'])
                new_constructors[path]['new_constructor']['new_constructor_body'].extend(body_without_this_statement)
                new_constructors[path]['new_constructor']['new_constructor_body'].append('    }\n')
            
            new_constructors[path]['new_constructor']['new_constructor_body'].append('}\n')

            new_constructors[path]['new_constructor']['new_constructor_body'].append(f'public static {constructor_name} {constructor_name}{overloaded_constructors[path][this_constructor]["constructor_id"]}({", ".join(new_parameters)}) {{\n')
            new_constructors[path]['new_constructor']['new_constructor_body'].append(f'    if (constructorId == {overloaded_constructors[path][this_constructor]["constructor_id"]}) {{\n')
            old_constructor_args = get_args(''.join(this_statement_body))

            index_map = {element: index for index, element in enumerate(new_parameters)}

            target_constructor_old_params = overloaded_constructors[path][called_constructor]['constructor_parameters'].copy()

            for i in range(len(new_parameters)):
                if new_parameters[i] not in overloaded_constructors[path][called_constructor]['constructor_parameters']:
                    old_constructor_args.insert(i, new_parameters[i].split()[-1])
                    overloaded_constructors[path][called_constructor]['constructor_parameters'].insert(i, new_parameters[i])

            new_constructor_args = [new_parameters[x].split()[-1] for x in range(len(new_parameters))]

            for i in range(len(new_parameters)):
                if new_parameters[i] in overloaded_constructors[path][called_constructor]['constructor_parameters']:
                    new_constructor_args[i] = old_constructor_args[index_map[overloaded_constructors[path][called_constructor]['constructor_parameters'][i]]]
                if 'boolean' in new_parameters[i] and new_constructor_args[i] == 'null':
                    new_constructor_args[i] = 'false'

            overloaded_constructors[path][called_constructor]['constructor_parameters'] = target_constructor_old_params

            new_constructors[path]['new_constructor']['new_constructor_body'].append(f'        return new {constructor_name}({", ".join(new_constructor_args)});\n')
            new_constructors[path]['new_constructor']['new_constructor_body'].append('    }\n')

            default_parameters = [new_parameters[x].split()[-1] for x in range(len(new_parameters))]
            new_constructors[path]['new_constructor']['new_constructor_body'].append(f'return new {constructor_name}({", ".join(default_parameters)});\n')
            new_constructors[path]['new_constructor']['new_constructor_body'].append('}\n')

            new_constructors[path]['new_constructor']['new_constructor_signature'] = new_parameters
            continue

        some_independent = False
        for overloaded_constructor in overloaded_constructors[path]:
            if 'rewrite_details' not in overloaded_constructors[path][overloaded_constructor]:
                raise Exception('rewrite_details not found')
        
            if overloaded_constructors[path][overloaded_constructor]['rewrite_details']['overloaded_constructor_type'] == 'independent':
                some_independent = True
                break
        
        if some_independent:

            new_constructors[path]['new_constructor'] = {}
            new_constructors[path]['new_constructor']['new_constructor_body'] = []

            new_parameters = ['int constructorId'] + parameters_union[path]

            new_constructors[path]['new_constructor']['new_constructor_body'].append(f'public {path.split("/")[-1].split(".")[0]}({", ".join(new_parameters)}) {{\n')

            keys = list(overloaded_constructors[path].keys())
            keys = [x for x in keys if overloaded_constructors[path][x]['rewrite_details']['overloaded_constructor_type'] == 'independent']
            first_overloaded_constructor = keys[0]
            last_overloaded_constructor = keys[-1]

            new_constructors[path]['new_constructor']['new_constructor_body'].append(f'    if (constructorId == {overloaded_constructors[path][first_overloaded_constructor]["constructor_id"]}) {{\n')
            constructor_content_raw = ''.join(overloaded_constructors[path][first_overloaded_constructor]['constructor_content_lines'])
            new_constructors[path]['new_constructor']['new_constructor_body'].append(constructor_content_raw[constructor_content_raw.find('{')+1:constructor_content_raw.rfind('}')])

            for overloaded_constructor in overloaded_constructors[path]:
                if overloaded_constructor == first_overloaded_constructor or overloaded_constructor == last_overloaded_constructor:
                    continue
                if overloaded_constructors[path][overloaded_constructor]['rewrite_details']['overloaded_constructor_type'] != 'independent':
                    continue
                new_constructors[path]['new_constructor']['new_constructor_body'].append(f'    else if (constructorId == {overloaded_constructors[path][overloaded_constructor]["constructor_id"]}) {{\n')
                constructor_content_raw = ''.join(overloaded_constructors[path][overloaded_constructor]['constructor_content_lines'])
                new_constructors[path]['new_constructor']['new_constructor_body'].append(constructor_content_raw[constructor_content_raw.find('{')+1:constructor_content_raw.rfind('}')])
            
            new_constructors[path]['new_constructor']['new_constructor_body'].append('    }\n')

            new_constructors[path]['new_constructor']['new_constructor_body'].append('    else {\n')
            constructor_content_raw = ''.join(overloaded_constructors[path][last_overloaded_constructor]['constructor_content_lines'])
            new_constructors[path]['new_constructor']['new_constructor_body'].append(constructor_content_raw[constructor_content_raw.find('{')+1:constructor_content_raw.rfind('}')])
            new_constructors[path]['new_constructor']['new_constructor_body'].append('    }\n')
            new_constructors[path]['new_constructor']['new_constructor_body'].append('}\n')

            dependent_constructors = [x for x in overloaded_constructors[path] if overloaded_constructors[path][x]['rewrite_details']['overloaded_constructor_type'] != 'independent']
            
            for overloaded_constructor in dependent_constructors:

                constructor_name = overloaded_constructor.split('(')[0]
                raw_constructor_body = ''.join(overloaded_constructors[path][overloaded_constructor]['constructor_content_lines'])

                this_statement_body = raw_constructor_body[raw_constructor_body.find('{')+1:raw_constructor_body.rfind('}')].split('\n')
                old_constructor_args = get_args(''.join(this_statement_body))

                called_constructor = None
                for overloaded_constructor_ in overloaded_constructors[path]:
                    if overloaded_constructor_ == overloaded_constructor:
                        continue

                    if overloaded_constructors[path][overloaded_constructor_]['rewrite_details']['overloaded_constructor_type'] == 'independent' \
                        and len(overloaded_constructors[path][overloaded_constructor_]['constructor_parameters']) == len(old_constructor_args):
                        called_constructor = overloaded_constructor_
                        break

                target_constructor_old_params = overloaded_constructors[path][called_constructor]['constructor_parameters'].copy()
                for i in range(len(new_parameters)):
                    if new_parameters[i] not in overloaded_constructors[path][called_constructor]['constructor_parameters']:
                        old_constructor_args.insert(i, 'null')
                        overloaded_constructors[path][called_constructor]['constructor_parameters'].insert(i, new_parameters[i])

                index_map = {element: index for index, element in enumerate(overloaded_constructors[path][called_constructor]['constructor_parameters'])}

                new_constructor_args = ['null' for x in range(len(new_parameters))]
                for i in range(len(new_parameters)):
                    if new_parameters[i] in overloaded_constructors[path][called_constructor]['constructor_parameters']:
                        new_constructor_args[i] = old_constructor_args[index_map[new_parameters[i]]]
                    if 'boolean' in new_parameters[i] and new_constructor_args[i] == 'null':
                        new_constructor_args[i] = 'false'

                overloaded_constructors[path][called_constructor]['constructor_parameters'] = target_constructor_old_params

                raw_constructor_body = raw_constructor_body.replace(f'public {constructor_name}', f'public static {constructor_name} {constructor_name}{overloaded_constructors[path][overloaded_constructor]["constructor_id"]}')
                raw_constructor_body = raw_constructor_body.replace(''.join(this_statement_body).strip(), f'return new {constructor_name}({overloaded_constructors[path][called_constructor]["constructor_id"]}, {", ".join(new_constructor_args[1:])});\n')

                new_constructors[path]['new_constructor']['new_constructor_body'].append(raw_constructor_body)

            new_constructors[path]['new_constructor']['new_constructor_signature'] = new_parameters
            continue

    return overloaded_constructors, new_constructors


def rewrite_call_sites(overloaded_constructors, constructor_call_sites, new_constructors):

    for path in constructor_call_sites:

        for location in constructor_call_sites[path]:
            start_line, start_col, end_line, end_col = [int(x) for x in location.split('.')]
            constructor_call_site_lines = constructor_call_sites[path][location]['constructor_call_site_lines']
            called_constructor_signature = constructor_call_sites[path][location]['called_constructor_signature']
            constructor_call_arugments = constructor_call_sites[path][location]['constructor_call_arugments']

            called_constructor = None
            called_constructor_path = None

            for path_ in overloaded_constructors:
                if called_constructor_signature in overloaded_constructors[path_]:
                    called_constructor = overloaded_constructors[path_][called_constructor_signature]
                    called_constructor_path = path_
                    break
            
            if called_constructor is None:
                continue

            if overloaded_constructors[called_constructor_path][called_constructor_signature]['rewrite_details']['overloaded_constructor_type'] == 'multiple statement dependent' \
            and overloaded_constructors[called_constructor_path][called_constructor_signature]['rewrite_details']['action'] == 'factory method':
                                
                new_parameters = new_constructors[called_constructor_path]['new_constructor']['new_constructor_signature']
                old_constructor_args = constructor_call_arugments.copy()

                index_map = {element: index for index, element in enumerate(new_parameters)}

                target_constructor_old_params = overloaded_constructors[called_constructor_path][called_constructor_signature]['constructor_parameters'].copy()
                for i in range(len(new_parameters)):
                    if new_parameters[i] not in overloaded_constructors[called_constructor_path][called_constructor_signature]['constructor_parameters']:
                        old_constructor_args.insert(i, 'null')
                        overloaded_constructors[called_constructor_path][called_constructor_signature]['constructor_parameters'].insert(i, new_parameters[i])
                
                new_constructor_args = ['null' for x in range(len(new_parameters))]
                for i in range(len(new_parameters)):
                    if new_parameters[i] in overloaded_constructors[called_constructor_path][called_constructor_signature]['constructor_parameters']:
                        new_constructor_args[i] = old_constructor_args[index_map[overloaded_constructors[called_constructor_path][called_constructor_signature]['constructor_parameters'][i]]]
                    if 'boolean' in new_parameters[i] and new_constructor_args[i] == 'null':
                        new_constructor_args[i] = 'false'
                
                overloaded_constructors[called_constructor_path][called_constructor_signature]['constructor_parameters'] = target_constructor_old_params

                call_site_body_raw = ''
                if len(constructor_call_site_lines) == 1:
                    call_site_body_raw = ''.join(constructor_call_site_lines)[start_col-1:end_col]
                else:
                    constructor_call_site_lines[0] = constructor_call_site_lines[0][start_col-1:]
                    constructor_call_site_lines[-1] = constructor_call_site_lines[-1][:end_col]
                    call_site_body_raw = ''.join(constructor_call_site_lines)
                
                new_call_site_body = f'{called_constructor_signature.split("(")[0]}.{called_constructor_signature.split("(")[0]}{str(called_constructor["constructor_id"])}({str(called_constructor["constructor_id"])}, {", ".join(new_constructor_args[1:])})'

                with open(temp_project_path + '/' + path, 'r') as f:
                    file_lines = f.readlines()
                
                file_lines[start_line-1:end_line] = ''.join(file_lines[start_line-1:end_line]).replace(call_site_body_raw, new_call_site_body)

                with open(temp_project_path + '/' + path, 'w') as f:
                    f.writelines(file_lines)

            if overloaded_constructors[called_constructor_path][called_constructor_signature]['rewrite_details']['overloaded_constructor_type'] == 'single statement dependent' \
                and overloaded_constructors[called_constructor_path][called_constructor_signature]['rewrite_details']['action'] == 'static method':

                call_site_body_raw = ''
                if len(constructor_call_site_lines) == 1:
                    call_site_body_raw = ''.join(constructor_call_site_lines)[start_col-1:end_col]
                else:
                    constructor_call_site_lines[0] = constructor_call_site_lines[0][start_col-1:]
                    constructor_call_site_lines[-1] = constructor_call_site_lines[-1][:end_col]
                    call_site_body_raw = ''.join(constructor_call_site_lines)
                
                new_call_site_body = f'{called_constructor_signature.split("(")[0]}.{called_constructor_signature.split("(")[0]}{str(called_constructor["constructor_id"])}({", ".join(constructor_call_arugments)})'

                if call_site_body_raw.strip().endswith(';'):
                    call_site_body_raw = call_site_body_raw.strip()[:-1]

                with open(temp_project_path + '/' + path, 'r') as f:
                    file_lines = f.readlines()

                file_lines[start_line-1:end_line] = ''.join(file_lines[start_line-1:end_line]).replace(call_site_body_raw, new_call_site_body)
                
                with open(temp_project_path + '/' + path, 'w') as f:
                    f.writelines(file_lines)

            if overloaded_constructors[called_constructor_path][called_constructor_signature]['rewrite_details']['overloaded_constructor_type'] == 'independent':

                new_parameters = new_constructors[called_constructor_path]['new_constructor']['new_constructor_signature']
                old_constructor_args = constructor_call_arugments.copy()

                target_constructor_old_params = overloaded_constructors[called_constructor_path][called_constructor_signature]['constructor_parameters'].copy()
                for i in range(len(new_parameters)):
                    if new_parameters[i] not in overloaded_constructors[called_constructor_path][called_constructor_signature]['constructor_parameters']:
                        old_constructor_args.insert(i, 'null')
                        overloaded_constructors[called_constructor_path][called_constructor_signature]['constructor_parameters'].insert(i, new_parameters[i])

                index_map = {element: index for index, element in enumerate(overloaded_constructors[called_constructor_path][called_constructor_signature]['constructor_parameters'])}

                new_constructor_args = ['null' for x in range(len(new_parameters))]
                for i in range(len(new_parameters)):
                    if new_parameters[i] in overloaded_constructors[called_constructor_path][called_constructor_signature]['constructor_parameters']:
                        new_constructor_args[i] = old_constructor_args[index_map[new_parameters[i]]]
                    if 'boolean' in new_parameters[i] and new_constructor_args[i] == 'null':
                        new_constructor_args[i] = 'false'
                
                overloaded_constructors[called_constructor_path][called_constructor_signature]['constructor_parameters'] = target_constructor_old_params

                call_site_body_raw = ''
                if len(constructor_call_site_lines) == 1:
                    call_site_body_raw = ''.join(constructor_call_site_lines)[start_col-1:end_col]
                else:
                    constructor_call_site_lines[0] = constructor_call_site_lines[0][start_col-1:]
                    constructor_call_site_lines[-1] = constructor_call_site_lines[-1][:end_col]
                    call_site_body_raw = ''.join(constructor_call_site_lines)

                new_call_site_body = 'new ' + called_constructor_signature.split('(')[0] + '(' + str(called_constructor['constructor_id']) + ', ' + ', '.join(new_constructor_args[1:]) + ')'

                total_line_breaks_old = call_site_body_raw.count('\n')
                total_line_breaks_new = new_call_site_body.count('\n')

                if total_line_breaks_old > total_line_breaks_new:
                    for i in range(total_line_breaks_old - total_line_breaks_new):
                        new_call_site_body += '\n'
                elif total_line_breaks_old < total_line_breaks_new:
                    for i in range(total_line_breaks_new - total_line_breaks_old):
                        new_call_site_body.replace('\n', '', 1)

                with open(temp_project_path + '/' + path, 'r') as f:
                    file_lines = f.readlines()
                
                file_lines[start_line-1:end_line] = ''.join(file_lines[start_line-1:end_line]).replace(call_site_body_raw, new_call_site_body)

                with open(temp_project_path + '/' + path, 'w') as f:
                    f.writelines(file_lines)


def replace_overloaded_constructors(overloaded_constructors, new_constructors):

    for path in new_constructors:

        file_lines = []
        with open(temp_project_path + '/' + path, 'r') as f:
            file_lines = f.readlines()
        new_constructor_start_line = 0
        for overloaded_constructor in overloaded_constructors[path]:

            if overloaded_constructor == 'new_constructor':
                continue
            
            new_constructor_start_line = overloaded_constructors[path][overloaded_constructor]['constructor_start_line']
            for i in range(overloaded_constructors[path][overloaded_constructor]['constructor_start_line']-1, overloaded_constructors[path][overloaded_constructor]['constructor_end_line']):
                file_lines[i] = '// ' + file_lines[i]
        
        file_lines[new_constructor_start_line-1:new_constructor_start_line-1] = new_constructors[path]['new_constructor']['new_constructor_body']

        with open(temp_project_path + '/' + path, 'w') as f:
            f.writelines(file_lines)


def main():
    overloaded_constructors = get_overloaded_constructors()
    # for path in overloaded_constructors:
    #     for constructor in overloaded_constructors[path]:
    #         print(path, constructor)
    #     print('-'*50)
    call_sites = get_constructor_call_sites()
    overloaded_constructors, new_constructors = rewrite_overloaded_constructors(overloaded_constructors)
    rewrite_call_sites(overloaded_constructors, call_sites, new_constructors)
    replace_overloaded_constructors(overloaded_constructors, new_constructors)

main()
