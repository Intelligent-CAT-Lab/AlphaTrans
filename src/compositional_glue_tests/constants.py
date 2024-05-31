ORIGINAL_DIR = "java_projects/cleaned_final_projects"
OUTPUT_DIR = "java_projects/compositional_glue_tests"
TRANSLATION_DIR = "data/verified_projects"
SKELETON_DIR = "data/skeletons"
SCHEMAS_DIR = "data/schemas"

DIR_DEPTH = "../" * (len(list(filter(None, ORIGINAL_DIR.split("/")))) + 1) # the depth of a glued project from the root directory of this repository
SCRIPT_DIR_DEPTH = "../../" # the depth of this script from the root directory of this repository

main_paths = {
    "commons-fileupload": "main/java/org/apache/commons/fileupload/",
    "commons-cli": "main/java/org/apache/commons/cli/",
    "commons-codec": "main/java/org/apache/commons/codec/",
    "commons-csv": "main/java/org/apache/commons/csv/",
    "commons-graph": "main/java/org/apache/commons/graph/",
    "commons-pool": "main/java/org/apache/commons/pool2/",
    "commons-validator": "main/java/org/apache/commons/validator/",
    "joda-convert": "main/java/org/joda/convert/",
    "joda-money": "main/java/org/joda/money/",
}
test_paths = {
    "commons-fileupload": "test/java/org/apache/commons/fileupload/",
    "commons-cli": "test/java/org/apache/commons/cli/",
    "commons-codec": "test/java/org/apache/commons/codec/",
    "commons-csv": "test/java/org/apache/commons/csv/",
    "commons-graph": "test/java/org/apache/commons/graph/",
    "commons-pool": "test/java/org/apache/commons/pool2/",
    "commons-validator": "test/java/org/apache/commons/validator/",
    "joda-convert": "test/java/org/joda/convert/",
    "joda-money": "test/java/org/joda/money/",
}

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
