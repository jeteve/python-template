#! /bin/bash
set -xe

uv venv
source .venv/bin/activate

uv pip sync requirements.txt dev-requirements.txt
