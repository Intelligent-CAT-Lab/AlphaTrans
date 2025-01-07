#!/bin/bash

projects=(
    "commons-cli"
    "commons-codec"
    "commons-csv"
    "commons-exec"
    "JavaFastPFOR"
    "commons-fileupload"
    "commons-graph"
    "jansi"
    "commons-pool"
    "commons-validator"
)

projects_dir=java_projects/cleaned_final_projects_decomposed_tests;
main=$(pwd);

for project in "${projects[@]}"; do
    echo "building $project"
    cd "$projects_dir/$project" || exit
    mvn clean test -Drat.skip
    cd "$main" || exit
done
