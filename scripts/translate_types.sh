#!/bin/bash

type=$1

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR';
do
    echo "translating types for $project"
    python3 src/type_resolution/translate_type.py --project_name=$project --model_name=deepseek-coder-33b-instruct --from_lang=Java --to_lang=Python --to_lang_version=3.11 --type=$type
done
