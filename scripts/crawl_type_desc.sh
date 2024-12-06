#!/bin/bash

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'joda-money' 'joda-convert';
do
    echo "creating schema for $project"
    python3 src/type_resolution/crawl_type_desc.py --project_name=$project
done
