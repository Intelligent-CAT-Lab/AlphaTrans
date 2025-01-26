#!/bin/bash

type=$1
model_name=$2

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR';
do
    echo "translating types for $project"
    python3 src/type_resolution/translate_type.py --project_name=$project --model_name=$model_name --type=$type
done
