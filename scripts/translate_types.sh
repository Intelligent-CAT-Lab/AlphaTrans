#!/bin/bash

TYPE=$1

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'joda-money' 'joda-convert';
do
    echo "extracting types for $project"
    python3 src/type_resolution/translate_type.py --project_name=$project --model_name=deepseek-coder-33b-instruct --from_lang=Java --to_lang=Python --to_lang_version=3.11 --type=$TYPE
done
