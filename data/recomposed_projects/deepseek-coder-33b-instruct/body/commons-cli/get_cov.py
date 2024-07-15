import coverage
# Start coverage
cov = coverage.Coverage()
cov.start()
# Run your test
import pytest
pytest.main(['src/test/org/apache/commons/cli/bug/BugsTest.py::BugsTest::test31148'])
# Stop coverage
cov.stop()
cov.save()
# Analyze the coverage data
covered_methods = []
for file_report in cov.get_data().measured_files():
    analysis = cov._analyze(file_report)

    for covered_line in analysis.executed:
        print(analysis.statements)
        method = analysis.statement_to_function[covered_line]
        covered_methods.append(method)
# Print covered methods
for method in covered_methods:
    print(method)
