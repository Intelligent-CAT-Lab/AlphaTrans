# AlphaTrans
This repository contains artifacts of the project

## Pre-requisites
<!-- Python Pre-requisites TBA (if any) -->
The `setup.sh` files contains multiple scripts to setup the proper conda environment and install all dependencies. Please execute the following in order to successfully install all pre-requisites:

### Setting up conda environment:
```
bash setup.sh setup_env
```

You may need to execute `conda deactivate` and `conda activate alphatrans` to properly activate the installed conda environment.

### Installing python dependencies:
```
bash setup.sh install_requirements
```

This command will install the proper versions of all python dependencies using python-pip.

### Downloading java subjects:
```
bash setup.sh download_java_projects
bash setup.sh build_java_projects
bash setup.sh create_database_java
```

This command will download the original snapshots of all java subjects we used in this work from GitHub. It then builds these projects to make sure we can successfully build these projects and finally create their CodeQL databases. Please make sure [CodeQL](https://codeql.github.com/) is installed on your machine.

### Installing Graal
For running graal-based scripts, both GraalVM and its python component must be installed on the system. The recommended version of the GraalVM JDK is 17.0.8. Please run the following command to install graal.
```
bash setup.sh install_graal
```
> [!NOTE]
> The script uses SDKMAN! to install GraalVM and set the $JAVA_HOME variable automatically. If $JAVA_HOME is still not set, restart the terminal or switch to the GraalVM JDK by running `sdk use java 17.0.8-graal` after installation.

To verify that GraalVM is installed correctly, run:
```bash
java --version
```
The output should be similar to:
```bash
java 17.0.8 2023-07-18 LTS
Java(TM) SE Runtime Environment Oracle GraalVM 17.0.8+9.1 (build 17.0.8+9-LTS-jvmci-23.0-b14)
Java HotSpot(TM) 64-Bit Server VM Oracle GraalVM 17.0.8+9.1 (build 17.0.8+9-LTS-jvmci-23.0-b14, mixed mode, sharing)
```

## Skeleton Generation
Execute the following from the root directory of the repository to generate skeletons of projects and check their syntactical correctness

```bash
bash scripts/create_skeleton.sh
```

This command should create proper skeletons in target language under `data/skeletons/<project_name>`.

---

### Generate Skeleton for a New Project

1. Install the [CodeQL CLI](https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli).
2. Clone the [vscode-codeql-starter](https://github.com/github/vscode-codeql-starter) repository into the root directory of this repository. Pull the `ql` submodule of this repository as directed in the README of the repository.
3. Place the project in `java_projects/cleaned_final_projects`.
4. Execute `codeql database create ../../../databases/<NameOfProject> --language=java --overwrite` from the project directory. This will create the database for the project.
5. Copy all the contents of the `queries` directory into the `vscode-codeql-starter/codeql-custom-queries-java` directory. `cd` into this directory and execute `run.sh`.
6. From the root directory, now execute the following.
```bash
python src/static_analysis/extract_call_graph.py --project_name <NameOfProject>
python src/static_analysis/create_schema.py --project_name <NameOfProject>
python utils.py --project_name <NameOfProject> --function parse_dependencies

# the following command may fail due to unknown types in the new project
python src/static_analysis/create_skeleton.py --project_name <NameOfProject>
```

## Graal-based Semantic Check
Execute the following from the root directory of the project to run the Graal-based semantic check.
```bash
python src/compositional_glue_tests/semantic_check.py --project <project_name> [--class=<class_name>] [--method=<method_name>]
```

> [!NOTE]
> GraalVM must be installed on the system and the default Java path must be set to GraalVM's installation directory.

If a `pom.xml` does not already exist for the project, the script will copy the original `pom.xml` to the project directory and throw an exception. You are required to manually check that the Java version in the `pom.xml` is set to at least 8 and that GraalVM is included in the dependencies. Once this is done, you can run the script again.
