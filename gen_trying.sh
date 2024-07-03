# create database
(cd java_projects/cleaned_final_projects/$1/ &&
codeql database create ../../../databases/$1 --language=java --overwrite)

# cleat the query_outputs from before
rm -rf data/query_outputs/$1

# run queries
(cd vscode-codeql-starter/codeql-custom-queries-java && bash simplify_script.sh $1 $1)

# create schemas and skeletons
python src/static_analysis/extract_call_graph.py --project_name=$1
python src/static_analysis/create_schema.py --project_name=$1
python utils.py --project_name=$1 --function parse_dependencies
python src/static_analysis/create_skeleton.py --project_name=$1
