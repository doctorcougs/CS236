from homework1.set_operations import cartesian_product, intersection, union

#############################
##     Integration Tests   ##
#############################

# --- UNION (integers) --------------------------------------------------------


def test_union_integration_disjoint() -> None:
    # Function inputs
    A: set[int] = {1, 2}
    B: set[int] = {3, 4}

    # Expected output
    expected: set[int] = {1, 2, 3, 4}

    # Assert that the union function works correctly
    assert union(A, B) == expected


def test_union_integration_overlap() -> None:
    # Function inputs
    A: set[int] = {1, 2, 3}
    B: set[int] = {3, 4, 5}

    # Expected output
    expected: set[int] = {1, 2, 3, 4, 5}

    # Assert that the union function works correctly
    assert union(A, B) == expected


def test_union_integration_with_empty() -> None:
    # Function inputs
    A: set[int] = set()
    B: set[int] = {10, 20}

    # Expected output
    expected: set[int] = {10, 20}

    # Assert that the union function works correctly
    assert union(A, B) == expected


# --- INTERSECTION (integers) -------------------------------------------------


def test_intersection_integration_basic() -> None:
    # Function inputs
    A: set[int] = {1, 2, 3, 4}
    B: set[int] = {3, 4, 5, 6}

    # Expected output
    expected: set[int] = {3, 4}

    # Assert that the intersection function works correctly
    assert intersection(A, B) == expected


def test_intersection_integration_disjoint() -> None:
    # Function inputs
    A: set[int] = {1, 2}
    B: set[int] = {3, 4}

    # Expected output
    expected: set[int] = set()

    # Assert that the intersection function works correctly
    assert intersection(A, B) == expected


def test_intersection_integration_with_empty() -> None:
    # Function inputs
    A: set[int] = set()
    B: set[int] = {1, 2, 3}

    # Expected output
    expected: set[int] = set()

    # Assert that the intersection function works correctly
    assert intersection(A, B) == expected


# --- CARTESIAN PRODUCT (mixed types) ----------------------------------------


def test_cartesian_product_integration_ints_and_strings() -> None:
    # Function inputs
    A: set[int] = {1, 2}
    B: set[str] = {"a", "b"}

    # Expected output
    expected: set[tuple[int, str]] = {(1, "a"), (1, "b"), (2, "a"), (2, "b")}

    # Assert that the cartesian_product function works correctly
    assert cartesian_product(A, B) == expected


def test_cartesian_product_integration_strings_and_bools() -> None:
    # Function inputs
    A: set[str] = {"x", "y"}
    B: set[bool] = {True, False}

    # Expected output
    expected: set[tuple[str, bool]] = {
        ("x", True),
        ("x", False),
        ("y", True),
        ("y", False),
    }

    # Assert that the cartesian_product function works correctly
    assert cartesian_product(A, B) == expected


def test_cartesian_product_integration_with_empty() -> None:
    # Function inputs
    A: set[int] = set()
    B: set[str] = {"only"}

    # Expected output
    expected: set[tuple[int, str]] = set()

    # Assert that the cartesian_product function works correctly
    assert cartesian_product(A, B) == expected
