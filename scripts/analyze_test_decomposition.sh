#!/bin/bash

model_name=$1
translation_dir=$2

export PYTHONPATH=$PYTHONPATH:`pwd`

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR';
do
    echo "analyzing test decomposition for $project"
    python3 src/postprocessing/analyze_test_decomposition.py --project_name=$project --model_name=$model_name --translation_dir=$translation_dir
done
