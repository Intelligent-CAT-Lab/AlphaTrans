#!/bin/bash

project=$1
suffix=$2
temperature=$3
model=$4

echo "results for $project [temperature=$temperature, model=$model]"
python3 src/postprocessing/print_results.py --project_name=$project --suffix=$suffix --temperature=$temperature --model=$model
