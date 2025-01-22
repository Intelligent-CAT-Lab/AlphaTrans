#!/bin/bash

project=$1
suffix=$2

echo "extracting test coverage for $project"
python3 src/static_analysis/extract_source_tests.py --project_name=$project --suffix=$suffix
