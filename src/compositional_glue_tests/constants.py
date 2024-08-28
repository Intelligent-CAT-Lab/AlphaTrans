USE_DECOMPOSED_TESTS = True

suffix = "_decomposed_tests" if USE_DECOMPOSED_TESTS else ""
ORIGINAL_DIR = f"java_projects/cleaned_final_projects{suffix}"
OUTPUT_DIR = "java_projects/compositional_glue_tests"
OVERRIDES_DIR = "java_projects/overrides"
TRANSLATION_DIR = "data/translated_projects"
COVERAGE_DIR = f"data/source_test_execution{suffix}"

DIR_DEPTH = "../" * (len(list(filter(None, ORIGINAL_DIR.split("/")))) + 1) # the depth of a glued project from the root directory of this repository
SCRIPT_DIR_DEPTH = "../../" # the depth of this script from the root directory of this repository


class CaseInsensitiveDict:
    """
    Light-weight implementation of case-insensitive dictionary for constants.
    """

    def __init__(self):
        self.__store = dict()

    def __setitem__(self, key, value):
        self.__store[key.lower()] = (key, value)

    def __getitem__(self, key):
        return self.__store[key.lower()][1]

    def __contains__(self, key):
        return key.lower() in self.__store


paths = CaseInsensitiveDict()
package_names = CaseInsensitiveDict()

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
    "main": "main/java/org/fusesource/jansi/",
    "test": "test/java/org/fusesource/jansi/",
}
package_names["jansi"] = "org.fusesource.jansi"

paths["javafastpfor"] = {
    "main": "main/java/com/kamikaze/pfordelta/",
    "test": "test/java/com/kamikaze/pfordelta/",
}
package_names["javafastpfor"] = "com.kamikaze.pfordelta"
