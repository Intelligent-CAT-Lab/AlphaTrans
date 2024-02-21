#!/bin/bash

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'joda-money' 'joda-convert';
do
    echo "extracting types for $project"
    python3 src/type_resolution/extract_types.py --project_name=$project
done
