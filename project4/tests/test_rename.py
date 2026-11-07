import pytest

from project4.relation import IncompatibleOperandError, Relation


def test_working():
    header = "a"
    relation = Relation(header, set())

    new_relation = relation.rename(["b"])

    new_header = "b"
    expected_relation = Relation(new_header, set())

    assert expected_relation == new_relation


def test_not_enough():
    header = ("a", "b")
    relation = Relation(header, set())

    with pytest.raises(IncompatibleOperandError):
        relation.rename(["c"])


def test_full_relation():
    header = ("a", "b", "c", "d")
    relation = Relation(header, set())

    new_relation = relation.rename(["d", "b", "a", "c"])

    new_header = ("d", "b", "a", "c")
    expected_relation = Relation(new_header, set())

    assert new_relation == expected_relation


def test_with_tuples():
    header = ("A",)
    relation = Relation(header, set())
    relation.add_tuple(("1",))
    relation.add_tuple(("2",))

    new_relation = relation.rename(["B"])

    new_header = ("B",)
    expected_relation = Relation(new_header, set())
    expected_relation.add_tuple(("1",))
    expected_relation.add_tuple(("2",))

    assert new_relation == expected_relation
