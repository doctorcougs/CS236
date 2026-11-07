"""Turn a input string into a stream of tokens with lexical analysis.

The `lexer(input_string: str)` function is the entry point. It generates a
stream of tokens from the `input_string`.

Examples:

    >>> from project1.lexer import lexer
    >>> input_string = ":\\n  \\n:"
    >>> for i in lexer(input_string):
    ...     print(i)
    ...
    (COLON,":",1)
    (COLON,":",3)
    (EOF,"",3)
"""

from typing import Iterator

from project1.fsm import (
    ID,
    Colon,
    Colon_Dash,
    Comma,
    Comment,
    Eof,
    Facts,
    FiniteStateMachine,
    Left_Paren,
    Period,
    Q_Mark,
    Queries,
    Right_Paren,
    Rules,
    Schemes,
    String,
    WhiteSpace,
    run_fsm,
)
from project1.token import Token, TokenType


def _is_last_token(token: Token) -> bool:
    if token.token_type == "EOF":
        return True
    return False


def _get_token(input_str: str, fsms: list[FiniteStateMachine]) -> Token:
    best_token = Token.undefined("")
    best_token_length = 0

    for fsm in fsms:
        numchars, value = run_fsm(fsm, input_str)
        if numchars > best_token_length:
            best_token = value
            best_token_length = numchars

    if best_token_length == 0 and input_str:
        return Token.undefined(input_str[0])

    return best_token


def lexer(input_string: str) -> Iterator[Token]:
    """Produce a stream of tokens from a given input string.

    Pseudo-code:

    ```
    fsms: list[FiniteStateMachine] = [Colon(), Eof(), WhiteSpace()]
    hidden: list[TokenType] = ["WHITESPACE"]
    line_num: int = 1
    token: Token = Token.undefined("")
    while not _is_last_token(token):
        token = _get_token(input_string, fsms)
        token.line_num = line_num
        line_num = line_num + _get_new_lines(token.value)
        input_string = input_string.removeprefix(token.value)
        if token.token_type in hidden:
            continue
        yield token
    ```

    The `_get_token` function should return the token from the FSM that reads
    the most characters. In the case of two FSMs reading the same number of
    characters, the one that comes first in the list of FSMs, `fsms`, wins.
    Some care must be given to determining when the _last_ token has been
    generated and how to update the new `line_num` for the next token.

    Args:
        input_string: Input string for token generation.

    Yields:
        token: The current token resulting from the string.
    """
    fsms: list[FiniteStateMachine] = [
        Comma(),
        Period(),
        Q_Mark(),
        Left_Paren(),
        Right_Paren(),
        Colon(),
        Eof(),
        Colon_Dash(),
        Schemes(),
        Facts(),
        Rules(),
        Queries(),
        WhiteSpace(),
        Comment(),
        ID(),
        String(),
    ]  # noqa: F841
    hidden: list[TokenType] = ["WHITESPACE"]  # noqa: F841
    line_num: int = 1
    token: Token = Token.undefined("")
    while not _is_last_token(token):
        token = _get_token(input_string, fsms)
        token.line_num = line_num
        line_num = line_num + token.value.count("\n")
        input_string = input_string.removeprefix(token.value)
        if token.token_type in hidden:
            continue

        if token.token_type == "UNDEFINED":
            yield token
            return

        yield token
