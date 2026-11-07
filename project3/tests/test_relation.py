# type: ignore
import pytest

from project3.relation import IncompatibleOperandError, Relation


def test_given_empty_relation_when_add_tuple_then_tuple_in_relation():
    # given
    header = ("a", "b", "c")
    relation = Relation(header, set())
    input = ("'1'", "'2'", "'3'")

    # when
    relation.add_tuple(input)

    # then
    assert 1 == len(relation.set_of_tuples)
    assert input in relation.set_of_tuples


def test_given_relation_when_str_then_match_expected():
    # given
    header = ("a", "b", "c")
    set_of_tuples = set([("'1'", "'2'", "'3'"), ("'1'", "'3'", "'5'")])
    relation = Relation(header, set_of_tuples)

    expected = """+-----+-----+-----+
|  a  |  b  |  c  |
+-----+-----+-----+
| '1' | '2' | '3' |
| '1' | '3' | '5' |
+-----+-----+-----+"""

    # when
    answer = str(relation)

    # then
    assert expected == answer


def test_given_relation_and_wrong_size_when_add_tuple_then_exception():
    # given
    relation = Relation(("a", "b", "c"), set())

    # when
    with pytest.raises(IncompatibleOperandError) as exception:
        relation.add_tuple(("1", "2"))

    # then
    assert (
        "Error: ('1', '2') is not compatible with header ['a', 'b', 'c'] in Relation.add_tuple"
        == str(exception.value)
    )


def test_given_relation_when_add_tuple_then_added():
    # given
    relation = Relation(("a", "b", "c"), set())

    # when
    relation.add_tuple(("1", "2", "3"))

    # then
    assert ("1", "2", "3") in relation.set_of_tuples


def test_given_mismatched_header_and_tuple_when_construct_then_exception():
    # given
    header = ("a", "b", "c")
    set_of_tuples = set([("1", "2")])

    # when
    with pytest.raises(IncompatibleOperandError) as exception:
        _ = Relation(header, set_of_tuples)

    # then
    assert (
        "Error: ('1', '2') is not compatible with header ['a', 'b', 'c'] in Relation.add_tuple"
        == str(exception.value)
    )


def test_given_set_that_is_not_over_tuples_when_construct_then_exception():
    # given
    header = "a"
    set_of_tuples = set(["1"])

    # when
    with pytest.raises(IncompatibleOperandError) as exception:
        _ = Relation(header, set_of_tuples)

    # then
    assert (
        "Error: 1 is not type compatible with Relation.RelationTuple in Relation.add_tuple"
        == str(exception.value)
    )


def test_given_set_that_is_tuples_but_not_str_when_construct_then_exception():
    # given
    header = ("a", "b")
    set_of_tuples = set([("1", 2)])

    # when
    with pytest.raises(IncompatibleOperandError) as exception:
        _ = Relation(header, set_of_tuples)

    # then
    assert (
        "Error: ('1', 2) is not type compatible with Relation.RelationTuple in Relation.add_tuple"
        == str(exception.value)
    )


def test_given_mismatched_relations_when_difference_then_exception():
    # given
    left = Relation(("a", "b", "c"), set())
    right = Relation(("a", "b"), set())

    # when
    with pytest.raises(IncompatibleOperandError) as exception:
        left.difference(right)

    # then
    assert (
        "Error: headers ['a', 'b', 'c'] and ['a', 'b'] are not compatible in Relation.difference"
        == str(exception.value)
    )


def test_given_matched_relations_when_difference_then_difference():
    # given
    left = Relation(("a", "b", "c"), set([("1", "2", "3"), ("2", "4", "6")]))
    right = Relation(("a", "b", "c"), set([("2", "4", "6")]))
    expected = Relation(("a", "b", "c"), set([("1", "2", "3")]))

    # when
    answer = left.difference(right)

    # then
    assert expected == answer


def test_union_raises_when_headers_differ() -> None:
    # given
    P = Relation(["bart", "lisa"], {("h", "1"), ("m", "2")})
    W = Relation(["bart", "maggie"], {("f", "3")})  # header differs in second column

    # when
    # then
    with pytest.raises(IncompatibleOperandError):
        P.union(W)


@pytest.mark.parametrize(
    argnames=("hdr, rows1, rows2, expected_rows"),
    argvalues=(
        # Disjoint
        (
            ["A", "B"],
            {("1", "a"), ("2", "b")},
            {("3", "c")},
            {("1", "a"), ("2", "b"), ("3", "c")},
        ),
        # Overlap (duplicates should be removed by set semantics)
        (
            ["A", "B"],
            {("1", "a"), ("2", "b")},
            {("2", "b"), ("3", "c")},
            {("1", "a"), ("2", "b"), ("3", "c")},
        ),
        # Left empty
        (["A", "B"], set(), {("1", "a")}, {("1", "a")}),
        # Right empty
        (["A", "B"], {("1", "a")}, set(), {("1", "a")}),
        # Idempotent: R ∪ R = R
        (
            ["A", "B"],
            {("10", "x"), ("11", "y")},
            {("10", "x"), ("11", "y")},
            {("10", "x"), ("11", "y")},
        ),
    ),
    ids=("Disjoint", "Overlap", "Left Empty", "Right Empty", "Idempotent"),
)
def test_union_basic_cases(hdr, rows1, rows2, expected_rows):
    # given
    r1 = Relation(hdr, rows1)
    r2 = Relation(hdr, rows2)
    expected = Relation(hdr, expected_rows)

    # when
    answer = r1.union(r2)

    # then
    assert expected == answer


def test_given_bad_col_when_project_then_raise() -> None:
    # given
    r = Relation(["A", "B"], {("x", "1")})
    project_hdr = ["Z"]

    # when
    # then
    with pytest.raises(IncompatibleOperandError):
        r.project(project_hdr)


@pytest.mark.parametrize(
    argnames=("hdr, rows, project_hdr, expected_rows"),
    argvalues=(
        # Disjoint
        (
            ["A", "B"],
            set(),
            ["A"],
            set(),
        ),
        # Two Columns
        (
            ["A", "B"],
            {("x", "1"), ("y", "2")},
            ["A"],
            {("x",), ("y",)},
        ),
        # Two Columns with Duplicates
        (
            ["A", "B"],
            {("x", "1"), ("x", "2")},
            ["A"],
            {("x",)},
        ),
        # Three Columns
        (
            ["A", "B", "C"],
            {("x1", "1", "True"), ("y", "2", "False")},
            ["B"],
            {("1",), ("2",)},
        ),
        # Three Columns with Two Adjacent
        (
            ["A", "B", "C"],
            {
                ("x", "1", "True"),
                ("y", "2", "False"),
                ("x", "1", "False"),
            },
            ["A", "B"],
            {("x", "1"), ("y", "2")},
        ),
        # Three Columns with Two Not Adjacent
        (
            ["A", "B", "C"],
            {
                ("x", "1", "True"),
                ("y", "2", "False"),
                ("x", "9", "True"),
            },
            ["A", "C"],
            {("x", "True"), ("y", "False")},
        ),
    ),
    ids=(
        "Empty",
        "Two Cols",
        "Two Cols with Dups",
        "Three Cols",
        "Three Cols with Two Adj",
        "Three Cols with Two Not Adj",
    ),
)
def test_project_basic_cases(hdr, rows, project_hdr, expected_rows):
    # given
    r = Relation(hdr, rows)
    expected = Relation(project_hdr, expected_rows)

    # when
    answer = r.project(project_hdr)

    # then
    assert expected == answer
