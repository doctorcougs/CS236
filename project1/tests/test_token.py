# type: ignore
import pytest

from project1.token import Token

str_test_inputs = [
    (Token.colon(":"), '(COLON,":",0)'),
    (Token.colon_dash(":-"), '(COLON_DASH,":-",0)'),
    (Token.comma(","), '(COMMA,",",0)'),
    (Token.comment("# line comment"), '(COMMENT,"# line comment",0)'),
    (
        Token.undefined("lots of undefined stuff"),
        '(UNDEFINED,"lots of undefined stuff",0)',
    ),
    (Token.eof(""), '(EOF,"",0)'),
    (Token.facts("Facts"), '(FACTS,"Facts",0)'),
    (Token.id("id"), '(ID,"id",0)'),
    (Token.left_paren("("), '(LEFT_PAREN,"(",0)'),
    (Token.period("."), '(PERIOD,".",0)'),
    (Token.queries("Queries"), '(QUERIES,"Queries",0)'),
    (Token.q_mark("?"), '(Q_MARK,"?",0)'),
    (Token.right_paren(")"), '(RIGHT_PAREN,")",0)'),
    (Token.rules("Rules"), '(RULES,"Rules",0)'),
    (Token.schemes("Schemes"), '(SCHEMES,"Schemes",0)'),
    (Token.string("string"), '(STRING,"string",0)'),
    (Token.whitespace(" \t\r\n"), '(WHITESPACE," \t\r\n",0)'),
]
str_test_ids = [
    "colon",
    "colon_dash",
    "comma",
    "comment",
    "undefined",
    "eof",
    "facts",
    "id",
    "left_paren",
    "period",
    "queries",
    "q_mark",
    "right_paren",
    "rules",
    "schemes",
    "string",
    "whitespace",
]


@pytest.mark.parametrize("token, expected", str_test_inputs, ids=str_test_ids)
def test_given_good_token_when_str_then_match_expected(token: Token, expected: str):
    # given
    # token

    # when
    result = str(token)

    # then
    assert expected == result
