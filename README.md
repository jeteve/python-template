# Template for a vanilla python 3 project

# Structure

This package's structure follows the guidance from Pypi: https://packaging.python.org/en/latest/tutorials/packaging-projects/

# Dependency managements

This uses UV ( https://docs.astral.sh/uv/ ) to pin the dependencies specified from
```pyproject.toml``` into requirements.txt and dev-requirements.txt

This can be achieved just by running:
```sh
# Activate the environment 
$ source .venv/bin/activate
# And sync the dependencies
$ ./sync-python-deps.sh
```

# Developing the CLI:

python src/jeteve_template/cli.py

# Building the package for distribution:

```sh
uv pip install --upgrade build
python3 -m build
```

And test the installation of the distribution:

```sh
uv pip install dist/jeteve_template-0.0.1-py3-none-any.whl
```

Note - when you install this package, the command it installs will be `jeteve_template_cli` executable as illustrated below:

```sh
jeteve_template_cli 
Hello world from jeteve_template CLI!
```
