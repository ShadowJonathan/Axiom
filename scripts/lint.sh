#!/bin/bash
# parts shamelessly stolen from synapse/scripts-dev/lint.sh :P

files=("axiom" "setup.py")

files+=("$@")

echo "Linting these paths: ${files[*]}"

# Print out the commands being run
set -x

isort "${files[@]}"
black "${files[@]}"
flake8 "${files[@]}"
mypy