#!/bin/bash

PROJECT_DIR=$1
PROJECT_NAME=$2
SUFFIX="_decomposed_tests"

python3 src/preprocessing/refactor_methods.py $PROJECT_DIR $PROJECT_NAME $SUFFIX
python3 src/preprocessing/refactor_constructors.py $PROJECT_DIR $PROJECT_NAME $SUFFIX
