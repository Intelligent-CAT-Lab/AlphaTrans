ORIGINAL_DIR = "java_projects/cleaned_final_projects"
OUTPUT_DIR = "java_projects/compositional_glue_tests"
TRANSLATION_DIR = "data/translated_projects" # was: "data/verified_projects"
SKELETON_DIR = "data/skeletons"
SCHEMAS_DIR = "data/schemas"

DIR_DEPTH = "../" * (len(list(filter(None, ORIGINAL_DIR.split("/")))) + 1) # the depth of a glued project from the root directory of this repository
SCRIPT_DIR_DEPTH = "../../" # the depth of this script from the root directory of this repository

paths = dict()
paths.update({k: {
        "main": f"main/java/org/apache/commons/{v}/",
        "test": f"test/java/org/apache/commons/{v}/",
    } for k, v in (
    ("commons-cli", "cli"),
    ("commons-codec", "codec"),
    ("commons-csv", "csv"),
    ("commons-fileupload", "fileupload"),
    ("commons-graph", "graph"),
    ("commons-pool", "pool2"),
    ("commons-validator", "validator"),
)})
paths.update({k: {
        "main": f"main/java/org/joda/{v}/",
        "test": f"test/java/org/joda/{v}/",
    } for k, v in (
    ("joda-convert", "convert"),
    ("joda-money", "money"),
)})

package_names = {}
package_names.update({k: f"org.apache.commons.{v}" for k, v in (
    ("commons-cli", "cli"),
    ("commons-codec", "codec"),
    ("commons-csv", "csv"),
    ("commons-fileupload", "fileupload"),
    ("commons-graph", "graph"),
    ("commons-pool", "pool"),
    ("commons-validator", "validator"),
)})
package_names.update({k: f"org.joda.{v}" for k, v in (
    ("joda-convert", "convert"),
    ("joda-money", "money"),
)})
