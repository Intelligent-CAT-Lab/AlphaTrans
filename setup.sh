
function download_java_projects() {

    repos=(
        "https://github.com/apache/commons-cli.git commons-cli commons-cli-1.5.0"
        "https://github.com/apache/commons-codec.git commons-codec commons-codec-1.16-rc1"
        "https://github.com/apache/commons-csv.git commons-csv rel/commons-csv-1.10.0"
        "https://github.com/apache/commons-exec.git commons-exec rel/commons-exec-1.4.0"
        "https://github.com/lemire/JavaFastPFOR.git JavaFastPFOR 0ecdda9"
        "https://github.com/apache/commons-fileupload.git commons-fileupload commons-fileupload-1.5"
        "https://github.com/apache/commons-graph.git commons-graph 93d2ba7"
        "https://github.com/fusesource/jansi.git jansi 045fd56"
        "https://github.com/apache/commons-pool.git commons-pool rel/commons-pool-2.11.1"
        "https://github.com/apache/commons-validator.git commons-validator VALIDATOR_1_7"
    )

    mkdir -p java_projects/original_projects;
    main=$(pwd);

    for repo in "${repos[@]}"; do
        IFS=' ' read -r url project commit <<< "$repo"
        git clone "$url" "java_projects/original_projects/$project"
        cd "java_projects/original_projects/$project" || exit
        git reset --hard "$commit"        
        cd "$main" || exit
    done
}

function build_java_projects() {

    projects=(
        "commons-cli"
        "commons-codec"
        "commons-csv"
        "commons-exec"
        "JavaFastPFOR"
        "commons-fileupload"
        "commons-graph"
        "jansi"
        "commons-pool"
        "commons-validator"
    )

    projects_dir=java_projects/original_projects;
    main=$(pwd);

    for project in "${projects[@]}"; do
        echo "building $project"
        cd "$projects_dir/$project" || exit
        mvn clean test --log-file build.log
        cd "$main" || exit
    done
}

function create_database_java() {

    projects=(
        "commons-cli"
        "commons-codec"
        "commons-csv"
        "commons-exec"
        "JavaFastPFOR"
        "commons-fileupload"
        "commons-graph"
        "jansi"
        "commons-pool"
        "commons-validator"
    )

    mkdir -p databases;
    main=$(pwd);

    suffix=_decomposed_tests;
    projects_dir=java_projects/cleaned_final_projects${suffix};

    for project in "${projects[@]}"; do
        echo "creating database $project"
        cd "$projects_dir/$project" || exit
        codeql database create ../../../databases/${project}${suffix} --language=java --overwrite;
        cd "$main" || exit
    done
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
}

if [ "$1" == "download_java_projects" ]; then
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
