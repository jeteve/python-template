# Template for a vanilla python 3 project

# Structure

This package's structure follows the guidance from Pypi: https://packaging.python.org/en/latest/tutorials/packaging-projects/

# Dependency managements

This uses https://github.com/jazzband/pip-tools to pin the dependencies specified from
```pyproject.toml``` into requirements.txt and dev-requirements.txt

This can be achieved just by running:
```
./sync-python-deps.sh
```

# Building the package for distribution:

```
python3 -m pip install --upgrade build
python3 -m build
```
