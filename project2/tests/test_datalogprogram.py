# type: ignore
import pytest

from project2.datalogprogram import DatalogProgram, Parameter, Predicate, Rule


@pytest.mark.parametrize(
    argnames=["test_input", "expected"],
    argvalues=[
        (Predicate("f", []), "f()"),
        (Predicate("f", [Parameter("g", "ID")]), "f(g)"),
        (
            Predicate(
                "f", [Parameter("g", "ID"), Parameter("h", "ID"), Parameter("i", "ID")]
            ),
            "f(g,h,i)",
        ),
        (
            Predicate(
                "f",
                [
                    Parameter("'this is a string'", "STRING"),
                    Parameter("i", "ID"),
                    Parameter("'C+ doh'", "STRING"),
                ],
            ),
            "f('this is a string',i,'C+ doh')",
        ),
    ],
    ids=["empty", "one", "many", "mix"],
)
def test_given_predicate_when_str_then_match_expected(
    test_input: Predicate, expected: str
):
    # given
    # test_input
    # expected

    # when
    answer = str(test_input)

    # then
    assert expected == answer


def test_given_rule_when_str_then_match_expected():
    # given
    head: Predicate = Predicate("WhoMajor", [Parameter.id("N"), Parameter.id("M")])
    predicates: list[Predicate] = [
        Predicate(
            "student",
            [
                Parameter.id("N"),
                Parameter.id("I"),
                Parameter.id("A"),
                Parameter.id("M"),
            ],
        ),
        Predicate(
            "instructor", [Parameter.id("M"), Parameter.id("A"), Parameter.id("Y")]
        ),
    ]
    rule: Rule = Rule(head, predicates)

    # when
    answer = str(rule)

    # then
    assert "WhoMajor(N,M) :- student(N,I,A,M),instructor(M,A,Y)" == answer


schemes = [
    Predicate(
        "student",
        [Parameter.id("N"), Parameter.id("I"), Parameter.id("A"), Parameter.id("M")],
    ),
    Predicate("WhoMajor", [Parameter.id("N"), Parameter.id("M")]),
]

prog_schemes_only = DatalogProgram(schemes, [], [], [])

schemes_only = """Schemes(2):
  student(N,I,A,M)
  WhoMajor(N,M)
Facts(0):
Rules(0):
Queries(0):
Domain(0):"""

facts = [
    Predicate(
        "student",
        [
            Parameter.string("'Roosevelt'"),
            Parameter.string("'51'"),
            Parameter.string("'10 Main'"),
            Parameter.string("'Econ'"),
        ],
    ),
    Predicate(
        "student",
        [
            Parameter.string("'Reagan'"),
            Parameter.string("'52'"),
            Parameter.string("'11 Maple'"),
            Parameter.string("'Econ'"),
        ],
    ),
    Predicate(
        "student",
        [
            Parameter.string("'G.W.Bush'"),
            Parameter.string("'53'"),
            Parameter.string("'12 Ashton'"),
            Parameter.string("'AgriSci'"),
        ],
    ),
    Predicate(
        "student",
        [
            Parameter.string("'Clinton'"),
            Parameter.string("'54'"),
            Parameter.string("''"),
            Parameter.string("'Lying'"),
        ],
    ),
]

prog_facts_only = DatalogProgram([], facts, [], [])

facts_only = """Schemes(0):
Facts(4):
  student('Roosevelt','51','10 Main','Econ').
  student('Reagan','52','11 Maple','Econ').
  student('G.W.Bush','53','12 Ashton','AgriSci').
  student('Clinton','54','','Lying').
Rules(0):
Queries(0):
Domain(15):
  ''
  '10 Main'
  '11 Maple'
  '12 Ashton'
  '51'
  '52'
  '53'
  '54'
  'AgriSci'
  'Clinton'
  'Econ'
  'G.W.Bush'
  'Lying'
  'Reagan'
  'Roosevelt'"""

rules = [
    Rule(
        Predicate("WhoMajor", [Parameter.id("N"), Parameter.id("M")]),
        [
            Predicate(
                "student",
                [
                    Parameter.id("N"),
                    Parameter.id("I"),
                    Parameter.id("A"),
                    Parameter.id("M"),
                ],
            ),
            Predicate(
                "instructor", [Parameter.id("M"), Parameter.id("A"), Parameter.id("Y")]
            ),
        ],
    )
]

prog_rules_only = DatalogProgram([], [], rules, [])

rules_only = """Schemes(0):
Facts(0):
Rules(1):
  WhoMajor(N,M) :- student(N,I,A,M),instructor(M,A,Y).
Queries(0):
Domain(0):"""

queries = [
    Predicate(
        "WhoMajor",
        [
            Parameter.string("'Roosevelt'"),
            Parameter.id("N"),
        ],
    ),
    Predicate(
        "WhoMajor",
        [
            Parameter.id("M"),
            Parameter.string("'Econ'"),
        ],
    ),
    Predicate(
        "WhoMajor",
        [
            Parameter.string("'George Washington'"),
            Parameter.string("'PoliSci'"),
        ],
    ),
    Predicate(
        "WhoMajor",
        [
            Parameter.string("'Abraham Lincoln'"),
            Parameter.string("'Law'"),
        ],
    ),
    Predicate(
        "student",
        [
            Parameter.string("'John Adams'"),
            Parameter.id("I"),
            Parameter.id("A"),
            Parameter.id("M"),
        ],
    ),
]

prog_queries_only = DatalogProgram([], [], [], queries)

queries_only = """Schemes(0):
Facts(0):
Rules(0):
Queries(5):
  WhoMajor('Roosevelt',N)?
  WhoMajor(M,'Econ')?
  WhoMajor('George Washington','PoliSci')?
  WhoMajor('Abraham Lincoln','Law')?
  student('John Adams',I,A,M)?
Domain(0):"""

prog_all = DatalogProgram(schemes, facts, rules, queries)
all = """Schemes(2):
  student(N,I,A,M)
  WhoMajor(N,M)
Facts(4):
  student('Roosevelt','51','10 Main','Econ').
  student('Reagan','52','11 Maple','Econ').
  student('G.W.Bush','53','12 Ashton','AgriSci').
  student('Clinton','54','','Lying').
Rules(1):
  WhoMajor(N,M) :- student(N,I,A,M),instructor(M,A,Y).
Queries(5):
  WhoMajor('Roosevelt',N)?
  WhoMajor(M,'Econ')?
  WhoMajor('George Washington','PoliSci')?
  WhoMajor('Abraham Lincoln','Law')?
  student('John Adams',I,A,M)?
Domain(15):
  ''
  '10 Main'
  '11 Maple'
  '12 Ashton'
  '51'
  '52'
  '53'
  '54'
  'AgriSci'
  'Clinton'
  'Econ'
  'G.W.Bush'
  'Lying'
  'Reagan'
  'Roosevelt'"""


@pytest.mark.parametrize(
    argnames=["test_input", "expected"],
    argvalues=[
        (prog_schemes_only, schemes_only),
        (prog_facts_only, facts_only),
        (prog_rules_only, rules_only),
        (prog_queries_only, queries_only),
        (prog_all, all),
    ],
    ids=["schemes", "facts", "rules", "queries", "all"],
)
def test_given_datalog_program_when_str_then_match_expected(
    test_input: DatalogProgram, expected: str
):
    # given
    # test_input
    # expected

    # when
    answer = str(test_input)

    # then
    assert expected == answer
