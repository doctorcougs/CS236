# type: ignore
from project1.project1 import project1


def test_given_good_input_when_project1_then_output_tokens():
    # given
    input = " \t\r\n::\t:\n\n"
    expected = (
        '(COLON,":",2)\n(COLON,":",2)\n(COLON,":",2)\n(EOF,"",4)\nTotal Tokens = 4'
    )

    # when
    result = project1(input)

    # then
    assert expected == result


def test_given_bad_input_when_project1_then_output_tokens_to_undefined():
    # given
    input = " \t\r\n:\n!this"
    expected = '(COLON,":",2)\n(UNDEFINED,"!",3)\n\nTotal Tokens = Error on line 3'

    # when
    result = project1(input)

    # then
    assert expected == result
