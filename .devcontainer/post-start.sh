#! /bin/bash
set -xe

echo "Upgrading pip"
python -m pip install --upgrade pip
echo "Installing pip-tools"
python -m pip install pip-tools

echo "Synchronizing requirements"
./sync-python-deps.sh


