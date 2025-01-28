#!/bin/bash

model_name=$1

export PYTHONPATH=$PYTHONPATH:`pwd`

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR';
do
    echo "translating class-by-class for $project"
    python3 src/translation/prompt_class_by_class.py --project_name=$project --model_name=$model_name
done
