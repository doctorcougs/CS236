"""Function to call lexer and get tokens.

These are the two project level entry points: `project1` and `project1cli`.
All the pass-off tests use `project1`.
"""

from sys import argv

from project1.lexer import lexer


def project1(input_string: str) -> str:
    """Build the token stream for a given input.

    Args:
        input_string (str): The string to tokenize.

    Returns:
        out: the token stream, as a string, from the input string

    Examples:
        >>> from project1.project1 import project1
        >>> token_stream = project1('\\n\\n::')
        >>> print(token_stream)
        (COLON,":",3)
        (COLON,":",3)
        (EOF,"",3)
        Total Tokens = 3
    """
    result: str = ""
    token_count = 0
    for i in lexer(input_string):
        result += str(i) + "\n"
        token_count += 1
        if i.token_type == "UNDEFINED":
            return result + "\nTotal Tokens = Error on line " + str(i.line_num)

    return result + "Total Tokens = " + str(token_count)


def project1cli() -> None:
    """Build the token stream from the contents of a file.

    `project1cli` is only called from the command line in the integrated terminal.
    Prints the token stream resulting from the contents of the named file.

    Args:
        argv (list[str]): Generated from the command line and needs to name the input file.

    Examples:
    ```
    $ project1 t.txt
    (COLON,":",2)
    (COLON,":",2)
    (COLON,":",2)
    (EOF,"",5)
    Total Tokens = 4
    ```
    """
    if len(argv) == 2:
        input_file = argv[1]
        with open(input_file, "r") as f:
            input_string = f.read()
            result = project1(input_string)
            print(result)
    else:
        print("usage: project1 <input file>")
