#!/bin/bash

suffix=$1

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR';
do
    echo "creating schema for $project"
    python3 src/static_analysis/create_schema.py --project_name=$project --suffix=$suffix
done
