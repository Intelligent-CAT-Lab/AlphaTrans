#!/bin/bash

projects=('commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR')

# if no project name is provided, generate glue for all projects
if [ -z "$1" ]; then
    for project in "${projects[@]}";
    do
        echo "generating glue for $project"
        python3 src/glue_code/script.py --project_name="$project"
    done
else
    if [[ " ${projects[@]} " =~ " $1 " ]]; then
        echo "generating glue for $1"
        python3 src/glue_code/script.py --project_name="$1"
    else
        echo "Invalid project name! Please provide a valid project name from the following list:
        ${projects[@]}"
    fi
fi
