Here are the relevant files and folders for Project2

  * `README.md`: overview and directions
  * `.pre-commit-config.yaml`: hook definitions for `pre-commit`
  * `config_test.sh`: support for auto-grading -- **please do not edit**
  * `pyproject.toml`: package definition and project configuration -- **please do not edit**
  * `docs`: documentation
  * `src`: folder for the package source files
  * `tests`: folder for the package test files
  * `debug_project2.py`: file that allows you to use the VS Code debugger on an input file of your choosing

## Reminder on Setup

**Copy** the below files from your solution to Project 1 into the `src/project2/` folder:

  * `fsm.py`
  * `lexer.py`

**Do not copy** the following files:
  * `token.py` since it is unchanged from what was given to you inProject 1.
  * any of the test files from Project 1

**Ignoring comments.** Comments are not used to generate the `DatalogProgram` in Project 2, so you will modify `lexer.py` to ignore comments. Edit `lexer.py` and add `COMMENT` to the list of `hidden` tokens. So `WHITESPACE` and `COMMENT` should both be hidden and not passed to the parser.

## Please do not Edit

Please do not edit any of the following files or directories as they are related to _auto-grading_ and _pass-off_:

  * `.vscode/settings.json`
  * `.pre-commit-config.yaml`
  * `config_test.sh`
  * `./tests/passoff_utils.py`
  * `./tests/test_passoff_80.py`
  * `./tests/test_passoff_100.py`
  * `./tests/resources/project2-passoff/*`

## Overview

The project is divided into the following modules each representing a key component of the project:

  * `src/project2/datalogprogram.py`: defines the `Parameter`, `Predicate`, `Rule`, and `DatalogProgram` classes.
  * `src/project2/parser.py`: defines `UnexpectedTokenException`, `TokenStream`, and the `parse` function entry point used by `project2.py`.
  * `src/project2/project2.py`: defines the entry point for auto-grading and the command line entry point.
  *  `debug_project2.py`: used if you use the VS Code debugger. You will change `"arg1"` to specify the file input you want to use.

Each of the above files (except `debug_project2.py`) are specified with Python _docstrings_ and they also have examples defined with python _doctests_. A _docstring_ is a way to document Python code so that the command `help(project2.parser)` in the Python interpreter outputs information about the module with it's functions and classes. For functions, the docstrings give documentation when the mouse hovers over the function in vscode.

### datalogprogram.py

The `parser.parse` function needs to build, and return, an instance of a `DatalogProgram`. The components of a `DatalogProgram` are defined in the `datalogprogram.py` module. An instance of a `DatalogProgram` is a collection of lists, and each list is built using the definition of a `Predicate` in the `datalogprogram.py` module. A predicate has a `name` and a list of `Parameter` objects. A `Parameter` is a `STRING` type or an `ID` type. Both types have a `value` attribute that is taken from the token when the `Parameter` is created, so it's either the value from the `ID` token or the value from the `STRING` token.

A `DatalogProgram` consists of `schemes`, `facts`, `rules`, and `queries`. The `schemes`, `facts`, and `queries` are of `List[Predicate]` type. The predicates in `schemes` can only have `ID` types for parameters. The predicates in `facts` can only have `STRING` types for parameters. The predicates `queries` can have `ID` or `STRING` parameter types.

The `rules` in the `DatalogProgram` are not simple lists of predicates. Rather, the `rules` are a list of  of a _head_ predicate with a list of predicates. The head predicate only has `ID` parameter types while the predicates in the list can have either `ID` or `STRING` in the parameters. These attributes are accessed directly as in `rule.head` and `rule.predicates` where `rule` is an instance of the `Rule` class.

The `Parameter` and `Predicate` classes both have an implementation of the `__str__` function for pretty printing. The implementation `DatalogProgram.__str__` is **not given and must be implemented by you.** There are tests in `./tests/test_datalogprogram.py` to test the `DatalogProgram.__str__` function. The tests should pass when the function is implemented correctly. There are also `__repr__` functions defined for the classes. These make debugging easier. As your favorite LLM, _"What are the __repr__ functions for in Python?"_

### parser.py

The bulk of the coding for the project is in the `src/project2/parser.py` module. See the project description in [PARSER.md](PARSER.md), lecture notes in [learningsuite.byu.edu](https://learningsuite.byu.edu) in the _Content_ section in both _Lectures_ and _Projects_, and the Jupyter notebook tutorials in the `docs` folder.

The `src/project2/parser.py` module provides three things out of the box:

1. A `TokenStream` class that is able to  `match` and `advance` the token iterator from the lexer. It raises an `UnexpectedTokenException` when `TokenStream.match` fails. These are fully implemented and should be used by your parser.
1. The unimplemented top-level function for the recursive decent parser: `datalog_program`. The name of this function corresponds to the `datalogProgram` rule in the Datalog grammar in [PARSER.md](PARSER.md). You will need to implement a function for each production in tho grammar.
1. The `parse` function that creates the `TokenStream` object and calls `datalog_program` with that object.

Understanding the `TokenStream` class is important. Recall that the lexer from Project 1 returns an iterator over tokens as `token_iterator: Iterator[Token] = lexer(input_string)` -- see the `project2` function in `src/project2/project2.py`. The `TokenStream` wraps this iterator,`token: TokenStream = TokenStream(token_iterator)`, and adds functionality specific to parsing. This _wrap_ happens in the `parse` function in `src/project2/parser.py` before calling `datalog_program` to start the parsing.

**IMPORTANT**: the `token` argument in the `datalog_program` function that implements the `datalogProgram` grammar rule is an instance of `TokenStream`. It's not a `Token` instance but a `TokenStream` instance. So what can you do with the `token` instance of a `TokenStream`:

1. `match(self, expected_type: TokenType) -> None`: raises `UnexpectedTokenException` if the current actual `Token` in the stream does not have type `expected_type`. For example, if the current token in the stream is `(QUERIES,"Queries",2)` and you call `token.match(TokenType,QMARK)`, then an `UnexpectedTokenException` is raised containing the `(QUERIES,"Queries",2)` token. Whereas if you call `token.match(TokenType,QUERIES)` then it just returns doing nothing. In this way you can implement the grammar productions to check if the current token in the `TokenStream` matches an expected `TokenType`.
1. `advance(self) -> None`: move to the next token in the stream. Once you match a token, then you can move to the next token with `advance`. It does nothing else.
1. `member_of(self, token_types: set[TokenType]) -> bool`: check to see if the `TokenType` of the current token in the stream is found in `token_types`. Excellent for checking if a token type is found in a `FIRST` or `FOLLOW` set.
1. `value(self) -> str`: returns the string associated with the current token. Recall the every token has three attributes: `token_type`, `value`, and `line_num`. This function gives the `value` attribute from the current token in the stream and is useful for creating instances of `Parameter`, `Predicate`, etc.

_You are strongly encouraged to read the docstrings in `src/project2/parser.py` for more details on the `TokenStream` class and how it should be used._

### project2.py

The entry point for the auto-grader and the `project2` command. See the docstrings for details.
