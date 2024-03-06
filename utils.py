import os
import argparse
import re
import json
import graphviz


def parse_dependencies(project_name):
    os.makedirs(f'data/dependencies/{project_name}', exist_ok=True)

    class_dependencies = {}
    java_files = []
    for root, dirs, files in os.walk(f'java_projects/cleaned_final_projects/{project_name}/src'):
        for file in files:
            if file.endswith('.java'):
                java_files.append(os.path.join(root, file))
    
    for dot_class_file in java_files:
        class_name = dot_class_file.split('/')[-1].split('.')[0]
        class_dependencies.setdefault(class_name, [])
    
    os.system(f'jdeps -verbose -dotoutput data/dependencies/{project_name} java_projects/cleaned_final_projects/{project_name}/target/classes')
    os.system(f'jdeps -verbose -dotoutput data/dependencies/{project_name} java_projects/cleaned_final_projects/{project_name}/target/test-classes')
    os.remove(f'data/dependencies/{project_name}/summary.dot')

    dependencies_dir = os.path.join(os.path.dirname(__file__), f'data/dependencies/{project_name}')
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

    # g = graphviz.Digraph('G', filename=os.path.join(dependencies_dir, 'dependencies.gv'))
    # for class_name, dependencies in class_dependencies.items():
    #     for dependency in dependencies:
    #         g.edge(class_name, dependency)
    # g.render(os.path.join(dependencies_dir, 'dependency_graph'), format='png', cleanup=True)

    # # remove cycles
    # removed_cycles = []
    # for k,v in class_dependencies.items():
    #     for dependency in v:
    #         if k in class_dependencies[dependency]:
    #             class_dependencies[dependency].remove(k)
    #             removed_cycles.append((dependency, k))

    # # create traversal based on dependencies (pure to impure)
    # traversal = {}
    # while len(class_dependencies) != len(traversal):
    #     for k,v in class_dependencies.items():
    #         if k not in traversal:
    #             if len(v) == 0:
    #                 traversal[k] = []
    #             else:
    #                 if all([x in traversal for x in v]):
    #                     traversal[k] = v

    # # add back cycles after creating traversal
    # for i,j in removed_cycles:
    #     traversal[i].append(j)

    # with open(os.path.join(dependencies_dir, 'traversal.json'), 'w') as f:
    #     json.dump(traversal, f, indent=4)


def main(args):
    function_name = args.function
    if function_name == 'parse_dependencies':
        parse_dependencies(args.project_name)
    else:
        raise NotImplementedError(f'function {function_name} not implemented')


def parse_args():
    parser = argparse.ArgumentParser("utilities")
    parser.add_argument('--project_name', type=str, default='java_projects', help='project name', required=True)
    parser.add_argument('--function', type=str, default='parse_dependencies', help='function name in utility', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(args)    
