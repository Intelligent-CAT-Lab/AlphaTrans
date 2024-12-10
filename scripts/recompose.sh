#!/bin/bash

PROJECT=$1
TEMPERATURE=$2
MODEL=$3

python3 src/postprocessing/recompose.py --project_name=$PROJECT \
                                        --model_name=$MODEL \
                                        --output_dir=data/recomposed_projects \
                                        --type=body \
                                        --temperature=$TEMPERATURE \
                                        --suffix=_decomposed_tests \
