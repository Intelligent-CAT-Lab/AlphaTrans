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
bash scripts/get_dependencies.sh _decomposed_tests
bash scrtips/generate_test_invocation_map.sh _decomposed_tests
bash scripts/extract_coverage.sh _decomposed_tests
bash scripts/translate_fragment.sh commons-cli 0.0 gpt-4o-2024-11-20
```

This script will translate the project fragment by fragment in reverse-call graph order and store translations in JSON files along with validation results (e.g., syntactical correctness, GraalVM correctness, test execution correctness, etc.). If you want to create standalone python projects, simply recompose all translations with the following script:

```
bash scripts/recompose.sh commons-cli 0.0 gpt-4o-2024-11-20
```

## Translate New Java Projects
In this section, we discuss how to add more projects and translate with AlphaTrans. Below, we provide the steps for the ten subject projects in our work. If you add a new project, it should be similar to existing ones. For every project, we provide two specific snapshots as shown below:

1. [`original_projects`](/java_projects/original_projects): Original snapshot of the projects cloned from GitHub.
2. [`cleaned_final_projects_decomposed_tests`](/java_projects/cleaned_final_projects_decomposed_tests/): Snapshot of the `original_projects` with third-party libraries removed, overload methods/constructors transformed, and tests decomposed.

You can start experimenting from the second snapshot (`cleaned_final_projects_decomposed_tests`) as project reduction, transformation, and decomposition can potentially take hours. Please refer to [Project Reduction, Program Transformation and Test Decomposition](#project-reduction-program-transformation-and-test-decomposition) for further preprocessing steps.

### 1. CodeQL Database Creation & Static Analysis

AlphaTrans requires [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli) for database creation and static analysis of projects. We already install CodeQL using Docker. We also clone the [vscode-codeql-starter](https://github.com/github/vscode-codeql-starter) repository required for executing CodeQL queries. Please follow the steps below to create project database and execute queries on [`cleaned_final_projects_decomposed_tests`](/java_projects/cleaned_final_projects_decomposed_tests/):

#### Create CodeQL Project Database
Create project database with CodeQL by executing the following script:
```
bash scripts/create_database.sh _decomposed_tests
```
After successful execution, the databases should be created under `databases/<project_name>_decomposed_tests`.

#### Execute CodeQL Queries
We have already copied all CodeQL files from [`queries`](/queries/) into the `vscode-codeql-starter/codeql-custom-queries-java` directory. Execute the following to run all necessary CodeQL queries:
```
cd vscode-codeql-starter/codeql-custom-queries-java
bash run.sh
```
Once all queries are executed, query outputs will be stored under `data/query_outputs_decomposed_tests`.

### 2. Program Decomposition

Execute the following to decompose programs and create project schemas:
```
bash scripts/create_schema.sh _decomposed_tests
bash scripts/extract_call_graph.sh _decomposed_tests
```
These scripts will properly store project schemas in JSON format under `data/schemas_decomposed_tests`.

### 3. Type Translation
We provide our universal type map under [`data/type_resolution/universal_type_map_final.json`](/data/type_resolution/universal_type_map_final.json). This type map can be directly used, however, if you want to translate types again, please execute the following from the root directory of the repository to perform type translation on the projects.

```
bash scripts/extract_types.sh
bash scripts/crawl_type_desc.sh
bash scripts/translate_types.sh <type>
```

The `<type>` can be either `simple` or `source_description`. The former prompts the model with vanilla prompt, while the latter prompts the model with source PL type description.

### 4. Skeleton Construction
Execute the following from the root directory of the repository to generate skeletons of projects and check their syntactical correctness

```bash
bash scripts/get_dependencies.sh _decomposed_tests
bash scripts/create_skeleton.sh _decomposed_tests
```

This command should create proper skeletons in target language under `data/skeletons/<project_name>`.

### 5. Compositional Translation and Validation

Finally, execute the following from the root directory of the repository to perform compositional translation and validation on the projects.

```bash
bash scrtips/generate_test_invocation_map.sh _decomposed_tests
bash scripts/extract_coverage.sh _decomposed_tests
bash scripts/translate_fragment.sh <project_name> <temperature> <model>
```

You can use `project_name=commons-cli`, `temperature=0.0`, and `model=gpt-4o-2024-11-20` as an example.

## Project Reduction, Program Transformation and Test Decomposition
In this section, we provide the steps on how to get rid of third-party libraries from original projects.

### 1. Project Reduction

#### Add the Maven JAR Plugin

Run the following script to add the `maven-jar-plugin` to a project for a test jar:
```
bash scripts/add_plugin.sh <project_name>
```

#### Build and Merge Source and Test JARs
Run this script to build the project and merge the source and test JARs:
```
bash scripts/merge_jar.sh <project_name>
```

#### Generate a Call Graph

Generate a simple call graph (via JavaCG) of the entire project using the merged JAR:
```
bash scripts/generate_cg.sh <project_name>
```

#### Reduce Project
```
python3 src/preprocessing/reduce_third_party_libs.py <project_name>
```
The project name is the name of a directory from `/java_projects/original_projects`. After reduction, a directory of the same name will appear under `/java_projects/automated_reduced_projects/`.

### 2. Program Transformation
Execute the following from the root directory of the repository to perform program transformation on a specific project.

```
bash scripts/program_transformation.sh <project_dir_overload_methods> <project_dir_overload_constructors> <project_name>
```

### 3. Test Decomposition
AlphaTrans performs test decomposition on transformed projects as a step to address the long-call chain problem when executing tests in target language. Please execute the following to first extract executed tests and their coverage, and use this information to decompose tests properly:
```
bash scripts/extract_coverage.sh ''
```
Once this executes properly, it should create a directory called `source_test_execution` under [`data`](/data/). Then execute the following to decompose tests:
```
bash scripts/decompose_test.sh
```
After successful execution, this should create the [`cleaned_final_projects_decomposed_tests`](/java_projects/cleaned_final_projects_decomposed_tests/) directory under [`java_projects`](/java_projects/).

> [!NOTE]
> There might be a need to do some small manual changes after test decomposition. For instance removing `@Test(expected = IllegalArgumentException.class)` from test annotation as we do not know ahead of time which decomposed tests throw exception. Please refer to our reference decomposed tests (e.g., [`cleaned_final_projects_decomposed_tests`](/java_projects/cleaned_final_projects_decomposed_tests/)) for specific examples. A project with decomposed tests is considered ok as long as it can be compiled by maven.

## Contact
We look forward to hearing your feedback. Please open an issue for any questions or comments 🙏.
