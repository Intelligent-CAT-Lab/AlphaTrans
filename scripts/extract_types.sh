#!/bin/bash

suffix=$1

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR';
do
    echo "extracting types for $project"
    python3 src/type_resolution/extract_types.py --project_name=$project --suffix=$suffix
done
