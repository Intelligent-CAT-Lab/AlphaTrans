
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

    git clone https://github.com/apache/commons-collections.git java_projects/commons-collections;
    cd java_projects/commons-collections;
    git reset --hard commons-commons-collections-4.4;
    cd $main;

    git clone https://github.com/apache/commons-io.git java_projects/commons-io;
    cd java_projects/commons-io;
    git reset --hard rel/commons-io-2.13.0;
    cd $main;

    git clone https://github.com/apache/commons-fileupload.git java_projects/commons-fileupload;
    cd java_projects/commons-fileupload;
    git reset --hard commons-fileupload-1.5;
    cd $main;

    git clone https://github.com/apache/commons-lang.git java_projects/commons-lang;
    cd java_projects/commons-lang;
    git reset --hard rel/commons-lang-3.12.0;
    cd $main;

    git clone https://github.com/apache/commons-beanutils.git java_projects/commons-beanutils;
    cd java_projects/commons-beanutils;
    git reset --hard commons-beanutils-1.9.4;
    cd $main;

    git clone https://github.com/apache/commons-validator.git java_projects/commons-validator;
    cd java_projects/commons-validator;
    git reset --hard VALIDATOR_1_7;
    cd $main;

    git clone https://github.com/apache/commons-text.git java_projects/commons-text;
    cd java_projects/commons-text;
    git reset --hard rel/commons-text-1.10.0;
    cd $main;

    git clone https://github.com/apache/commons-bcel.git java_projects/commons-bcel;
    cd java_projects/commons-bcel;
    git reset --hard rel/commons-bcel-6.7.0;
    cd $main;

    git clone https://github.com/apache/commons-imaging.git java_projects/commons-imaging;
    cd java_projects/commons-imaging;
    git reset --hard rel/commons-imaging-1.0-alpha3;
    cd $main;

    git clone https://github.com/apache/commons-daemon.git java_projects/commons-daemon;
    cd java_projects/commons-daemon;
    git reset --hard commons-daemon-1.3.4;
    cd $main;

    git clone https://github.com/apache/commons-codec.git java_projects/commons-codec;
    cd java_projects/commons-codec;
    git reset --hard commons-codec-1.16-rc1;
    cd $main;

    git clone https://github.com/apache/commons-pool.git java_projects/commons-pool;
    cd java_projects/commons-pool;
    git reset --hard rel/commons-pool-2.11.1;
    cd $main;

    git clone https://github.com/apache/commons-net.git java_projects/commons-net;
    cd java_projects/commons-net;
    git reset --hard rel/commons-net-3.9.0;
    cd $main;

    git clone https://github.com/apache/commons-cli.git java_projects/commons-cli;
    cd java_projects/commons-cli;
    git reset --hard commons-cli-1.5.0;
    cd $main;

    git clone https://github.com/apache/commons-csv.git java_projects/commons-csv;
    cd java_projects/commons-csv;
    git reset --hard rel/commons-csv-1.10.0;
    cd $main;

    git clone https://github.com/apache/commons-geometry.git java_projects/commons-geometry;
    cd java_projects/commons-geometry;
    git reset --hard rel/commons-geometry-1.0;
    cd $main;

    git clone https://github.com/apache/commons-dbcp.git java_projects/commons-dbcp;
    cd java_projects/commons-dbcp;
    git reset --hard rel/commons-dbcp-2.9.0;
    cd $main;

    git clone https://github.com/apache/commons-rng.git java_projects/commons-rng;
    cd java_projects/commons-rng;
    git reset --hard rel/commons-rng-1.5;
    cd $main;

    git clone https://github.com/apache/commons-jexl.git java_projects/commons-jexl;
    cd java_projects/commons-jexl;
    git reset --hard rel/commons-jexl-3.3;
    cd $main;

    git clone https://github.com/apache/commons-dbutils.git java_projects/commons-dbutils;
    cd java_projects/commons-dbutils;
    git reset --hard commons-dbutils-1.8-RC2;
    cd $main;
}

function build_java_projects() {
    main=`pwd`;

    cd java_projects/commons-collections;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-io;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-fileupload;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-lang;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-beanutils;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-validator;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-text;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-bcel;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-imaging;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-daemon;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-codec;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-pool;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-net;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-cli;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-csv;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-geometry;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-dbcp;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-rng;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-jexl;
    mvn clean test --log-file build.log;
    cd $main;

    cd java_projects/commons-dbutils;
    mvn clean test --log-file build.log;
    cd $main;
}

function create_database_java() {
    mkdir -p databases;
    main=`pwd`;

    cd java_projects/commons-collections;
    codeql database create ../../databases/commons-collections --language=java;
    cd $main;

    cd java_projects/commons-io;
    codeql database create ../../databases/commons-io --language=java;
    cd $main;

    cd java_projects/commons-fileupload;
    codeql database create ../../databases/commons-fileupload --language=java;
    cd $main;

    cd java_projects/commons-lang;
    codeql database create ../../databases/commons-lang --language=java;
    cd $main;

    cd java_projects/commons-beanutils;
    codeql database create ../../databases/commons-beanutils --language=java;
    cd $main;

    cd java_projects/commons-validator;
    codeql database create ../../databases/commons-validator --language=java;
    cd $main;

    cd java_projects/commons-text;
    codeql database create ../../databases/commons-text --language=java;
    cd $main;

    cd java_projects/commons-bcel;
    codeql database create ../../databases/commons-bcel --language=java;
    cd $main;

    cd java_projects/commons-imaging;
    codeql database create ../../databases/commons-imaging --language=java;
    cd $main;

    cd java_projects/commons-daemon;
    codeql database create ../../databases/commons-daemon --language=java;
    cd $main;

    cd java_projects/commons-codec;
    codeql database create ../../databases/commons-codec --language=java;
    cd $main;

    cd java_projects/commons-pool;
    codeql database create ../../databases/commons-pool --language=java;
    cd $main;

    cd java_projects/commons-net;
    codeql database create ../../databases/commons-net --language=java;
    cd $main;

    cd java_projects/commons-cli;
    codeql database create ../../databases/commons-cli --language=java;
    cd $main;

    cd java_projects/commons-csv;
    codeql database create ../../databases/commons-csv --language=java;
    cd $main;

    cd java_projects/commons-geometry;
    codeql database create ../../databases/commons-geometry --language=java;
    cd $main;

    cd java_projects/commons-dbcp;
    codeql database create ../../databases/commons-dbcp --language=java;
    cd $main;

    cd java_projects/commons-rng;
    codeql database create ../../databases/commons-rng --language=java;
    cd $main;

    cd java_projects/commons-jexl;
    codeql database create ../../databases/commons-jexl --language=java;
    cd $main;

    cd java_projects/commons-dbutils;
    codeql database create ../../databases/commons-dbutils --language=java;
    cd $main;
}

# setup_env;
# install_requirements;
# download_java_projects;
# build_java_projects;
# create_database_java;
