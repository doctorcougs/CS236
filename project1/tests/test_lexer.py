# type: ignore
import pytest

from project1.lexer import lexer
from project1.token import Token

inputs = [
    (": ", [Token("COLON", ":", 1), Token("EOF", "", 1)]),
    (" \t\r\n\n: ", [Token("COLON", ":", 3), Token("EOF", "", 3)]),
    ("   !undefined\n\t", [Token("UNDEFINED", "!", 1)]),
]
ids = [
    "colon",
    "colon-line",
    "undefined",
]


@pytest.mark.parametrize("test_input, expected", inputs, ids=ids)
def test_given_input_when_lexer_then_match_tokens(
    test_input: str, expected: list[Token]
):
    # given
    # input

    # went
    tokens = [i for i in lexer(test_input)]

    # then
    assert len(expected) == len(tokens)
    assert expected == tokens
