# type: ignore
import pytest

from project4.relation import IncompatibleOperandError, Relation


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
