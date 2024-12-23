#!/bin/bash

# To execute, run `bash scripts/test_glue.sh <project>` from the root directory

projects=('commons-cli' 'commons-codec' 'commons-csv' 'commons-validator' 'commons-fileupload' 'commons-pool' 'commons-graph' 'commons-exec' 'jansi' 'JavaFastPFOR')

if [[ " ${projects[@]} " =~ " $1 " ]]; then
    echo "Running tests for $1"
else
    echo "Invalid project name! Please provide a valid project name from the following:
    ${projects[@]}"
    echo "Usage: bash scripts/test_glue.sh <project>"
    exit 1
fi

# Directory where your Maven project is located using positional parameter
PROJECT_DIR="java_projects/glue_code/$1"

# Directory to store results (create if it doesn't exist)
OUTPUT_DIR="$PROJECT_DIR/results"
mkdir -p $OUTPUT_DIR

# clean output directory
rm -rf $OUTPUT_DIR/*

# Run Maven test
mvn -f $PROJECT_DIR clean test -Drat.skip

# Copy the test results only in .txt files to the output directory
cp -r $PROJECT_DIR/target/surefire-reports/*.txt "$OUTPUT_DIR"
