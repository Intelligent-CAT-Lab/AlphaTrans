# AlphaTrans
This repository contains artifacts of the paper "Repository-Level Compositional Code Translation and Validation".

## Generated Artifacts
All artifacts generated during experiments are available online on Zenodo. The link to the Zenodo repository is [here](https://zenodo.org/records/13826661).

## Manually Verified Translations
All manually verified translations from 4 projects are available online on Zenodo. The link to the Zenodo repository is [here](https://zenodo.org/records/13826661).

## Pre-requisites
The `setup.sh` files contains multiple scripts to setup the proper conda environment, install all dependencies, download, build, and create project databases for CodeQL, and install GraalVM. Please execute the following in order to successfully setup AlphaTrans requirements.

### 1. Setting up conda environment:
```
bash setup.sh setup_env
```

You may need to execute `conda deactivate` and `conda activate alphatrans` to properly activate the installed conda environment in your current bash terminal.

### 2. Installing Python dependencies:
```
bash setup.sh install_requirements
```

This command will install the proper versions of all python dependencies using python-pip.

### 3. Downloading Java subjects:
```
bash setup.sh download_java_projects
bash setup.sh build_java_projects
bash setup.sh create_database_java
```

This command will download the original snapshots of all java subjects we used in this work from GitHub. It then builds these projects to make sure we can successfully build these projects and finally create their CodeQL databases. Please make sure [CodeQL](https://codeql.github.com/) is installed on your machine.

### 4. Installing GraalVM
For running graal-based scripts, both GraalVM and its python component must be installed on the system. The recommended version of the GraalVM JDK is 21.0.3. Please run the following command to install graal.
```
bash setup.sh install_graal
```
> [!NOTE]
> The script uses SDKMAN! to install GraalVM and set the $JAVA_HOME variable automatically. If $JAVA_HOME is still not set, restart the terminal or switch to the GraalVM JDK by running `sdk use java 21.0.3-graal` after installation.

To verify that GraalVM is installed correctly, run:
```bash
java --version
```
The output should be similar to:
```bash
java 21.0.3 2024-04-16 LTS
Java(TM) SE Runtime Environment Oracle GraalVM 21.0.3+7.1 (build 21.0.3+7-LTS-jvmci-23.1-b37)
Java HotSpot(TM) 64-Bit Server VM Oracle GraalVM 21.0.3+7.1 (build 21.0.3+7-LTS-jvmci-23.1-b37, mixed mode, sharing)
```

## CodeQL-based Static Analysis

AlphaTrans requires CodeQL for database creation and static analysis. We did database creation previously, and now the following steps describes how to use CodeQL to query and extract its generated outputs for all subject projects.

1. Install the [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli).
2. Clone the [vscode-codeql-starter](https://github.com/github/vscode-codeql-starter) repository into the root directory of this repository. Pull the `ql` submodule of this repository as directed in the README of the repository.
3. Place the project in `<project_directory>`. The `<project_directory>` can be `java_projects/original_projects`.
4. Copy all the contents of the `queries` directory into the `vscode-codeql-starter/codeql-custom-queries-java` directory. `cd` into this directory and execute `run.sh`.
5. Once all queries are executed, query outputs will be stored under `data/query_outputs`.

## Program Transformation
Execute the following from the root directory of the repository to perform program transformation on the projects.

```bash
bash scripts/program_transformation.sh <project_dir> <project_name>
```

## Program Decomposition

### Source Decomposition
Execute the following for source decomposition from the root directory of the repository.

```bash
bash scripts/create_schema.sh
bash scripts/extract_call_graph.sh
```

### Test Decomposition
Execute the following for test decomposition from the root directory of the repository.

```bash
bash scripts/decompose_test.sh
```

## Type Translation
Execute the following from the root directory of the repository to perform type translation on the projects.

```bash
bash scripts/extract_types.sh
bash scripts/crawl_type_desc.sh
bash scripts/translate_types.sh <type>
```

The `<type>` can be either `simple` or `source_description`. The former prompts the model with vanilla prompt, while the latter prompts the model with source PL type description.

## Skeleton Construction
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

## Compositional Translation and Validation

Execute the following from the root directory of the repository to perform compositional translation and validation on the projects.

```bash
bash scripts/extract_coverage.sh <project_name>
bash scripts/translate_fragment.sh <project_name>
```
