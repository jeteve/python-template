# Template for a vanilla python 3 project

# Structure

This package's structure follows the guidance from Pypi: https://packaging.python.org/en/latest/tutorials/packaging-projects/

# Getting started

If you use the included `.devcontainer`, this will create the python venv using `uv` for you, using the latest python stable version.

If you don't use devcontainers, look in the `post-create.sh` and `post-start.sh` scripts in `.devcontainer`.

# Dependency managements

This uses UV ( https://docs.astral.sh/uv/ ) to pin the dependencies specified from
```pyproject.toml``` into a uv lock file.

This can be achieved just by running:
```sh
# Activate the environment 
$ source .venv/bin/activate
# And sync the dependencies
$ ./sync-python-deps.sh
```

## Upgrading one dependency (even transitive)

```sh
uv lock --upgrade-package <package>
```

# View the logs and the prints running test.


```sh
 pytest -o log_cli=true -o log_cli_level=DEBUG -s
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
