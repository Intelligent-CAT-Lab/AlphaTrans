#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: ./merge_jar.sh <project_name>"
  exit 1
fi
PROJECT_NAME="$1"
PROJECT_DIR="./java_projects/automated_reduced_projects/$PROJECT_NAME"

if [ ! -d "$PROJECT_DIR" ]; then
  echo "Error: Directory '$PROJECT_DIR' does not exist."
  exit 1
fi

if [ "$PROJECT_NAME" == "commons-graph" ]; then
  TARGET_FILE="$PROJECT_DIR/src/main/java/org/apache/commons/graph/export/DefaultExportSelector.java"
  
  if [ ! -f "$TARGET_FILE" ]; then
    echo "Error: File '$TARGET_FILE' not found."
    exit 1
  fi
  
  awk 'NR==62 {$0="return null;"} {print}' "$TARGET_FILE" > "${TARGET_FILE}.tmp" && mv "${TARGET_FILE}.tmp" "$TARGET_FILE"
fi

if [ "$PROJECT_NAME" == "commons-pool" ]; then
  TARGET_FILE="$PROJECT_DIR/src/test/java/org/apache/commons/pool2/performance/PerformanceTest.java"
  
  if [ -f "$TARGET_FILE" ]; then
    rm -f "$TARGET_FILE"
  else
    echo "Error: File '$TARGET_FILE' not found."
    exit 1
  fi
fi

cd "$PROJECT_DIR" || exit 1

echo "Running 'mvn clean install' in $PROJECT_DIR..."
if ! mvn clean install -DskipTests -Drat.skip -Dgpg.skip -Dcheckstyle.skip; then
  echo "Error: Maven build failed."
  exit 1
fi

TARGET_DIR="target"

MAIN_JAR=$(find "$TARGET_DIR" -type f -name "*[^-tests].jar" | grep -v "merged" | head -n 1)
TEST_JAR=$(find "$TARGET_DIR" -type f -name "*-tests.jar" | head -n 1)

MERGED_JAR="$TARGET_DIR/$(basename "$MAIN_JAR" .jar)-merged.jar"

if [ -z "$MAIN_JAR" ]; then
  echo "Error: Main JAR file not found in $TARGET_DIR."
  exit 1
fi

if [ -z "$TEST_JAR" ]; then
  echo "Error: Test JAR file not found in $TARGET_DIR."
  exit 1
fi

TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

echo "Extracting $MAIN_JAR..."
unzip -q "$MAIN_JAR" -d "$TEMP_DIR"

echo "Extracting $TEST_JAR..."
unzip -q -o "$TEST_JAR" -d "$TEMP_DIR"

echo "Creating merged JAR at $MERGED_JAR..."
jar cf "$MERGED_JAR" -C "$TEMP_DIR" .

echo "Merged JAR created successfully at $MERGED_JAR."

