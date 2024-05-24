
for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'joda-money' 'joda-convert';
do
    python3 src/translation/translate_fragment.py --model_name=codellama-13b-instruct --project_name=$project --from_lang=Java --to_lang=Python --include_call_graph --num_translations=3 --cache_dir=/home/shared/huggingface --translate_test | tee {$project}_test.log
done
