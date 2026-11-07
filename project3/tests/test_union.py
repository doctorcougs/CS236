import pytest

from project3.relation import IncompatibleOperandError, Relation


def test_working():
    header = ("a", "b")
    relation1 = Relation(header, {("1", "2")})
    relation2 = Relation(header, {("2", "3")})

    new_relation = relation1.union(relation2)

    expected_relation = Relation(header, {("1", "2"), ("2", "3")})

    assert new_relation == expected_relation


def test_incompatible():
    header1 = ("a", "b")
    header2 = ("b", "c")
    relation1 = Relation(header1, set())
    relation2 = Relation(header2, set())

    with pytest.raises(IncompatibleOperandError):
        relation1.union(relation2)


def test_union_three_columns():  # AI Generated
    # Create two relations with the same 3-column header
    header = ("id", "name", "age")

    relation1 = Relation(header, set())
    relation1.add_tuple(("1", "Alice", "20"))
    relation1.add_tuple(("2", "Bob", "25"))

    relation2 = Relation(header, set())
    relation2.add_tuple(("2", "Bob", "25"))  # duplicate tuple
    relation2.add_tuple(("3", "Charlie", "30"))

    # Perform union (should include all unique tuples)
    new_relation = relation1.union(relation2)

    # Expected result contains all distinct tuples from both relations
    expected_relation = Relation(header, set())
    expected_relation.add_tuple(("1", "Alice", "20"))
    expected_relation.add_tuple(("2", "Bob", "25"))
    expected_relation.add_tuple(("3", "Charlie", "30"))

    # Assert that the union result matches expectation
    assert new_relation == expected_relation
