#!/bin/bash

plugin_config=$(cat <<'EOF'
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-jar-plugin</artifactId>
        <version>3.2.0</version>
        <configuration>
            <excludes>
                <exclude>module-info.class</exclude>
            </excludes>
        </configuration>
        <executions>
            <execution>
                <goals>
                    <goal>test-jar</goal>
                </goals>
            </execution>
        </executions>
    </plugin>
EOF
)

if [ $# -ne 1 ]; then
    echo "Usage: ./add_plugin.sh <project_name>"
    exit 1
fi

project_name="$1"
original_dir="./java_projects/original_projects/$project_name"
reduced_dir="./java_projects/automated_reduced_projects/$project_name"

if [ ! -d "$original_dir" ]; then
    echo "Error: Project '$project_name' not found in /java_projects/original_projects/"
    exit 1
fi

cp -r "$original_dir" "$reduced_dir"
if [ $? -ne 0 ]; then
    echo "Error: Failed to copy project '$project_name' to $reduced_dir."
    exit 1
fi

cd "$reduced_dir" || exit

if [ ! -f "pom.xml" ]; then
    echo "Error: pom.xml not found in $reduced_dir."
    exit 1
fi

insertion_point="<plugins>"

OS=$(uname)

if [ "$OS" = "Linux" ]; then
    sed -i "/$insertion_point/a\\
$plugin_config" pom.xml
elif [ "$OS" = "Darwin" ]; then
    sed "/$insertion_point/ r /dev/stdin" pom.xml > pom.xml.new <<EOF
$plugin_config
EOF
    mv pom.xml.new pom.xml
else
    echo "Unsupported OS: $OS"
    exit 1
fi

echo "Plugin configuration added to pom.xml in $reduced_dir"

