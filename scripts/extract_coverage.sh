#!/bin/bash

PROJECT=$1

python3 src/static_analysis/create_test_method_map.py --project_name=$PROJECT --suffix=_decomposed_tests
python3 src/static_analysis/extract_source_tests.py --project_name=$PROJECT --suffix=_decomposed_tests
