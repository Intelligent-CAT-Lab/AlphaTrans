#!/bin/bash

repos=(
        "https://github.com/apache/commons-cli.git commons-cli commons-cli-1.5.0"
        "https://github.com/apache/commons-codec.git commons-codec commons-codec-1.16-rc1"
        "https://github.com/apache/commons-csv.git commons-csv rel/commons-csv-1.10.0"
        "https://github.com/apache/commons-exec.git commons-exec rel/commons-exec-1.4.0"
        "https://github.com/lemire/JavaFastPFOR.git JavaFastPFOR 0ecdda9"
        "https://github.com/apache/commons-fileupload.git commons-fileupload commons-fileupload-1.5"
        "https://github.com/apache/commons-graph.git commons-graph 93d2ba7"
        "https://github.com/fusesource/jansi.git jansi 045fd56"
        "https://github.com/apache/commons-pool.git commons-pool rel/commons-pool-2.11.1"
        "https://github.com/apache/commons-validator.git commons-validator VALIDATOR_1_7"
)

mkdir -p java_projects/original_projects;
main=$(pwd);

for repo in "${repos[@]}"; do
    IFS=' ' read -r url project commit <<< "$repo"
    git clone "$url" "java_projects/original_projects/$project"
    cd "java_projects/original_projects/$project" || exit
    git reset --hard "$commit"        
    cd "$main" || exit
done
