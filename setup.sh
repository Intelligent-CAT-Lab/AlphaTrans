
function setup_env() {
    conda create -n alphatrans python=3.10.8;       # miniconda 23.5.2 download from https://docs.conda.io/en/latest/miniconda_hashes.html
    conda activate alphatrans;
    # conda install maven-3.9.4-hce30654_0.conda;     # download from https://anaconda.org/conda-forge/maven/files
    # conda install openjdk-17.0.3-hbe7ddab_8.conda;  # download from https://anaconda.org/conda-forge/openjdk/files
}

function install_requirements() {
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118;
    pip3 install tqdm==4.66.1;
    pip3 install graphviz==0.20.1;
    pip3 install python-dotenv==1.0.0;
    pip3 install openai==0.27.8;
    pip3 install tiktoken==0.3.2;
    pip3 install python-dotenv==1.0.0;
    pip3 install accelerate==0.24.1;
    pip3 install black==24.4.2;
    pip3 install transformers==4.34.1;
    pip3 install pynguin==0.36.0;
    pip3 install ibm-generative-ai==3.0.0;
}

function download_java_projects() {
    mkdir -p java_projects;
    main=`pwd`;

    git clone https://github.com/apache/commons-fileupload.git java_projects/original_projects/commons-fileupload;
    cd java_projects/original_projects/commons-fileupload;
    git reset --hard commons-fileupload-1.5;
    cd $main;

    git clone https://github.com/apache/commons-validator.git java_projects/original_projects/commons-validator;
    cd java_projects/original_projects/commons-validator;
    git reset --hard VALIDATOR_1_7;
    cd $main;

    git clone https://github.com/apache/commons-codec.git java_projects/original_projects/commons-codec;
    cd java_projects/original_projects/commons-codec;
    git reset --hard commons-codec-1.16-rc1;
    cd $main;

    git clone https://github.com/apache/commons-pool.git java_projects/original_projects/commons-pool;
    cd java_projects/original_projects/commons-pool;
    git reset --hard rel/commons-pool-2.11.1;
    cd $main;

    git clone https://github.com/apache/commons-cli.git java_projects/original_projects/commons-cli;
    cd java_projects/original_projects/commons-cli;
    git reset --hard commons-cli-1.5.0;
    cd $main;

    git clone https://github.com/apache/commons-csv.git java_projects/original_projects/commons-csv;
    cd java_projects/original_projects/commons-csv;
    git reset --hard rel/commons-csv-1.10.0;
    cd $main;

    git clone https://github.com/apache/commons-graph.git java_projects/original_projects/commons-graph;
    cd java_projects/original_projects/commons-graph;
    git reset --hard 93d2ba7;
    cd $main;

    git clone https://github.com/JodaOrg/joda-money.git java_projects/original_projects/joda-money;
    cd java_projects/original_projects/joda-money;
    git reset --hard v1.0.4;
    cd $main;

    git clone https://github.com/JodaOrg/joda-convert.git java_projects/original_projects/joda-convert;
    cd java_projects/original_projects/joda-convert;
    git reset --hard v2.2.3;
    cd $main;

    git clone https://github.com/apache/commons-exec.git java_projects/original_projects/commons-exec;
    cd java_projects/original_projects/commons-exec;
    git reset --hard rel/commons-exec-1.4.0;
    cd $main;

    git clone https://github.com/FasterXML/jackson-core.git java_projects/original_projects/jackson-core;
    cd java_projects/original_projects/jackson-core;
    git reset --hard jackson-core-2.12.0;
    cd $main;

    git clone https://github.com/fusesource/jansi.git java_projects/original_projects/jansi;
    cd java_projects/original_projects/jansi;
    git reset --hard 045fd56;
    cd $main;

    git clone https://github.com/stleary/JSON-java.git java_projects/original_projects/JSON-java;
    cd java_projects/original_projects/JSON-java;
    git reset --hard 20240303;
    cd $main;

    git clone https://github.com/tbsalling/aismessages.git java_projects/original_projects/aismessages;
    cd java_projects/original_projects/aismessages;
    git reset --hard aismessages-2.2.4;
    cd $main;

    git clone https://github.com/lemire/javaewah.git java_projects/original_projects/javaewah;
    cd java_projects/original_projects/javaewah;
    git reset --hard JavaEWAH-1.2.3;
    cd $main;

    git clone https://github.com/fasseg/exp4j.git java_projects/original_projects/exp4j;
    cd java_projects/original_projects/exp4j;
    git reset --hard 4657309;
    cd $main;

    git clone https://github.com/lemire/JavaFastPFOR.git java_projects/original_projects/JavaFastPFOR;
    cd java_projects/original_projects/JavaFastPFOR;
    git reset --hard 0ecdda9;
    cd $main;

    git clone https://github.com/gbenroscience/ParserNG.git java_projects/ParserNG;
    cd java_projects/original_projects/ParserNG;
    git reset --hard v0.1.9;
    cd $main;
}

function build_java_projects() {
    main=`pwd`;
    projects_dir=java_projects;

    echo "building commons-fileupload";
    cd $projects_dir/commons-fileupload;
    mvn clean test --log-file build.log;
    cd $main;

    echo "building commons-validator";
    cd $projects_dir/commons-validator;
    mvn clean test --log-file build.log;
    cd $main;

    echo "building commons-codec";
    cd $projects_dir/commons-codec;
    mvn clean test --log-file build.log;
    cd $main;

    echo "building commons-pool";
    cd $projects_dir/commons-pool;
    mvn clean test --log-file build.log;
    cd $main;

    echo "building commons-cli";
    cd $projects_dir/commons-cli;
    mvn clean test --log-file build.log;
    cd $main;

    echo "building commons-csv";
    cd $projects_dir/commons-csv;
    mvn clean test --log-file build.log;
    cd $main;

    echo "building commons-graph";
    cd $projects_dir/commons-graph;
    mvn clean test --log-file build.log;
    cd $main;

    echo "building joda-money";
    cd $projects_dir/joda-money;
    mvn clean test --log-file build.log;
    cd $main;

    echo "building joda-convert";
    cd $projects_dir/joda-convert;
    mvn clean test --log-file build.log;
    cd $main;
}

function create_database_java() {
    mkdir -p databases;
    main=`pwd`;

    suffix=_decomposed_tests;
    projects_dir=java_projects/cleaned_final_projects${suffix};

    cd $projects_dir/commons-fileupload;
    codeql database create ../../../databases/commons-fileupload$suffix --language=java --overwrite;
    cd $main;

    cd $projects_dir/commons-validator;
    codeql database create ../../../databases/commons-validator$suffix --language=java --overwrite;
    cd $main;

    cd $projects_dir/commons-codec;
    codeql database create ../../../databases/commons-codec$suffix --language=java --overwrite;
    cd $main;

    cd $projects_dir/commons-pool;
    codeql database create ../../../databases/commons-pool$suffix --language=java --overwrite;
    cd $main;

    cd $projects_dir/commons-cli;
    codeql database create ../../../databases/commons-cli$suffix --language=java --overwrite;
    cd $main;

    cd $projects_dir/commons-csv;
    codeql database create ../../../databases/commons-csv$suffix --language=java --overwrite;
    cd $main;

    cd $projects_dir/commons-graph;
    codeql database create ../../../databases/commons-graph$suffix --language=java --overwrite;
    cd $main;

    # cd $projects_dir/joda-money;
    # codeql database create ../../../databases/joda-money$suffix --language=java --overwrite;
    # cd $main;

    # cd $projects_dir/joda-convert;
    # codeql database create ../../../databases/joda-convert$suffix --language=java --overwrite;
    # cd $main;

    cd $projects_dir/commons-exec;
    codeql database create ../../../databases/commons-exec$suffix --language=java --overwrite;
    cd $main;

    # cd $projects_dir/jackson-core;
    # codeql database create ../../../databases/jackson-core$suffix --language=java --overwrite;
    # cd $main;

    cd $projects_dir/jansi;
    codeql database create ../../../databases/jansi$suffix --language=java --overwrite;
    cd $main;

    cd $projects_dir/JavaFastPFOR;
    codeql database create ../../../databases/JavaFastPFOR$suffix --language=java --overwrite;
    cd $main;

    # cd $projects_dir/aismessages;
    # codeql database create ../../../databases/aismessages$suffix --language=java --overwrite;
    # cd $main;

    # cd $projects_dir/javaewah;
    # codeql database create ../../../databases/javaewah$suffix --language=java --overwrite;
    # cd $main;
}

function install_graal() {
    curl -s https://get.sdkman.io | bash
    source "$HOME/.sdkman/bin/sdkman-init.sh"
    sdk install java 21.0.3-graal

    if [ $? -eq 0 ]; then
        echo -e "\e[32mJava installation successful!\e[0m"
    else
        echo "Java installation failed"
        exit 1
    fi

    # Do not need to install graalpy separately for GraalVM 21.0.3
    # -------------------------------------------------------------------------------
    # gu install python
    # if [ $? -eq 0 ]; then
    #     echo -e "\e[32mPython component for GraalVM installed successfully!\e[0m"
    # else
    #     echo "Python component for GraalVM failed to install"
    #     exit 1
    # fi
    # -------------------------------------------------------------------------------
}

if [ "$1" == "setup_env" ]; then
    setup_env;
elif [ "$1" == "install_requirements" ]; then
    install_requirements;
elif [ "$1" == "download_java_projects" ]; then
    download_java_projects;
elif [ "$1" == "build_java_projects" ]; then
    build_java_projects;
elif [ "$1" == "create_database_java" ]; then
    create_database_java;
elif [ "$1" == "install_graal" ]; then
    install_graal;
else
    echo "Invalid argument";
fi
