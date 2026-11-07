# Overview

The project is divided into the following modules each representing a key component of the project:

  * `src/project4/interpreter.py`: defines the `Interpreter` class with its interface.
  * `src/project4/project4.py`: defines the entry point for auto-grading and the command line entry point.
  * `src/project4/relation.py`: defines the `Relation` class with its interface.
  * `src/project4/reporter.py`: defines functions for reporting the results of the interpreter.

Each of the above files are specified with Python _docstrings_ and they also have examples defined with python _doctests_. A _docstring_ is a way to document Python code so that the command `help(project4.relation)` in the Python interpreter outputs information about the module with it's functions and classes. For functions, the docstrings give documentation when the mouse hovers over the function in vscode.

## interpreter.py

The portion of the `Interpreter` class that needs to be implemented for Project 4 is `eval_rules`. The docstring describe what
it should do. There are no provided tests. You are expected to write tests for the function before starting any implementation. There should a few tests that cover interesting inputs for rule evaluation. Justify why the set of tests are sufficient to give confidence in the implementation.

## project4.py

The entry point for the auto-grader and the `project4` command. See the docstrings for details.

## relation.py

The only part of the `Relation` class that needs to be implemented for Project 4 is `join` (hard). The docstring describe what the function should do. **You are expected to write at least three positive tests for `join`: one for when there are no shared attributes, one for when all the attributes are shared, and one from when the is a mix of each.**

The `Relation.union` relational operator must be used for Project 4. Whether you implemented union in Project 3 or will implement it in Project 4, you should include unit tests for this operation.

## reporter.py

A module for output matching in the pass-off tests. It takes the interface defined by `Interpreter` and converts the return types to strings that are used for the actual query reports that must output match for pass-off. _This module should work out of the box and not need to be touched_.
