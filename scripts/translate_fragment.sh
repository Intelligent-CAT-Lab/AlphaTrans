#!/bin/bash

PROJECT=$1
TEMPERATURE=$2
MODEL=$3

export PYTHONPATH=$PYTHONPATH:`pwd`
python3 src/translation/compositional_translation_validation.py \
    --model_name=$MODEL \
    --project_name=$PROJECT \
    --from_lang=Java \
    --to_lang=Python \
    --include_call_graph \
    --debug \
    --suffix=_decomposed_tests \
    --temperature=$TEMPERATURE \
    --validate_by_graal \
    --recursion_depth=2 \
    --use_ollama \
    --include_implementation | tee ${PROJECT}_${MODEL}_body.log
