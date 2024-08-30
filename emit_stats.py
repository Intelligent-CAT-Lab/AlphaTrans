import json
import argparse

def emit_stats(project: str):
    filename = f"{project}_results.jsonl"
    
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return f"File {filename} not found"

    data = [json.loads(line) for line in lines]

    total = len(data)
    not_exercised_count = 0
    error_unsupported_fragment_count = 0
    error_unsupported_operation_count = 0
    error_timeout_count = 0
    error_other_count = 0
    fail_1_count = 0
    fail_many_count = 0
    passed = 0
    
    for item in data:
        if item['status'] == 'not-exercised':
            not_exercised_count += 1
        
        if item['status'] == 'error':
            if item['message'].startswith('Unsupported fragment'):
                error_unsupported_fragment_count += 1
            elif item['message'].startswith('Unsupported operation'):
                error_unsupported_operation_count += 1
            elif item['message'].startswith('Timeout'):
                error_timeout_count += 1
            else:
                error_other_count += 1
        
        if item['status'] == 'failure':
            failed_tests_count = len(item['message'].split('\n'))
            if failed_tests_count == 1:
                fail_1_count += 1
            elif failed_tests_count > 1:
                fail_many_count += 1
        
        if item['status'] == 'success':
            passed += 1

    total_error_count = error_unsupported_fragment_count + error_unsupported_operation_count + error_timeout_count + error_other_count
    total_fail_count = fail_1_count + fail_many_count
    
    return total, not_exercised_count, total_error_count, error_unsupported_fragment_count, error_unsupported_operation_count, error_timeout_count, error_other_count, total_fail_count, fail_1_count, fail_many_count, passed

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Emit stats from JSONL result files')
    parser.add_argument('--project', type=str, required=True, help='Project name')
    args = parser.parse_args()

    print(*emit_stats(args.project), sep=", ")
