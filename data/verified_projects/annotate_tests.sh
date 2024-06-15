#!/bin/bash

# Find all .py files excluding __init__.py
find . -type f -name "*.py" ! -name "__init__.py" | while read file; do
  # Add `import pytest` at the top if not already present
  if ! grep -q "^import pytest" "$file"; then
    sed -i '' '1s/^/import pytest\n\n/' "$file"
  fi

  # Annotate test methods with @pytest.mark.test
  awk '
  /^[ \t]*def test/ {
    indent = substr($0, 1, match($0, /[^ \t]/)-1)
    if (prev !~ /^@[ \t]*pytest\.mark\.test/) {
      print indent "@pytest.mark.test"
    }
  }
  {
    print
    prev = $0
  }
  ' "$file" > tmpfile && mv tmpfile "$file"
done
