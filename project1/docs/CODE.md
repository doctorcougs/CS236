# Provided Python Code

We provide a fair amount of python code for this project. Please take time to review, and be sure you understand, the code before starting to write code for the project.

## Files

  * `README.md`: overview and directions
  * `config_test.sh`: support for auto-grading -- **please do not edit**
  * `images`: folder for images referenced in `README.md` and `LEXER.md`
  * `pyproject.toml`: package definition and project configuration -- **please do not edit**
  * `src`: folder for the package source files
  * `tests`: folder for the package test files
  * `docs`: folder for different docs
  * Other misc. files for different tools (these you can ignore)

### Reminder

Please do not edit any of the following files or directories as they are related to _auto-grading_ and _pass-off_:

  * `config_test.sh`
  * `./tests/test_passoff_20.py`
  * `./tests/test_passoff_40.py`
  * `./tests/test_passoff_60.py`
  * `./tests/test_passoff_80.py`
  * `./tests/test_passoff_100.py`
  * `./tests/resources/project1-passoff/*`

## Python Overview

The project is divided into the following modules each representing a key component (see the Jupyter notebook tutorials for examples of using `token.py` and understanding `fsm.py` on [learningsuite.byu.edu](https://learningsuite.byu.edu) at _Content_ &rarr; _Project 1_ &rarr; _Project Description and Specification_ and _Content_ &rarr; _Lectures: Reading, Topics, Slides_ &rarr; _September Lectures_ &rarr; _FSMs in Project 1_):

  * `src/project1/token.py`: defines the `Token` class with methods to create tokens of each type needed for Datalog. You should read this code but you will not need to modify it. You can use an AI tool to help you understand what this code does.
  * `src/project1/fsm.py`: defines the `FiniteStateMachineClass` and how to run an instance of a `FiniteStateMachine`. You will add a FSM for each token in this file.
  * `src/project1/lexer.py`: defines the interface for the lexer. You will implement the lexer algorithm from [LEXER.md](./LEXER.md) in this file.
  * `src/project1/project1.py`: defines the entry point for auto-grading and the command line entry point. You will not need to modify this file.
  * `debug_project1.py`: defines the entry point for using the VS Code debugger. Change the entry `"arg1"` part of the entry `sys.argv = ["project1", "arg1"]` on the third line of the file to specify the input file to use when debugging. For example, if you want to step through your lexer for one of the integration tests in `tests/resources/80`, you would replace `"arg1"` with the path and name of the file.

Except for the debugging support, each of the above files are specified with Python _docstrings_ and they also have examples defined with python _doctests_. A _docstring_ is a way to document Python code so that the command `help(project1.lexer)` in the Python interpreter outputs information about the module with its functions and classes. For functions, the docstrings give documentation when the mouse hovers over the function in vscode.

```
$ python
Python 3.12.3 (main, Apr 24 2024, 14:45:49) [GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import project1.lexer
>>> help(project1.lexer)
```

The `help` function can be called on functions, classes, or modules. For example, you can type 
```bash
python3 -m pydoc src/project1/token.py
```
to print out the docstring for the `token.py` module. This project comes with a fair amount of code already provided. Take time to read the docstrings either in the vscode editor or the Python interpreter to be sure you understand what you need, and do not need, to implement.

Associated with each of the above files are corresponding test files. For example, `src/project1/token.py` has a corresponding `tests/test_token.py` file. These test files demonstrate the test driven development approach encourage by the course and will be referenced as each file is discussed.

#### Python Imports

Our Python files are all organized in a package, so any import must reference the package first. So in the above example for the `help` function, we have `import project1.lexer`. We could also do `from project1.lexer import lexer` as below:

```
$ python
Python 3.12.3 (main, Apr 24 2024, 14:45:49) [GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from project1.lexer import lexer
>>> help(lexer)
```

The above example will show a different docstring. The first example is the docstring for the module. This second example is the docstring for the function `lexer`. There are several examples of how to import things in the package throughout the provided code.

### token.py

The `Token` class is fully implemented for you. Take a moment now to look at the code, read the docstrings, and review how the Token class was used in the Jupyter notebook referenced the [Overview](#overview). New is the use of the algebraic sum type `TokenType` as well as the other uses of the `Literal` type. These make it so `mypy` is able to type check that only tokens of type `TokenType` can ever be created and that when creating fixed string tokens such as COLON the value associated with that token type matches what the token should be.

Be sure you understand the examples in the docstrings before moving on. These can be run in the Python interpreter in the terminal by recreating the commands.

The `test_token.py` file checks that `str(token)` works as expected for each token type.

### fsm.py

This file implements an FSM and how to run an FSM. A few FSMs and the `run_fsm` function are implemented for you. The implemented FSMs are meant to be examples of what you need to do for the other FSMs.

The `run_fsm` is what steps an FSM until it accepts or rejects.
This `run_fsm` function is similar to `run` function in the Jupyter notebook tutorial and is adapted to the revised `FiniteStateMachine` class. The details are in the docstring that you can read directly in the file or using the `help` function in the Python interpreter.

```
$ python
>>> from project1.fsm import run_fsm
>>> help(run_fsm)
```

**Please study this function until you understand what it is doing.** It is key to completing the project since it is used to run the FSMs that you need to create. Use the example in the docstring and the Python interpreter to help in understanding.

`FiniteStateMachine` is the Python equivalent of the FSMs that are being discussed in class. The details are in the docstring for the class. Use the `help` function (see below) are open and read the docstrings in the file directly.

```
$ python
Python 3.12.3 (main, Apr 24 2024, 14:45:49) [GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from project1.fsm import FiniteStateMachine
>>> help(FiniteStateMachine)
```

The are three FSMs already provided with the project with tests in `test_fsm.py` for each one: `Colon`, `Eof`, and `Whitespace`. These are complete, and may be used _as is_. They are also examples of how to create the other FSMs required for the projects. There are **two tests** for each FSM: one that should reject and one that should accept. You can find these tests in the `tests` directory in the file called `test_fsm.py`. **Follow this pattern of testing for the other FSMs that you must implement.**

### lexer.py

The `lexer.py` file includes pseudo-code with a few added details in the docstrings. **It is well worth your time to study and understand the provided pseudo-code in `lexer.py` before starting the project.**

```
$ python
>>> from project1.lexer import lexer
>>> help(lexer)
```

The `test_lexer.py` includes tests for the lexer that are suitable for the three FSMs that are provided. Review these tests because they are the starting point for the project. **Be sure you understand the tests before moving to the next section.**

### project1.py

The entry point for the auto-grader and the `project1` command. See the docstrings for details.
