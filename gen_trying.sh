# create database
cd java_projects/cleaned_final_projects/trying_stuff_out/
codeql database create ../../../databases/trying_stuff_out --language=java --overwrite
cd ../../../

# run queries
cd vscode-codeql-starter/codeql-custom-queries-java && ./run.sh
cd ../../

# create schemas and skeletons
python src/static_analysis/extract_call_graph.py --project_name=trying_stuff_out
python src/static_analysis/create_schema.py --project_name=trying_stuff_out
python utils.py --project_name=trying_stuff_out --function parse_dependencies
python src/static_analysis/create_skeleton.py --project_name=trying_stuff_out
