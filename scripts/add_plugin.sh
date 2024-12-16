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
    echo "Usage: ./add_plugin.sh <directory_containing_pom.xml>"
    exit 1
fi

project_dir="$1"
if ! cd "$project_dir" 2>/dev/null; then
    echo "Error: Cannot access directory '$project_dir'."
    exit 1
fi

if [ ! -f "pom.xml" ]; then
    echo "Error: pom.xml not found in $project_dir."
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

echo "Plugin configuration added to pom.xml in $project_dir"

