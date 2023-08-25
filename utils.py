import os
import argparse
import re
import json
import graphviz


def parse_dependencies():
    """
    you should have compiled and executed the following before running this function:
    jdeps -verbose -dotoutput dependencies java_projects/<project_name>/target/classes/<path-to-class-files>/*.class
    rm -rf dependencies/summary.dot
    """
    dependencies_dir = os.path.join(os.path.dirname(__file__), 'dependencies')
    class_deps = os.listdir(dependencies_dir)
    class_dependencies = {}
    for class_dep in class_deps:

        if class_dep.startswith('package-info'):
            continue

        if not class_dep.endswith('.dot'):
            continue

        if '$' in class_dep:
            continue

        current_class = class_dep.split('.')[0]
        class_dependencies.setdefault(current_class, [])

        with open(os.path.join(dependencies_dir, class_dep), 'r') as f:
            lines = f.readlines()
            for line in lines[2:-1]:

                if 'java.base' in line:
                    continue

                candidate_line = line.strip()
                class_name = re.search(r'\((.*?)\)', candidate_line).group(1).split('.')[0]

                if '$' in class_name:
                    class_name = class_name.split('$')[0]
                
                if class_name == current_class:
                    continue

                class_dependencies[current_class].append(class_name)

    with open(os.path.join(dependencies_dir, 'dependencies.json'), 'w') as f:
        json.dump(class_dependencies, f, indent=4)

    # uncomment below to plot dependency graph
    g = graphviz.Digraph('G', filename=os.path.join(dependencies_dir, 'dependencies.gv'), format='png')
    for class_name, dependencies in class_dependencies.items():
        for dependency in dependencies:
            g.edge(class_name, dependency)
    g.view()

    # remove cycles
    removed_cycles = []
    for k,v in class_dependencies.items():
        for dependency in v:
            if k in class_dependencies[dependency]:
                class_dependencies[dependency].remove(k)
                removed_cycles.append((dependency, k))

    # create traversal based on dependencies (pure to impure)
    traversal = {}
    while len(class_dependencies) != len(traversal):
        for k,v in class_dependencies.items():
            if k not in traversal:
                if len(v) == 0:
                    traversal[k] = []
                else:
                    if all([x in traversal for x in v]):
                        traversal[k] = v

    # add back cycles after creating traversal
    for i,j in removed_cycles:
        traversal[i].append(j)

    with open(os.path.join(dependencies_dir, 'traversal.json'), 'w') as f:
        json.dump(traversal, f, indent=4)


def main(args):
    function_name = args.function
    if function_name == 'parse_dependencies':
        parse_dependencies()
    else:
        raise NotImplementedError(f'function {function_name} not implemented')


def parse_args():
    parser = argparse.ArgumentParser("utilities")
    parser.add_argument('--function', type=str, default='parse_dependencies', help='function name in utility', required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(args)    
