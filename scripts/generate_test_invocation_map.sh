#!/bin/bash

suffix=$1

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR';
do
    echo "extracting test map for $project"
    python3 src/static_analysis/create_test_method_map.py --project_name=$project --suffix=$suffix
done
