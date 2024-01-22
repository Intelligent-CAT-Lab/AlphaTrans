import os
import json
import argparse


def main(args):

    import_lines = []
    with open(f'data/query_outputs/{args.project_name}/{args.project_name}_imports.txt', 'r') as f:
        import_lines = f.readlines()

    import_bodies = {}
    for l in import_lines:
        import_name, import_path = [x.strip() for x in l.split('|')[1:-1]]

        path = import_path[import_path.find(':')+1:import_path.find(':', import_path.find(':')+1)]
        path = path[path.find(f'/{args.project_name}/')+1:]

        start_line = int(import_path[import_path.find(':', import_path.find(':')+1)+1:].split(':')[0])
        end_line = int(import_path[import_path.find(':', import_path.find(':')+1)+1:].split(':')[2])

        with open(f'java_projects/{path}', 'r') as f:
            lines = f.readlines()
        
        if start_line != end_line:
            raise Exception('start_line != end_line')
        
        import_bodies.setdefault(path, [])
        import_body = ''.join(lines[start_line-1:end_line]).strip().replace(';', '')
        assert import_body != '', f'import_body is empty: {path} {start_line} {end_line}'
        import_bodies[path].append(import_body)

    os.makedirs(f'data/third_party_libs/{args.project_name}', exist_ok=True)

    if not os.path.exists(f'data/third_party_libs/{args.project_name}/{args.project_name}_trusted.txt'):
        with open(f'data/third_party_libs/{args.project_name}/{args.project_name}_trusted.txt', 'w') as f:
            f.write('')

    trusted_patterns = []
    with open(f'data/third_party_libs/{args.project_name}/{args.project_name}_trusted.txt') as f:
        trusted_patterns = [x.strip() for x in f.readlines()]

    unresolved_imports = []
    for path, bodies in import_bodies.items():
        for body in bodies:

            if (body, path) in unresolved_imports:
                continue

            is_true = False
            for pattern in trusted_patterns:
                if body == pattern:
                    is_true = True
                    break
            
            if is_true:
                continue
            
            unresolved_imports.append((body, path))

    import_out = open(f'data/third_party_libs/{args.project_name}/{args.project_name}_untrusted.jsonl', 'wt')
    unresolved_imports = sorted(unresolved_imports, key=lambda x: x[0])
    for item, item_path in unresolved_imports:
        import_out.writelines(json.dumps({'body': item, 'path': item_path}) + '\n')

    unique_import_out = open(f'data/third_party_libs/{args.project_name}/{args.project_name}_unique_import_bodies.txt', 'w')
    unique_imports = sorted(set([x[0] for x in unresolved_imports]))
    for item in unique_imports:
        unique_import_out.write(f'{item}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simplify projects from third-party libraries')
    parser.add_argument('--project_name', type=str, help='Project name to simplify')
    args = parser.parse_args()
    main(args)
