# AlphaTrans
This repository contains artifacts of AlphaTrans from the paper ["Repository-Level Compositional Code Translation and Validation"](https://arxiv.org/abs/2410.24117).

## Getting Started
We provide a [`Dockerfile`](/Dockerfile) which installs all necessary dependencies to reproduce the results of AlphaTrans. Please execute the following to create a docker image and execute the container in interactive mode:

```
docker build --no-cache -t alphatrans .
docker run -it alphatrans bash
```

Please refer to [Reproduce AlphaTrans Results](#reproduce-alphatrans-results) for instructions on how to reproduce the results of AlphaTrans. If you are interested in translating more projects, please refer to [Translate New Java Projects](#translate-new-java-projects).

## Reproduce AlphaTrans Results
AlphaTrans currently supports prompting OpenAI models (e.g., `GPT-4o-2024-11-20`) and open-source models (e.g., `deepseek-ai/deepseek-coder-33b-instruct`) served by ollama (please see the [Ollama Project](https://ollama.com/) on how to start an engine). We have created a `.env` file to store API keys and model endpoints. If prompting with ollama, please simply paste in your `OLLAMA_HOST` (e.g., `http://0.0.0.0:5000` when the engine `IP` is `0.0.0.0` and `PORT` is `5000`). If prompting with OpenAI models, you only need to paste in your key in `OPENAI_API_KEY`.

```
vim .env
```

For all ten projects, we provide the project skeletons and partial translations. Please execute the following to start translating projects (e.g., `commons-cli` with `deepseek-coder-33b-instruct` model with `temperature=0.0`):

```
bash scripts/translate_fragment.sh commons-cli 0.0 deepseek-coder-33b-instruct
```

This script will translate the project fragment by fragment in reverse-call graph order and store translations in JSON files along with validation results (e.g., syntactical correctness, GraalVM correctness, test execution correctness, etc.). If you want to create standalone python projects, simply recompose all translations with the following script:

```
bash scripts/recompose.sh commons-cli 0.0 deepseek-coder-33b-instruct
```

## Translate New Java Projects
If you are interested in building on top of AlphaTrans and add more projects, please follow the following steps:

### 1. CodeQL Database Creation & Static Analysis

AlphaTrans requires [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli) for database creation and static analysis. We already install CodeQL using Docker. We also clone the [vscode-codeql-starter](https://github.com/github/vscode-codeql-starter) repository required for executing CodeQL queries.

First, from the root of the repository, execute the following to create a CodeQL database for your project.

```bash
mkdir -p databases

cd path/to/project/<project_name>
# eg. cd java_projects/cleaned_final_projects/commons-cli

codeql database create /path/to/databases/<project_name> --language=java --overwrite
# eg. codeql database create ../../../databases/commons-cli --language=java --overwrite
```

Now, to execute CodeQL queries, return to the root of the repository and execute the following.

```bash
cd vscode-codeql-starter/codeql-custom-queries-java/

bash execute_codeql_queries.sh <project_name> <project_name> /path/to/output_directory
# eg. bash execute_codeql_queries.sh commons-cli commons-cli query_outputs
```

The query outputs will be saved under `data/output_directory`.

### 2. Program Transformation
Execute the following from the root directory of the repository to perform program transformation on the projects.

```bash
bash scripts/program_transformation.sh path/to/project <project_name>
# eg. bash scripts/program_transformation.sh java_projects/cleaned_final_projects commons-cli
```

### 3. Program Decomposition

#### Source Decomposition
Execute the following for source decomposition from the root directory of the repository.

```bash
python3 src/static_analysis/create_schema.py --project_name=<project_name> --suffix=_decomposed_tests
python3 src/static_analysis/extract_call_graph.py --project_name=<project_name> --suffix=_decomposed_tests
```

#### Test Decomposition
Execute the following for test decomposition from the root directory of the repository.

```bash
python3 src/static_analysis/decompose_dev_test.py --project_name=<project_name>
```

### 4. Type Translation
Execute the following from the root directory of the repository to perform type translation on the projects.

```bash
bash scripts/extract_types.sh
bash scripts/crawl_type_desc.sh
bash scripts/translate_types.sh <type>
```

The `<type>` can be either `simple` or `source_description`. The former prompts the model with vanilla prompt, while the latter prompts the model with source PL type description.

### 5. Skeleton Construction
Execute the following from the root directory of the repository to generate skeletons of projects and check their syntactical correctness

```bash
bash scripts/get_dependencies.sh
bash scripts/create_skeleton.sh
```

This command should create proper skeletons in target language under `data/skeletons/<project_name>`.

Execute the following from the root directory of the project to run the Graal-based semantic check of generated skeletons.
```bash
python src/compositional_glue_tests/semantic_check.py --project <project_name> [--class=<class_name>] [--method=<method_name>]
```

If a `pom.xml` does not already exist for the project, the script will copy the original `pom.xml` to the project directory and throw an exception. You are required to manually check that the Java version in the `pom.xml` is set to at least 8 and that GraalVM is included in the dependencies. Once this is done, you can run the script again.

### 6. Compositional Translation and Validation

Execute the following from the root directory of the repository to perform compositional translation and validation on the projects.

```bash
bash scripts/extract_coverage.sh <project_name>
bash scripts/translate_fragment.sh <project_name> <temperature> <model>
```

## Contact
We look forward to hearing your feedback. Please open an issue for any questions or comments 🙏.
