#!/bin/bash

suffix=$1

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR';
do
    echo "extracting source api for $project"
    python3 src/static_analysis/extract_source_tests.py --project_name=$project --suffix=$suffix

done
