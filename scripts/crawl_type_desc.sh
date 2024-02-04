#!/bin/bash

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-fileupload' 'commons-graph' 'commons-pool' 'commons-validator' 'joda-convert' 'joda-money';
do
    echo "creating schema for $project"
    python3 src/type_resolution/crawl_type_desc.py --project_name=$project
done
