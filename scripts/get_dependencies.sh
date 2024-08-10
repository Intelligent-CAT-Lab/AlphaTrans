#!/bin/bash

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'joda-money' 'joda-convert';
do
    echo "extracting dependencies for $project"
    python3 utils.py --project_name=$project --function=parse_dependencies --suffix=_decomposed_tests
done
