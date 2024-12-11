
PROJECT_NAME=$1
DATABASE_NAME=$2
OUTPUT_PATH=$3

python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_imports --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_fields --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_class_callables --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_interfaces --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_superclasses --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_nested_classes --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_parameters --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_call_graph --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_types --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_constructor_call_graph --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_all_constructors --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_method_call_graph --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_all_methods --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_overridden_methods --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
python3 execute_queries.py --project_name=$PROJECT_NAME --query_name=get_static_initializers --database_name=$DATABASE_NAME --output_path=$OUTPUT_PATH
