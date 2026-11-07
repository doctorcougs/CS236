"""Function to call the parser for Datalog.

These are the two project level entry points: `project2` and `project2cli`.
All the pass-off tests use `project2`. This file should not need to be modified.
"""

from sys import argv
from typing import Iterator

from project2.datalogprogram import DatalogProgram
from project2.lexer import lexer
from project2.parser import UnexpectedTokenException, parse
from project2.token import Token


def project2(input_string: str) -> str:
    """Return the parse of the input as a string.

    Invokes the Datalog parser on the input string and either returns an
    string for the `DatalogProgram` or fails reporting the unexpected
    token in the parse.

    Args:
        input_string (str): The string to parse.

    Returns:
        out (str): The string representation of the `DatalogProgram` or unexpected token from the parse.
    """
    token_iterator: Iterator[Token] = lexer(input_string)
    try:
        datalog_program: DatalogProgram = parse(token_iterator)
        return "Success!\n" + str(datalog_program)
    except UnexpectedTokenException as e:
        return "Failure!\n  " + str(e.token)


def project2cli() -> None:
    """Build the DatalogProgram from the contents of a file.

    `project2cli` is only called from the command line in the integrated terminal.
    Prints the `DatalogProgram` resulting from the contents of the named file.

    Args:
        argv (list[str]): Generated from the command line and needs to name the input file.

    Examples:

    ```
    $ cat prog.txt
    Schemes:
      student(N, I, A, M)
    WhoMajor(N,M)
      Facts:
    student('Roosevelt', '51', '10 Main', 'Econ').
      Rules:
    WhoMajor(N,M):-student(N,I,A,M).
      Queries:
      WhoMajor('Roosevelt',N)?

    $ project2 prog.txt
    Success!
    Schemes(2):
      student(N, I, A, M)
      WhoMajor(N,M)
    Facts(1):
      student('Roosevelt', '51', '10 Main', 'Econ').
    Rules(1):
      WhoMajor(N,M):-student(N,I,A,M).
    Queries(1):
      WhoMajor('Roosevelt',N)?
    Domain(4):
      '10 Main'
      '51'
      'Econ'
      'Roosevelt'
    ```
    """
    if len(argv) == 2:
        input_file = argv[1]
        with open(input_file, "r") as f:
            input_string = f.read()
            result = project2(input_string)
            print(result)
    else:
        print("usage: project2 <input file>")
