#!/bin/bash

SUFFIX=$1

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR';
do
    echo "extracting source api for $project"
    python3 src/static_analysis/create_test_method_map.py --project_name=$PROJECT --suffix=$SUFFIX
done
