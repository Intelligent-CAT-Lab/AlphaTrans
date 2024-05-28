
for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'joda-money' 'joda-convert';
do
    python3 src/translation/compositional_translation_validation.py \
        --model_name=deepseek-coder-33b-instruct \
        --project_name=$project \
        --from_lang=Java \
        --to_lang=Python \
        --include_call_graph \
        --cache_dir=/home/shared/huggingface \
        --translate_main | tee ${project}_main.log
done
