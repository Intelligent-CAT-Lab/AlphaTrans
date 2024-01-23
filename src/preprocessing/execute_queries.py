import os
import argparse

def main(args):

    os.makedirs(f"../../data/query_outputs/{args.project_name}", exist_ok=True)

    if args.query_name == 'get_imports':
        os.system(f"codeql query run -d ../../databases/{args.database_name} -- get_imports.ql | tail -n +3 >> ../../data/query_outputs/{args.project_name}/{args.project_name}_imports.txt")

    if args.query_name == 'get_method_call_graph':
        os.system(f"codeql query run -d ../../databases/{args.database_name} -- get_method_call_graph_1.ql | tail -n +3 >> ../../data/query_outputs/{args.project_name}/{args.project_name}_method_call_graph.txt")
        os.system(f"codeql query run -d ../../databases/{args.database_name} -- get_method_call_graph_2.ql | tail -n +3 >> ../../data/query_outputs/{args.project_name}/{args.project_name}_method_call_graph.txt")

    if args.query_name == 'get_constructor_call_graph':
        os.system(f"codeql query run -d ../../databases/{args.database_name} -- get_constructor_call_graph_1.ql | tail -n +3 >> ../../data/query_outputs/{args.project_name}/{args.project_name}_constructor_call_graph.txt")
        os.system(f"codeql query run -d ../../databases/{args.database_name} -- get_constructor_call_graph_2.ql | tail -n +3 >> ../../data/query_outputs/{args.project_name}/{args.project_name}_constructor_call_graph.txt")

    if args.query_name == 'get_all_methods':
        os.system(f"codeql query run -d ../../databases/{args.database_name} -- get_all_methods_1.ql | tail -n +3 >> ../../data/query_outputs/{args.project_name}/{args.project_name}_all_methods.txt")
        os.system(f"codeql query run -d ../../databases/{args.database_name} -- get_all_methods_2.ql | tail -n +3 >> ../../data/query_outputs/{args.project_name}/{args.project_name}_all_methods.txt")

    if args.query_name == 'get_fields':
        os.system(f"codeql query run -d ../../databases/{args.database_name} -- get_fields.ql | tail -n +3 >> ../../data/query_outputs/{args.project_name}/{args.project_name}_fields.txt")

    if args.query_name == 'get_overridden_methods':
        os.system(f"codeql query run -d ../../databases/{args.database_name} -- get_overridden_methods.ql | tail -n +3 >> ../../data/query_outputs/{args.project_name}/{args.project_name}_overridden_methods.txt")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='execute codeql queries')
    parser.add_argument('--project_name', type=str, help='Project name to simplify', required=True)
    parser.add_argument('--query_name', type=str, help='Query name to execute', required=True)
    parser.add_argument('--database_name', type=str, help='Database name to execute', required=True)
    args = parser.parse_args()
    main(args)
