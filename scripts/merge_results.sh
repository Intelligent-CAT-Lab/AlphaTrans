#!/bin/bash

temperature=$1
first_model=$2
second_model=$3

echo "merging results for temperature=$temperature, first_model=$first_model, second_model=$second_model"
python3 src/postprocessing/merge_results.py  --temperature=$temperature --first_model=$first_model --second_model=$second_model
