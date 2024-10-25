
project=$1
temperature=$2

export PYTHONPATH=$PYTHONPATH:`pwd`
python3 src/translation/compositional_translation_validation.py \
    --model_name=deepseek-coder-33b-instruct \
    --project_name=$project \
    --from_lang=Java \
    --to_lang=Python \
    --include_call_graph \
    --debug \
    --suffix=_decomposed_tests \
    --temperature=$temperature \
    --validate_by_graal \
    --recursion_depth=2 \
    --include_implementation | tee ${project}_${model}_body.log
