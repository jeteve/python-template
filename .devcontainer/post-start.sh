#! /bin/bash

set -xe

source .venv/bin/activate

uv pip sync requirements.txt dev-requirements.txt
