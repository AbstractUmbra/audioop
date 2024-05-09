# audioop

An LTS port of the Python builtin module `audioop` which was deprecated since version 3.11 and removed in 3.13.

This project exists to maintain this module for future versions.

## Using this project

As this only becomes mandatory at Python versions of 3.13 or greater, you can conditionally add this project to your dependencies:

### pip-requirements
```
audioop-lts; python_version>='3.13'
```

### Poetry-pyproject
```toml
[tool.poetry.dependencies]
audioop-lts = { version = "...", python = "^3.13" }
```
Relevant documtation is [here](https://python-poetry.org/docs/dependency-specification/#python-restricted-dependencies), or alternatively use [`markers`](https://python-poetry.org/docs/dependency-specification/#using-environment-markers)

### Pipenv-pipfile
```toml
[packages]
audioop-lts = { version = "...", markers = "python_version >= 3.13" }
```

### Hatch-pyproject
```toml
[project]
dependencies = [
    "audioop-lts; python_version >= '3.13'"
    # or
    "audioop-lts==...; python_version >= '3.13'"
]
