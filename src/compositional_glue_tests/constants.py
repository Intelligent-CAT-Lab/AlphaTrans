ORIGINAL_DIR = "java_projects/cleaned_final_projects"
OUTPUT_DIR = "java_projects/compositional_glue_tests"
OVERRIDES_DIR = "java_projects/overrides"
TRANSLATION_DIR = "data/translated_projects" # was: "data/verified_projects"
SKELETON_DIR = "data/skeletons"
SCHEMAS_DIR = "data/schemas"
CALLGRAPH_DIR = "data/call_graphs"

DIR_DEPTH = "../" * (len(list(filter(None, ORIGINAL_DIR.split("/")))) + 1) # the depth of a glued project from the root directory of this repository
SCRIPT_DIR_DEPTH = "../../" # the depth of this script from the root directory of this repository

paths = dict()
package_names = dict()

commons_projects = [
    ("commons-cli", "cli"),
    ("commons-codec", "codec"),
    ("commons-csv", "csv"),
    ("commons-fileupload", "fileupload"),
    ("commons-graph", "graph"),
    ("commons-pool", "pool2"),
    ("commons-validator", "validator"),
    ("commons-exec", "exec")
]

for project, code in commons_projects:
    paths[project] = {
        "main": f"main/java/org/apache/commons/{code}/",
        "test": f"test/java/org/apache/commons/{code}/",
    }
    package_names[project] = f"org.apache.commons.{code}"

paths["jansi"] = {
    "main": "src/main/java/org/fusesource/jansi/",
    "test": "src/test/java/org/fusesource/jansi/",
}
package_names["jansi"] = "org.fusesource.jansi"

paths["javafastpfor"] = {
    "main": "src/main/java/com/kamikaze/pfordelta/",
    "test": "src/test/java/com/kamikaze/pfordelta/",
}
package_names["javafastpfor"] = "com.kamikaze.pfordelta"
