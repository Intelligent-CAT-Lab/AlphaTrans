#!/bin/bash

SUFFIX=$1
mkdir -p databases;
main=$(pwd);
projects_dir=java_projects/cleaned_final_projects${SUFFIX};

for project in 'commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR';
do
    echo "creating database $project"
    cd "$projects_dir/$project" || exit
    codeql database create ../../../databases/${project}${SUFFIX} --language=java --overwrite;
    cd "$main" || exit
done
