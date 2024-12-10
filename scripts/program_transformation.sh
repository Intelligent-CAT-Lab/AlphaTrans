#!/bin/bash

$PROJECT_DIR=$1
$PROJECT_NAME=$2

python3 src/preprocessing/refactor_methods.py $PROJECT_DIR $PROJECT_NAME
python3 src/preprocessing/refactor_constructors.py $PROJECT_DIR $PROJECT_NAME
