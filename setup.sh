
function setup_env() {
    conda create -n alphatrans python=3.9.12;       # miniconda 23.5.2 download from https://docs.conda.io/en/latest/miniconda_hashes.html
    conda activate alphatrans;
    conda install maven-3.9.4-hce30654_0.conda;     # download from https://anaconda.org/conda-forge/maven/files
    conda install openjdk-17.0.3-hbe7ddab_8.conda;  # download from https://anaconda.org/conda-forge/openjdk/files
}

function install_requirements() {
    pip3 install tqdm==4.66.1;
    pip3 install graphviz==0.20.1;
    pip3 install python-dotenv==1.0.0;
    pip3 install openai==0.27.8;
    pip3 install tiktoken==0.3.2;
    pip3 install python-dotenv==1.0.0;
    pip3 install accelerate==0.24.1;
}

function download_java_projects() {
    mkdir -p java_projects;
    main=`pwd`;

    git clone https://github.com/apache/commons-fileupload.git java_projects/commons-fileupload;
    cd java_projects/commons-fileupload;
    git reset --hard commons-fileupload-1.5;
    cd $main;

    git clone https://github.com/apache/commons-validator.git java_projects/commons-validator;
    cd java_projects/commons-validator;
    git reset --hard VALIDATOR_1_7;
    cd $main;

    git clone https://github.com/apache/commons-codec.git java_projects/commons-codec;
    cd java_projects/commons-codec;
    git reset --hard commons-codec-1.16-rc1;
    cd $main;

    git clone https://github.com/apache/commons-pool.git java_projects/commons-pool;
    cd java_projects/commons-pool;
    git reset --hard rel/commons-pool-2.11.1;
    cd $main;

    git clone https://github.com/apache/commons-cli.git java_projects/commons-cli;
    cd java_projects/commons-cli;
    git reset --hard commons-cli-1.5.0;
    cd $main;

    git clone https://github.com/apache/commons-csv.git java_projects/commons-csv;
    cd java_projects/commons-csv;
    git reset --hard rel/commons-csv-1.10.0;
    cd $main;

    git clone https://github.com/apache/commons-graph.git java_projects/commons-graph;
    cd java_projects/commons-graph;
    git reset --hard 93d2ba7;
    cd $main;

    git clone https://github.com/JodaOrg/joda-money.git java_projects/joda-money;
    cd java_projects/joda-money;
    git reset --hard v1.0.4;
    cd $main;

    git clone https://github.com/JodaOrg/joda-convert.git java_projects/joda-convert;
    cd java_projects/joda-convert;
    git reset --hard v2.2.3;
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
    projects_dir=java_projects;

    cd $projects_dir/commons-fileupload;
    codeql database create ../../databases/commons-fileupload --language=java --overwrite;
    cd $main;

    cd $projects_dir/commons-validator;
    codeql database create ../../databases/commons-validator --language=java --overwrite;
    cd $main;

    cd $projects_dir/commons-codec;
    codeql database create ../../databases/commons-codec --language=java --overwrite;
    cd $main;

    cd $projects_dir/commons-pool;
    codeql database create ../../databases/commons-pool --language=java --overwrite;
    cd $main;

    cd $projects_dir/commons-cli;
    codeql database create ../../databases/commons-cli --language=java --overwrite;
    cd $main;

    cd $projects_dir/commons-csv;
    codeql database create ../../databases/commons-csv --language=java --overwrite;
    cd $main;

    cd $projects_dir/commons-graph;
    codeql database create ../../databases/commons-graph --language=java --overwrite;
    cd $main;

    cd $projects_dir/joda-money;
    codeql database create ../../databases/joda-money --language=java --overwrite;
    cd $main;

    cd $projects_dir/joda-convert;
    codeql database create ../../databases/joda-convert --language=java --overwrite;
    cd $main;
}

# setup_env;
# install_requirements;
# download_java_projects;
# build_java_projects;
# create_database_java;
