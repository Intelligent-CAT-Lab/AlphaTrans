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
AlphaTrans currently supports prompting OpenAI models (e.g., `GPT-4o-2024-11-20`) and open-source models (e.g., `deepseek-ai/deepseek-coder-33b-instruct`) served by vLLM (please see the [vLLM Project](https://github.com/vllm-project/vllm) on how to start an engine). We have created a `.env` file to store API keys and model endpoints. If prompting with vLLM, please simply paste in your `VLLM_API_KEY` (set to `EMPTY` if you don't have a key) and `VLLM_API_URL` (e.g., `http://0.0.0.0:5000/v1` when the engine `IP` is `0.0.0.0` and `PORT` is `5000`). If prompting with OpenAI models, you only need to paste in your key in `OPENAI_API_KEY`.

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

AlphaTrans requires CodeQL for database creation and static analysis. Please install [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli) and then follow the steps below:

1. Clone the [vscode-codeql-starter](https://github.com/github/vscode-codeql-starter) repository into the root directory of this repository. Pull the `ql` submodule of this repository as directed in the README of the repository.
2. Place the project in `<project_directory>`. The `<project_directory>` can be `java_projects/original_projects`.
3. Create project database with CodeQL. Please see `create_database_java` function in [`setup.sh`](/setup.sh) as reference.
4. Copy all the contents of the [`queries`](/queries/) directory into the `vscode-codeql-starter/codeql-custom-queries-java` directory. `cd` into this directory and execute `bash simplify_script.sh <project_name> <project_name>`. Again, change the project name based on your new project.
5. Once all queries are executed, query outputs will be stored under `data/query_outputs_decomposed_tests`.

### 2. Program Transformation
Execute the following from the root directory of the repository to perform program transformation on the projects.

```
bash scripts/program_transformation.sh <project_dir> <project_name>
```

### 3. Program Decomposition

#### Source Decomposition
Execute the following for source decomposition from the root directory of the repository.

```bash
bash scripts/create_schema.sh
bash scripts/extract_call_graph.sh
```

#### Test Decomposition
Execute the following for test decomposition from the root directory of the repository.

```bash
bash scripts/decompose_test.sh
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

> [!NOTE]
> GraalVM must be installed on the system and the default Java path must be set to GraalVM's installation directory.

If a `pom.xml` does not already exist for the project, the script will copy the original `pom.xml` to the project directory and throw an exception. You are required to manually check that the Java version in the `pom.xml` is set to at least 8 and that GraalVM is included in the dependencies. Once this is done, you can run the script again.

### 6. Compositional Translation and Validation

Execute the following from the root directory of the repository to perform compositional translation and validation on the projects.

```bash
bash scripts/extract_coverage.sh <project_name>
bash scripts/translate_fragment.sh <project_name> <temperature> <model>
```

## Contact
We look forward to hearing your feedback. Please open an issue for any questions or comments 🙏.
