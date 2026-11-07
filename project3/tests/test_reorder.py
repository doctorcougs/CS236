import pytest

from project3.relation import IncompatibleOperandError, Relation


def test_three_col():
    header = ("a", "b", "c")
    relation = Relation(header, set())
    relation.add_tuple(("1", "3", "3"))
    relation.add_tuple(("4", "6", "6"))
    relation.add_tuple(("4", "4", "6"))

    new_relation = relation.reorder(["b", "a", "c"])

    new_header = ("b", "a", "c")
    expected_relation = Relation(new_header, set())
    expected_relation.add_tuple(("3", "1", "3"))
    expected_relation.add_tuple(("6", "4", "6"))
    expected_relation.add_tuple(("4", "4", "6"))

    assert new_relation == expected_relation


def test_empty_relation():
    header = ("a", "b")
    relation = Relation(header, set())

    new_relation = relation.reorder(["b", "a"])

    new_header = ("b", "a")
    expected_relation = Relation(new_header, set())

    assert new_relation == expected_relation


def test_not_enough_reordered():
    header = ("a", "b", "c")
    relation = Relation(header, set())

    with pytest.raises(IncompatibleOperandError):
        relation.reorder(["b", "a"])


def test_unexpected_list():
    header = ("a", "b")
    relation = Relation(header, set())

    with pytest.raises(IncompatibleOperandError):
        relation.reorder(["C", "b", "a"])
