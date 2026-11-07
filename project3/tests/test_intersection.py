import pytest

from project3.relation import IncompatibleOperandError, Relation


def test_working():
    header = ("a", "b")
    relation1 = Relation(header, set())
    relation1.add_tuple(("1", "2"))
    relation1.add_tuple(("2", "3"))

    relation2 = Relation(header, set())
    relation2.add_tuple(("1", "2"))
    relation2.add_tuple(("3", "4"))

    new_relation = relation1.intersection(relation2)

    expected_relation = Relation(header, set())
    expected_relation.add_tuple(("1", "2"))

    assert new_relation == expected_relation


def test_incompatible():
    header1 = ("a", "b")
    header2 = ("c", "d")

    relation1 = Relation(header1, {("1", "2")})
    relation2 = Relation(header2, {("1", "2")})

    with pytest.raises(IncompatibleOperandError):
        relation1.intersection(relation2)


def test_intersection_three_columns():  # AI generated
    # Create two relations with the same 3-column header
    header = ("id", "name", "age")

    relation1 = Relation(header, set())
    relation1.add_tuple(("1", "Alice", "20"))
    relation1.add_tuple(("2", "Bob", "25"))
    relation1.add_tuple(("3", "Charlie", "30"))

    relation2 = Relation(header, set())
    relation2.add_tuple(("2", "Bob", "25"))
    relation2.add_tuple(("3", "Charlie", "30"))
    relation2.add_tuple(("4", "Diana", "22"))

    # Perform intersection (should keep only matching tuples)
    new_relation = relation1.intersection(relation2)

    # Expected result contains only tuples common to both
    expected_relation = Relation(header, set())
    expected_relation.add_tuple(("2", "Bob", "25"))
    expected_relation.add_tuple(("3", "Charlie", "30"))

    # Assert that the intersection result matches expectation
    assert new_relation == expected_relation
