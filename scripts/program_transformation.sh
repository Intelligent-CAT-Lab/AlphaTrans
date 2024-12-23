#!/bin/bash

PROJECT_DIR_METHODS=$1
PROJECT_DIR_CONSTRUCTORS=$1
PROJECT_NAME=$2

python3 src/preprocessing/refactor_methods.py $PROJECT_DIR_METHODS $PROJECT_NAME
python3 src/preprocessing/refactor_constructors.py $PROJECT_DIR_CONSTRUCTORS $PROJECT_NAME
