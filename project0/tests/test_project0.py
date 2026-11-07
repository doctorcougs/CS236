# type: ignore
import pytest

from project0.project0 import compute


def test_given_bad_input_when_project0_then_except():
    # givin
    input = 10

    # when
    with pytest.raises(TypeError):
        compute(input)

    # then
    pass


@pytest.mark.parametrize(
    "input, expected",
    [("who", "Hello World who"), ("do", "Hello World do"), ("you", "Hello World you")],
    ids=["who", "do", "you"],
)
def test_given_good_input_when_project0_then_match_pattern(input: str, expected: str):
    # given
    pass

    # when
    answer = compute(input)

    # then
    assert expected == answer
