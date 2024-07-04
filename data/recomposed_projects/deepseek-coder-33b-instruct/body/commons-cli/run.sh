CURRENT_DIR=$(pwd)
export PYTHONPATH=$CURRENT_DIR
python3 -m pytest
xmllint --format pytest-report.xml -o pytest-report.xml