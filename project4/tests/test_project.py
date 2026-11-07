import pytest

from project4.relation import IncompatibleOperandError, Relation


def test_working():
    header = ("a", "b")
    relation = Relation(header, set())

    new_relation = relation.project(("a"))

    expected_relation = Relation(("a"), set())

    assert new_relation == expected_relation


def test_incompatible():
    relation = Relation(("a"), set())

    with pytest.raises(IncompatibleOperandError):
        relation.project(("b"))


def test_project_multiple_columns():  # AI generated
    header = ("id", "name", "age")
    relation = Relation(header, set())
    relation.add_tuple(("1", "Alice", "20"))
    relation.add_tuple(("2", "Bob", "25"))
    relation.add_tuple(("3", "Charlie", "30"))

    # Project onto just two columns
    new_relation = relation.project(("id", "name"))

    # Expected relation should only include the id and name columns
    expected_relation = Relation(("id", "name"), set())
    expected_relation.add_tuple(("1", "Alice"))
    expected_relation.add_tuple(("2", "Bob"))
    expected_relation.add_tuple(("3", "Charlie"))

    assert new_relation == expected_relation
