#!/bin/bash

project=$1
temperature=$2
model=$3
results_dir=$4

echo "results for $project [temperature=$temperature, model=$model]"
python3 src/postprocessing/print_results.py --project_name=$project --results_dir=$results_dir --temperature=$temperature --model=$model
