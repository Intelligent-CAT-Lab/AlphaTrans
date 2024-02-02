#!/bin/bash

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-fileupload' 'commons-graph' 'commons-pool' 'commons-validator' 'joda-convert' 'joda-money';
do
    echo "extracting call graph for $project"
    python3 src/static_analysis/extract_call_graph.py --project_name=$project
done
