import os
import argparse
import re
import json
from collections import defaultdict, deque


def detect_and_remove_cycles(graph):
    # Calculate in-degrees of all nodes
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # Initialize a queue with nodes having zero in-degree
    queue = deque([node for node in graph if in_degree[node] == 0])
    
    topological_order = []
    while queue:
        current = queue.popleft()
        topological_order.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check for cycles
    if len(topological_order) != len(graph):
        # There is a cycle; remove one edge from each cycle
        remaining_nodes = set(graph.keys()) - set(topological_order)
        for node in remaining_nodes:
            for neighbor in graph[node]:
                if neighbor in remaining_nodes:
                    # print(f"Removing edge {node} -> {neighbor} to break the cycle")
                    graph[node].remove(neighbor)
                    return detect_and_remove_cycles(graph)
    
    topological_order.reverse()
    return topological_order


def parse_dependencies(project_name, suffix):
    dependencies_dir = f'data/dependencies{suffix}'
    os.makedirs(f'{dependencies_dir}/{project_name}', exist_ok=True)

    project_dir = f'java_projects/cleaned_final_projects{suffix}'

    class_dependencies = {}
    java_files = []
    for root, dirs, files in os.walk(f'{project_dir}/{project_name}/src'):
        for file in files:
            if file.endswith('.java'):
                java_files.append(os.path.join(root, file))
    
    for dot_class_file in java_files:
        class_name = dot_class_file.split('/')[-1].split('.')[0]
        class_dependencies.setdefault(class_name, [])
    
    os.system(f'jdeps -verbose -dotoutput {dependencies_dir}/{project_name} {project_dir}/{project_name}/target/classes')
    os.system(f'jdeps -verbose -dotoutput {dependencies_dir}/{project_name} {project_dir}/{project_name}/target/test-classes')
    os.remove(f'{dependencies_dir}/{project_name}/summary.dot')

    dependencies_dir = os.path.join(os.path.dirname(__file__), f'{dependencies_dir}/{project_name}')
    class_deps = os.listdir(dependencies_dir)
    for class_dep in class_deps:

        if not class_dep.endswith('.dot'):
            continue

        with open(os.path.join(dependencies_dir, class_dep), 'r') as f:
            lines = f.readlines()
            for line in lines[2:-1]:

                candidate_line = line.strip()
                if 'java.base' in candidate_line or 'java' in candidate_line or 'junit' in candidate_line:
                    continue

                class_name_path = re.search(r'->\s(.*?)\s\(', candidate_line).group(1).replace('"', '').strip()
                class_name = class_name_path.split('.')[-1].strip()

                current_class_path = candidate_line[candidate_line.find('\"') + 1:candidate_line.find('\"', candidate_line.find('\"') + 1)]
                current_class = current_class_path.split('.')[-1].strip()

                if '$' in class_name:
                    if class_name.split('$')[-1].isdigit():
                        # class_name = '.'.join(class_name.split('$')[:-1])
                        class_name = class_name.split('$')[0]
                        class_dependencies.setdefault(class_name, [])
                    else:
                        # class_name = class_name.replace('$', '.')
                        class_name = class_name.split('$')[0]
                        class_dependencies.setdefault(class_name, [])
                
                if '$' in current_class:
                    if current_class.split('$')[-1].isdigit():
                        # current_class = '.'.join(current_class.split('$')[:-1])
                        current_class = current_class.split('$')[0]
                        class_dependencies.setdefault(current_class, [])
                    else:
                        # current_class = current_class.replace('$', '.')
                        current_class = current_class.split('$')[0]
                        class_dependencies.setdefault(current_class, [])
                
                if class_name == current_class:
                    continue
                
                if class_name in class_dependencies[current_class]:
                    continue

                if (class_name, class_name_path.split('$')[0]) in class_dependencies[current_class]:
                    continue

                class_dependencies[current_class].append((class_name, class_name_path.split('$')[0]))

    with open(os.path.join(dependencies_dir, 'dependencies.json'), 'w') as f:
        json.dump(class_dependencies, f, indent=4)

    adjacency_list = defaultdict(list)
    for key, value in class_dependencies.items():
        adjacency_list[key] = []
        for pair in value:
            adjacency_list[key].append(pair[0])

    topological_order = detect_and_remove_cycles(adjacency_list)
    traversal = {i: topological_order[i] for i in range(len(topological_order)) if topological_order[i] not in ['package-info', 'module-info'] and topological_order[i] in class_dependencies}

    with open(os.path.join(dependencies_dir, 'traversal.json'), 'w') as f:
        json.dump(traversal, f, indent=4)


def main(args):
    function_name = args.function
    if function_name == 'parse_dependencies':
        parse_dependencies(args.project_name, args.suffix)
    else:
        raise NotImplementedError(f'function {function_name} not implemented')


def parse_args():
    parser = argparse.ArgumentParser("utilities")
    parser.add_argument('--project_name', type=str, default='java_projects', help='project name', required=True)
    parser.add_argument('--function', type=str, default='parse_dependencies', help='function name in utility', required=True)
    parser.add_argument('--suffix', type=str, default='', help='suffix for output files')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(args)    
