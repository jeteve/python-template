#! /bin/bash
set -xe

uv venv
source .venv/bin/activate

echo "#For venv" >> ~/.bashrc
echo "source .venv/bin/activate" >> ~/.bashrc
