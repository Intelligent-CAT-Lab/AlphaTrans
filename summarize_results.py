from collections import defaultdict
import json
import argparse
import os

def emit_summary(project: str, dir: str):
    directory = f"{dir}/{project}/"

    # check if directory exists
    if not os.path.exists(directory):
        raise ValueError(f"Cannot find results for project {project} in directory {dir}")

    summary = defaultdict(list)

    # read all files in directory
    for filename in os.listdir(directory):
        if filename.endswith(".json") and "src.main." in filename:
            with open(f"{directory}/{filename}") as f:
                data = json.load(f)
                
                # find all failed methods (from test_execution)
                for class_name in data["classes"]:
                    for method in data["classes"][class_name]["methods"]:
                        if "test_execution" in data["classes"][class_name]["methods"][method]:
                            status = data["classes"][class_name]["methods"][method]["test_execution"]
                            if not isinstance(status, str):
                                if data["classes"][class_name]["methods"][method]["graal_validation"] == "not-exercised":
                                    print(f"\n{filename}::{class_name}::{method}\nAssociated Tests:")
                                    for test in status:
                                        print(f"{test} \t\t{status[test]['test_outcome']}")

    return summary

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize results from translation pipeline")
    parser.add_argument("--project", type=str, required=True, help="Project name")
    parser.add_argument("--dir", type=str, default="data/results/deepseek-coder-33b-instruct/body/", help="Directory containing results")
    args = parser.parse_args()

    print(json.dumps(emit_summary(args.project, args.dir), indent=4))
