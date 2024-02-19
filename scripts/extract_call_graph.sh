#!/bin/bash

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'joda-money' 'joda-convert';
do
    echo "extracting call graph for $project"
    python3 src/static_analysis/extract_call_graph.py --project_name=$project
done
