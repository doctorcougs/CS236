# type: ignore
from project2.parser import TokenStream
from project2.token import Token


def test_given_token_stream_when_advance_then_stutter_last_token():
    # given
    token_list = [Token.colon(":"), Token.eof("")]
    token_iterator = iter(token_list)
    token = TokenStream(token_iterator)

    # when
    token.match("COLON")
    token.advance()

    # then
    assert token.token == Token.eof("")

    # when
    token.match("EOF")
    token.advance()

    # then
    assert token.token == Token.eof("")

    # when
    token.match("EOF")

    # then
    assert token.token == Token.eof("")


"""
Here is an example test for testing the id_list production (it assumes there is an id_list function defined in the parser.py file):

import pytest
from project2.datalogprogram import Parameter
from project2.parser import id_list, TokenStream

id_list_token_stream = TokenStream(
    iter(
        [
            Token.comma(","),
            Token.id("A"),
            Token.comma(","),
            Token.id("B"),
            Token.comma(","),
            Token.id("C"),
            Token.right_paren(")"),
        ]
    )
)
id_list_expected = [Parameter.id("A"), Parameter.id("B"), Parameter.id("C")]


@pytest.mark.parametrize(
    argnames=["rule", "token_stream", "expected"],
    argvalues=[(id_list, id_list_token_stream, id_list_expected)],
    ids=["id_list"],
)
def test_given_valid_token_stream_when_parse_rule_then_match_value(
    rule, token_stream, expected
):
    # given
    # test_input

    # when
    answer = rule(token_stream)

    # then
    assert expected == answer
"""
