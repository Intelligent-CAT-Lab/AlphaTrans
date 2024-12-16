#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: ./generate_cg.sh <path_to_project>"
  exit 1
fi

SCRIPT_DIR=$(dirname "$(realpath "$0")")

PROJECT_DIR="$1"

if [ ! -d "$PROJECT_DIR" ]; then
  echo "Error: Directory '$PROJECT_DIR' does not exist."
  exit 1
fi

cd "$PROJECT_DIR" || exit 1

TARGET_DIR="target"

MAIN_JAR=$(find "$TARGET_DIR" -type f -name "*[^-tests].jar" | grep -v "merged" | head -n 1)

MERGED_JAR="$TARGET_DIR/$(basename "$MAIN_JAR" .jar)-merged.jar"

JAVACG_PATH="$SCRIPT_DIR/javacg-0.1-SNAPSHOT-static.jar"

if [ ! -f "$JAVACG_PATH" ]; then
  echo "Error: javacg-0.1-SNAPSHOT-static.jar not found at $JAVACG_PATH."
  exit 1
fi

echo "Generating call graph for $MERGED_JAR..."
java -jar "$JAVACG_PATH" "$MERGED_JAR" > callgraph.txt

echo "Call graph saved to callgraph.txt."

