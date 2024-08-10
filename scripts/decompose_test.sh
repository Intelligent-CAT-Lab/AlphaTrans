#!/bin/bash

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR';
do
    echo "Decomposing tests for $project";
    mkdir -p java_projects/cleaned_final_projects_decomposed_tests/$project;
    cp -r java_projects/cleaned_final_projects/$project java_projects/cleaned_final_projects_decomposed_tests/;
    python3 src/static_analysis/decompose_dev_test.py --project_name=$project;
done
