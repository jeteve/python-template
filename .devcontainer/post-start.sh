#! /bin/bash

set -xe

source .venv/bin/activate

uv sync --extra dev
