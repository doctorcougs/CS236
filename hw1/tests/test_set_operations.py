# tests/test_set_operations.py
import pytest

from homework1.set_operations import cartesian_product, intersection, union


#################
## Union Tests ##
#################
# positive tests: what should happen
def test_union_positive() -> None:
    # Function inputs
    A: set[int] = {1, 2}
    B: set[int] = {2, 3}

    # Expected output
    expected: set[int] = {1, 2, 3}

    # Assert that the union function works correctly
    assert union(A, B) == expected


# negative tests: what should not happen
def test_union_negative() -> None:
    # Function inputs
    A: set[int] = {1}
    B: set[int] = {2}

    # Expected output
    incorrect_result: set[int] = {1}

    # Assert that the union function works does not work incorrectly
    assert union(A, B) != incorrect_result


# TypeError tests: when invalid input should raise an error
def test_union_invalid_input_type_1() -> None:
    # one input is the wrong type
    A: str = "not a set"
    B: set[int] = {1, 2}

    with pytest.raises(TypeError):
        union(A, B)


def test_union_invalid_input_type_2() -> None:
    # one input is the wrong type
    A: set[int] = {1, 2}
    B: str = "not a set"

    with pytest.raises(TypeError):
        union(A, B)


def test_union_invalid_element_type() -> None:
    # one input has an element that is not an int
    A: set[int] = {1, 2}
    B: set[int] = {2, "not an int"}

    with pytest.raises(TypeError):
        union(A, B)


########################
## Intersection Tests ##
########################
# positive tests: what should happen
def test_intersection_positive() -> None:
    # Function inputs
    A: set[int] = {1, 2}
    B: set[int] = {2, 3}

    # Expected output
    expected: set[int] = {2}

    # Assert that the intersection function works correctly
    assert intersection(A, B) == expected


# negative tests: what should not happen
def test_intersection_negative() -> None:
    # Function inputs
    A: set[int] = {1}
    B: set[int] = {2}

    # Expected output
    incorrect_result: set[int] = {1, 2}

    # Assert that the intersection function works does not work incorrectly
    assert intersection(A, B) != incorrect_result


# TypeError tests: when invalid input should raise an error
def test_intersection_invalid_input_type_1() -> None:
    # one input is the wrong type
    A: str = "not a set"
    B: set[int] = {1, 2}

    with pytest.raises(TypeError):
        intersection(A, B)


def test_intersection_invalid_input_type_2() -> None:
    # one input is the wrong type
    A: set[int] = {1, 2}
    B: str = "not a set"

    with pytest.raises(TypeError):
        intersection(A, B)


def test_intersection_invalid_element_type() -> None:
    # one input has an element that is not an int
    A: set[int] = {1, 2}
    B: set[int] = {2, "not an int"}

    with pytest.raises(TypeError):
        intersection(A, B)


#############################
## Cartesian Product Tests ##
#############################
# positive tests: what should happen
def test_cartesian_product_positive() -> None:
    # Function inputs
    A: set[int] = {1, 2}
    B: set[str] = {"a", "b"}

    # Expected output
    expected: set[tuple] = {(1, "a"), (1, "b"), (2, "a"), (2, "b")}

    # Assert that the cartesian_product function works correctly
    assert cartesian_product(A, B) == expected


# negative tests: what should not happen
def test_cartesian_product_negative() -> None:
    # Function inputs
    A = {1}
    B = {2}

    # Incorrect expected output
    incorrect_result: set[tuple] = {
        (1, 1)
    }  # This is incorrect because it should be {(1, 2)}

    # Assert that the cartesian_product function does not work incorrectly
    assert cartesian_product(A, B) != incorrect_result


# TypeError tests: when invalid input should raise an error
def test_cartesian_product_invalid_input_type_1() -> None:
    # one input is the wrong type
    A: str = "not a set"
    B: set[int] = {1, 2}

    with pytest.raises(TypeError):
        cartesian_product(A, B)


def test_cartesian_product_invalid_input_type_2() -> None:
    # one input is the wrong type
    A: set[int] = {1, 2}
    B: str = "not a set"

    with pytest.raises(TypeError):
        cartesian_product(A, B)


def test_cartesian_product_output_type() -> None:
    # Function inputs
    A: set[int] = {1, 2}
    B: set[str] = {"a", "b"}

    # Call the cartesian_product function
    result = cartesian_product(A, B)

    # Check that the result is a set
    assert isinstance(result, set)

    # Check that all elements are tuples
    for item in result:
        assert isinstance(item, tuple)

    # Check that all tuples have the correct length
    for item in result:
        assert len(item) == 2, f"Expected tuple of length 2, got {item}"
