#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: ./merge_jar.sh <path_to_project>"
  exit 1
fi
PROJECT_DIR="$1"

if [ ! -d "$PROJECT_DIR" ]; then
  echo "Error: Directory '$PROJECT_DIR' does not exist."
  exit 1
fi

cd "$PROJECT_DIR" || exit 1

echo "Running 'mvn clean install' in $PROJECT_DIR..."
if ! mvn clean install -DskipTests -Drat.skip -Dgpg.skip; then
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

