import argparse
import os
import json

if __name__ == '__main__':
    # accept a command line argument "project_name"\
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_name", help="The name of the project", dest="project_name", required=True)
    args = parser.parse_args()
    
    # load up all the schemas in data/schemas/project_name
    schema_dir = os.path.join("data", "schemas", args.project_name)
    schemas = []
    for file in os.listdir(schema_dir):
        if file.endswith(".json"):
            schemas.append(file)
            
    # for every method in every class in every schema, set translation_status to 'failure'
    for schema in schemas:
        with open(os.path.join(schema_dir, schema), 'r') as f:
            schema_data = json.load(f)
        for _class in schema_data['classes']:
            for method in schema_data['classes'][_class]['methods']:
                schema_data['classes'][_class]['methods'][method]['translation_status'] = 'failure'
                
        # write the schema back to the file
        with open(os.path.join(schema_dir, schema), 'w') as f:
            json.dump(schema_data, f, indent=4)   
