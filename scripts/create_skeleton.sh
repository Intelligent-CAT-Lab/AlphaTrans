#!/bin/bash


pwd=$(pwd)

for model in 'deepseek-coder-33b-instruct';
do
    for type in 'body';
    do
        for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR';
        do
            echo "creating skeleton for $project"
            export PYTHONPATH=$pwd/data/skeletons/$project
            python3 src/static_analysis/create_skeleton.py --project_name=$project --model_name=$model --type=$type --suffix=_decomposed_tests
        done
    done
done
