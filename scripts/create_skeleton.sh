#!/bin/bash

suffix=$1

pwd=$(pwd)
for model in 'deepseek-coder-33b-instruct' 'gpt-4o-2024-11-20';
do
    for type in 'body';
    do
        for temperature in 0.0;
        do
            for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR';
            do
                echo "creating skeleton for $project"
                export PYTHONPATH=$pwd/data/skeletons/$project
                python3 src/static_analysis/create_skeleton.py --project_name=$project --model_name=$model --type=$type --suffix=$suffix --temperature=$temperature
            done
        done
    done
done
