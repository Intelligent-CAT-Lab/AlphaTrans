import json
import argparse
import tqdm

def main(args):

    project = args.project_name
    projects_dir = f'java_projects/cleaned_final_projects{args.suffix}/'
    query_outputs_dir = f'data/query_outputs{args.suffix}'

    method_call_graph = []
    with open(f'{query_outputs_dir}/{project}/{project}_call_graph.txt') as f:
        method_call_graph = f.readlines()
    
    for line in tqdm.tqdm(method_call_graph):
        splitted_line = [x.strip() for x in line.split('|') if x.strip() != '']

        if len(splitted_line) != 7:
            continue

        call_location, caller_name, caller_location, caller_signature, callee_name, callee_location, callee_signature = splitted_line

        if args.suffix == '_evosuite' and 'ESTest' not in call_location:
            continue

        if call_location == caller_location:
            continue

        if caller_name in ['<obinit>', '<clinit>'] or callee_name in ['<obinit>', '<clinit>']:
            continue

        is_library_callee = False
        if callee_location.endswith(':0:0:0:0'):
            is_library_callee = True

            if 'evosuite-standalone-runtime-1.2.0.jar' in callee_location:
                callee_location = callee_location[callee_location.find('evosuite-standalone-runtime-1.2.0.jar')+len('evosuite-standalone-runtime-1.2.0.jar'):]
            if 'target/classes' in callee_location:
                callee_location = callee_location[callee_location.find('target/classes/')+len('target/classes/'):]
            if 'target/test-classes' in callee_location:
                callee_location = callee_location[callee_location.find('target/test-classes/')+len('target/test-classes/'):]
            
            map_ = {'Assert.class:0:0:0:0': 'Assert', 'EvoAssertions.class:0:0:0:0': 'EvoAssertions', 'Log.class:0:0:0:0': 'Log', 'LogFactory.class:0:0:0:0': 'LogFactory', 'TestCase.class:0:0:0:0': 'TestCase', 'Assumptions.class:0:0:0:0': 'Assumptions', 'Assertions.class:0:0:0:0': 'Assertions', 'Assumptions.class:0:0:0:0': 'Assumptions', 'Assume.class:0:0:0:0': 'Assume', 'IOUtils.class:0:0:0:0': 'IOUtils', 'Arguments.class:0:0:0:0': 'Arguments'}

            for k in map_:
                if callee_location.endswith(k):
                    callee_location = map_[k]
                    break
            
            callee_location = callee_location.replace('.class:0:0:0:0', '').replace('.sig:0:0:0:0', '')
            if 'file:///' in callee_location:
                callee_location = '/'.join(callee_location[callee_location.find('file:///') + len('file:///'):].split('/')[1:])
                        
            assert 'file:///' not in callee_location, f'callee_location: {callee_location}'
            assert '.class:0:0:0:0' not in callee_location, f'callee_location: {callee_location}'

        callee_path = callee_location[callee_location.find(':')+1:callee_location.find(':', callee_location.find(':')+1)]
        callee_path = callee_path[callee_path.find(project):]

        caller_path = caller_location[caller_location.find(':')+1:caller_location.find(':', caller_location.find(':')+1)]
        caller_path = caller_path[caller_path.find(project):]

        caller_start_line = int(caller_location[caller_location.find(':', caller_location.find(':')+1)+1:].split(':')[0]) - 1
        caller_end_line = caller_start_line + 5

        callable_body = ''
        with open(f'{projects_dir}/{caller_path}', 'r') as f:
            callable_body = f.readlines()[caller_start_line-1:caller_end_line]
        
        # print(call_location, caller_name, callee_name, callable_body, caller_start_line, caller_end_line, flush=True)
        # print(caller_location)
        # print(callee_location)
        # print('-------------------' * 10, flush=True)

        start_terminations = ['*/', '@', '}']
        end_terminations = [';', '}', '*/', '{']
        searched = False
        while not (any([callable_body[0].strip().startswith(x) for x in start_terminations]) 
                or any([callable_body[0].strip().endswith(x) for x in end_terminations])):

            searched = True
            
            callable_body = ''
            with open(f'{projects_dir}/{caller_path}', 'r') as f:
                callable_body = f.readlines()[caller_start_line-1:caller_end_line]
            caller_start_line -= 1
        
        if searched:
            caller_start_line += 2

            callable_body = ''
            with open(f'{projects_dir}/{caller_path}', 'r') as f:
                callable_body = f.readlines()[caller_start_line-1:caller_end_line]
            
            for i in range(len(callable_body)):
                if callable_body[i].strip() == '':
                    caller_start_line += 1
                if callable_body[i].strip() != '':
                    break
        else:
            caller_start_line += 1

        if not is_library_callee:

            callee_start_line = int(callee_location[callee_location.find(':', callee_location.find(':')+1)+1:].split(':')[0]) - 1
            callee_end_line = callee_start_line + 5

            callable_body = ''
            with open(f'{projects_dir}/{callee_path}', 'r') as f:
                callable_body = f.readlines()[callee_start_line-1:callee_end_line]

            searched = False
            while not (any([callable_body[0].strip().startswith(x) for x in start_terminations]) 
                    or any([callable_body[0].strip().endswith(x) for x in end_terminations])):

                searched = True
                
                callable_body = ''
                with open(f'{projects_dir}/{callee_path}', 'r') as f:
                    callable_body = f.readlines()[callee_start_line-1:callee_end_line]
                callee_start_line -= 1
            
            if searched:
                callee_start_line += 2

                callable_body = ''
                with open(f'{projects_dir}/{callee_path}', 'r') as f:
                    callable_body = f.readlines()[callee_start_line-1:callee_end_line]
                
                for i in range(len(callable_body)):
                    if callable_body[i].strip() == '':
                        callee_start_line += 1
                    if callable_body[i].strip() != '':
                        break
            else:
                callee_start_line += 1

            callee_schema_name = callee_path[callee_path.find(project):].replace('/', '.').replace('.java', '')

            if callee_name == 'getCompBuffer' and 'JavaFastPFOR' in callee_schema_name:
                callee_start_line = 84
            if callee_name == 'RoaringIntPacking' and 'JavaFastPFOR' in callee_schema_name:
                continue

            callee_method_class_name, callee_method_key_name = None, None
            callee_schema = {}
            is_available = False
            with open(f'data/schemas{args.suffix}/{project}/{callee_schema_name}.json') as f:
                callee_schema = json.load(f)
                for class_ in callee_schema['classes']:

                    if callee_name == class_ and callee_start_line == callee_schema['classes'][class_]['start']:
                        callee_method_class_name = class_
                        callee_method_key_name = class_
                        is_available = True
                        break

                    for method in callee_schema['classes'][class_]['methods']:
                        if callee_name == method.split(':')[1] and callee_start_line == callee_schema['classes'][class_]['methods'][method]['start']:                        
                            callee_method_class_name = class_
                            callee_method_key_name = method
                            is_available = True
                            break

            assert is_available, f'callee is not available: {callee_name} in {callee_schema_name}'
        
        else:
            callee_schema_name = 'library'
            callee_method_class_name = callee_location
            callee_method_key_name = callee_signature

        caller_schema_name = caller_path[caller_path.find(project):].replace('/', '.').replace('.java', '')
        caller_schema = {}
        is_available = False
        with open(f'data/schemas{args.suffix}/{project}/{caller_schema_name}.json') as f:
            caller_schema = json.load(f)
            for class_ in caller_schema['classes']:

                for method in caller_schema['classes'][class_]['methods']:
                    if caller_name == method.split(':')[1] and caller_start_line == caller_schema['classes'][class_]['methods'][method]['start']:
                        if [callee_schema_name, callee_method_class_name, callee_method_key_name] not in caller_schema['classes'][class_]['methods'][method]['calls']:
                            caller_schema['classes'][class_]['methods'][method]['calls'].append((callee_schema_name, callee_method_class_name, callee_method_key_name))
                        is_available = True
                        break

        assert is_available, f'caller is not available: {caller_name} in {caller_schema_name}'

        with open(f'data/schemas{args.suffix}/{project}/{caller_schema_name}.json', 'w') as f:
            json.dump(caller_schema, f, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='extract call graph of preprocessed project')
    parser.add_argument('--project_name', type=str, help='Name of the project')
    parser.add_argument('--suffix', type=str, help='suffix')
    args = parser.parse_args()
    main(args)
