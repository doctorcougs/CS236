# type: ignore
import pytest

from project3.datalogprogram import Parameter, Predicate
from project3.relation import Relation
from project3.reporter import query_report

input_literals_no = (
    Predicate("SK", [Parameter.string("'c'"), Parameter.string("'c'")]),
    Relation(("X", "Y"), set()),
)
expect_literals_no = "SK('c','c')? No"


input_literals_yes = (
    Predicate("SK", [Parameter.string("'b'"), Parameter.string("'c'")]),
    Relation(("X", "Y"), set([("'b'", "'c'")])),
)
expect_literals_yes = "SK('b','c')? Yes(1)"


input_mixed_no = (
    Predicate("SK", [Parameter.id("A"), Parameter.string("'c'")]),
    Relation(("A",), set()),
)
expect_mixed_no = "SK(A,'c')? No"


input_mixed_yes = (
    Predicate("SK", [Parameter.id("A"), Parameter.string("'c'")]),
    Relation(("A",), set([("'a'",), ("'b'",)])),
)
expect_mixed_yes = """SK(A,'c')? Yes(2)
  A='a'
  A='b'"""

input_id_yes = (
    Predicate("SK", [Parameter.id("A"), Parameter.string("B")]),
    Relation(("A", "B"), set([("'a'", "'b'"), ("'a'", "'c'"), ("'b'", "'c'")])),
)
expect_id_yes = """SK(A,B)? Yes(3)
  A='a', B='b'
  A='a', B='c'
  A='b', B='c'"""


@pytest.mark.parametrize(
    argnames=("input", "expect"),
    argvalues=(
        (input_literals_no, expect_literals_no),
        (input_literals_yes, expect_literals_yes),
        (input_mixed_no, expect_mixed_no),
        (input_mixed_yes, expect_mixed_yes),
        (input_id_yes, expect_id_yes),
    ),
    ids=[
        "literals_no",
        "literals_yes",
        "mixed_no",
        "mixed_yes",
        "id_yes",
    ],
)
def test_given_query_reporter_when_str_then_match_expect(input, expect):
    # given
    # input, expect
    query, answer = input

    # when
    answer = query_report(query, answer)

    # then
    assert expect == answer


def test_given_iterator_when_reporting_then_match_expect():
    # given
    answers = [
        input_literals_no,
        input_literals_yes,
        input_mixed_no,
        input_mixed_yes,
        input_id_yes,
    ]
    expect = f"{expect_literals_no}\n{expect_literals_yes}\n{expect_mixed_no}\n{expect_mixed_yes}\n{expect_id_yes}"

    # when
    answer = "\n".join([query_report(i, j) for i, j in answers])

    # then
    assert expect == answer
