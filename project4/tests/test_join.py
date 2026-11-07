from project4.relation import Relation


def test_simple_working():
    header1 = ("a", "b", "c")
    relation1 = Relation(header1, set())
    relation1.add_tuple(("1", "2", "3"))
    relation1.add_tuple(("4", "5", "6"))

    header2 = ("b", "d", "e")
    relation2 = Relation(header2, set())
    relation2.add_tuple(("2", "4", "5"))
    relation2.add_tuple(("6", "7", "8"))

    new_relation = relation1.join(relation2)

    expected_header = ("a", "b", "c", "d", "e")
    expected_relation = Relation(expected_header, set())
    expected_relation.add_tuple(("1", "2", "3", "4", "5"))

    assert new_relation == expected_relation


def test_no_matching_headers():
    header1 = ("a", "b")
    relation1 = Relation(header1, set())
    relation1.add_tuple(("1", "2"))

    header2 = ("c", "d")
    relation2 = Relation(header2, set())
    relation2.add_tuple(("3", "4"))

    new_relation = relation1.join(relation2)

    expected_header = ("a", "b", "c", "d")
    expected_relation = Relation(expected_header, set())
    expected_relation.add_tuple(("1", "2", "3", "4"))

    assert new_relation == expected_relation


def test_two_matching_headers():  # AI generated
    # Relations share two attributes: b and c
    header1 = ("a", "b", "c")
    relation1 = Relation(header1, set())
    relation1.add_tuple(("1", "2", "3"))  # matches tuple A in relation2
    relation1.add_tuple(("4", "5", "6"))  # matches tuple B in relation2
    relation1.add_tuple(("7", "8", "9"))  # NO MATCH

    header2 = ("b", "c", "d")
    relation2 = Relation(header2, set())
    relation2.add_tuple(("2", "3", "10"))  # matches first tuple from relation1
    relation2.add_tuple(("5", "6", "20"))  # matches second tuple from relation1
    relation2.add_tuple(("0", "0", "30"))  # NO MATCH

    new_relation = relation1.join(relation2)

    expected_header = ("a", "b", "c", "d")
    expected_relation = Relation(expected_header, set())
    expected_relation.add_tuple(("1", "2", "3", "10"))
    expected_relation.add_tuple(("4", "5", "6", "20"))
    # note: no tuple for ("7", "8", "9") because no match in relation2
    # note: tuple ("0", "0", "30") also produces no output

    assert new_relation == expected_relation
