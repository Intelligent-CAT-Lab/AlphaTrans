#!/bin/bash

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-fileupload' 'commons-graph' 'commons-pool' 'commons-validator' 'joda-convert' 'joda-money';
do
    echo "extracting types for $project"
    python3 src/static_analysis/extract_types.py --project_name=$project
done
