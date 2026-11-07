from project4.relation import Relation


def test_three_col():
    header = ("a", "b", "c")
    relation = Relation(header, set())
    relation.add_tuple(("1", "3", "3"))
    relation.add_tuple(("4", "6", "6"))
    relation.add_tuple(("4", "4", "6"))

    new_relation = relation.select_eq_lit("a", "4")

    expected_relation = Relation(header, set())
    expected_relation.add_tuple(("4", "6", "6"))
    expected_relation.add_tuple(("4", "4", "6"))

    assert new_relation == expected_relation


def test_empty_relation():
    header = ("a", "b")
    relation = Relation(header, set())

    new_relation = relation.select_eq_lit("a", "7")

    expected_relation = Relation(header, set())

    assert new_relation == expected_relation


def test_no_new_relation():
    header = ("a", "b")
    relation = Relation(header, set())
    relation.add_tuple(("1", "2"))
    relation.add_tuple(("3", "4"))

    new_relation = relation.select_eq_lit("a", "2")

    expected_relation = Relation(header, set())

    assert new_relation == expected_relation


def test_two_col():
    header = ("a", "b")
    relation = Relation(header, set())
    relation.add_tuple(("1", "2"))
    relation.add_tuple(("3", "3"))

    new_relation = relation.select_eq_lit("b", "3")

    expected_relation = Relation(header, set())
    expected_relation.add_tuple(("3", "3"))

    assert new_relation == expected_relation
