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

mkdir -p "$reduced_dir"
rsync -a --exclude='.git' "$original_dir/" "$reduced_dir"
if [ $? -ne 0 ]; then
    echo "Error: Failed to copy project '$project_name' to $reduced_dir."
    exit 1
fi

cd "$reduced_dir" || exit

if [ ! -f "pom.xml" ]; then
    echo "Error: pom.xml not found in $reduced_dir."
    exit 1
fi

awk -v config="$plugin_config" '
    BEGIN { in_build = 0 }
    /<build>/ { in_build = 1 }
    /<\/build>/ { in_build = 0 }
    in_build && /<plugins>/ {
        print; 
        print config; 
        next 
    }
    { print }
' pom.xml > pom.xml.new && mv pom.xml.new pom.xml

echo "Plugin configuration added to pom.xml in $reduced_dir"
