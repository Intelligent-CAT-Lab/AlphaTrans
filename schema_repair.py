import copy
import os
import json
import argparse

ORIGINAL_SCHEMA = 'data/schemas/'
NEW_SCHEMA = 'data/schemas_decomposed_tests/'


def diff_and_repair(original, new):
    """
    Deeply compare two dictionaries or lists with scalar values,
    prioritizing the original schema.
    """
    if original == new:
        return

    if isinstance(original, dict) and isinstance(new, dict):
        for key in original:
            if key in ['path']:
                continue
            if key not in new:
                new[key] = original[key]
                continue                
            if not isinstance(original[key], dict) and not isinstance(original[key], list):
                if original[key] != new[key]:
                    new[key] = original[key]
                continue            
            diff_and_repair(original[key], new[key])
        keys_to_delete = []
        for key in new:
            if key not in original:
                keys_to_delete.append(key)
        for key in keys_to_delete:
            del new[key]
    elif isinstance(original, list) and isinstance(new, list):
        # ignore order of elements (but count of elements should be the same)
        if set(original) == set(new):
            if all(original.count(x) == new.count(x) for x in set(original)):
                return
        new.clear()
        new.extend(original)

def main(project: str):
    # get the common set of "main" schema files
    schema_files = set()
    schema_files.update(os.listdir(f"{ORIGINAL_SCHEMA}/{project}"))
    schema_files.update(os.listdir(f"{NEW_SCHEMA}/{project}"))
    schema_files = {f for f in schema_files if (
        'src.main' in f
        or ('src.test' in f and 'Test' not in f)
    )}
    
    # loop over the files and compare them
    for schema_file in schema_files:
        with open(f"{ORIGINAL_SCHEMA}/{project}/{schema_file}", 'r') as f:
            original_schema = json.load(f)
        with open(f"{NEW_SCHEMA}/{project}/{schema_file}", 'r') as f:
            new_schema = json.load(f)

        diff_and_repair(original_schema, new_schema)

        # save the repaired schema
        with open(f"{NEW_SCHEMA}/{project}/{schema_file}", 'w') as f:
            json.dump(new_schema, f, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Repair schema')
    parser.add_argument('--project', help='Project name', type=str)
    
    args = parser.parse_args()
    
    if args.project is None:
        projects = [
            'commons-cli',
            'commons-codec',
            'commons-csv',
            'commons-fileupload',
            'commons-validator',
            'commons-graph',
            'commons-exec',
            'commons-pool',
            'jansi',
            'JavaFastPFOR'
        ]
        for project in projects:
            print(f"Repairing {project}...")
            main(project)
    
    else:
        main(args.project)
