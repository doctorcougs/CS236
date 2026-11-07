Here are the relevant files for the project:

  * `.devcontainer`: container definition for those using docker with vscode (this doesn't apply to most of you)
  * `.github`: workflow definitions
  * `README.md`: overview and directions
  * `config_test.sh`: support for auto-grading -- **please do not edit**
  * `pyproject.toml`: package definition and project configuration -- **please do not edit**
  * `pytest.ini`: custom pytest marks for pass-off -- **please do not edit**
  * `src`: folder for the package source files
  * `tests`: folder for the package test files
  * `.gitignore`: files patterns that git should ignore
  * `debug_project3.py`: file that allows you to run the interpreter on an input of your choosing so that you can use the VS Code debugger

## Reminder

Please do not edit any of the following files or directories as they are related to _auto-grading_ and _pass-off_:

  * `config_test.sh`
  * `pytest.ini`
  * `./tests/test_passoff.py`
  * `./tests/resources/project3-passoff/*`

## Overview

The project is divided into the following modules each representing a key component of the project:

  * `src/project3/interpreter.py`: defines the `Interpreter` class with its interface.
  * `src/project3/project3.py`: defines the entry point for auto-grading and the command line entry point.
  * `src/project3/relation.py`: defines the `Relation` class with its interface.
  * `src/project3/reporter.py`: defines functions for reporting the results of the interpreter.

Each of the above files are specified with Python _docstrings_ and they also have examples defined with python _doctests_. A _docstring_ is a way to document Python code so that the command `help(project3.relation)` in the Python interpreter outputs information about the module with it's functions and classes. For functions, the docstrings give documentation when the mouse hovers over the function in vscode.

### interpreter.py

A portion of the `Interpreter` class needs to be implemented for project 3: `eval_schemes`, `eval_facts`, and `eval_queries`. The docstrings describe what
each should do. Relational algebra must be used for `eval_queries`. There are no provided tests. You are expected to write tests for each function before starting any implementation. Be sure to add to the repository the file with the tests.

### project3.py

The entry point for the auto-grader and the `project3` command. See the docstrings for details.

### relation.py

Some of the `Relation` class is already implemented. The attributes are complete as is the interface. A portion of the `Relation` class needs to be implemented for project 3:
  - `intersection` (easy),
  - `project` (hard),
  - `rename` (super easy),
  - `reorder` (hard),
  - `select_eq_col` (moderate),
  - `select_eq_lit` (moderate), and
  - `union` (easy).
**You do not need natural join for project 3**.

The docstrings describe what each function should do. There are tests in `./tests/test_relation.py` for the provided portions of the class that are implemented already. It is wise to write negative and positive tests for each function before starting any implementation. A negative test is one where an error is expected (e.g., bad operands to an operation). Follow the examples provided in the test file.

### reporter.py

A module for output matching in the pass-off tests. It takes the interface defined by `Interpreter` and converts the return types to strings that are used for the actual query reports that must output match for pass-off. _This module should work out of the box and not need to be touched_.
