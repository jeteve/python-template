#! /bin/bash
set -xe

# Uses pip-tools:
# https://github.com/jazzband/pip-tools
#
# To drive the requirements.txt files from the toml file.
pip-compile --resolver=backtracking -o requirements.txt pyproject.toml
pip-compile --resolver=backtracking --extra dev -o dev-requirements.txt pyproject.toml

pip-sync requirements.txt dev-requirements.txt
