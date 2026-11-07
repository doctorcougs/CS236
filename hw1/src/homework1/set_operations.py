# src/set_operations.py
from typing import Any


# ✅ Correct implementation
def union(a: set[int], b: set[int]) -> set[int]:
    """
    Input: two sets of integers
    Output: a set of integers that is the union of the two sets
    """
    # Check if inputs are sets
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError("Arguments must be sets")
    # Check if all set elements are integers
    if not all(isinstance(x, int) for x in a | b):
        raise TypeError("All elements of the sets must be integers")
    # Return the union of the two sets
    return a | b


# ❌ Incorrect implementation (uses intersection)
def intersection(a: set[int], b: set[int]) -> set[int]:
    """
    Input: two sets of integers
    Output: a set of integers that is the intersection of the two sets
    """
    # Check if inputs are sets
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError("Arguments must be sets")
    # Check if all set elements are integers
    if not all(isinstance(x, int) for x in a | b):
        raise TypeError("All elements of the sets must be integers")

    # Return the intersection of the two sets
    # Note: This implementation is incorrect because it uses union instead of intersection
    # It should return the intersection of the two sets
    return a & b


# ❌ Incorrect implementation (repeats a)
def cartesian_product(a: set[Any], b: set[Any]) -> set[tuple[Any, Any]]:
    """
    Input: two sets of any type
    Output: a set of tuples representing the Cartesian product of the two sets
    """
    # Check if inputs are sets
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError("Arguments must be sets")

    # Return the Cartesian product of the two sets
    # Note: This implementation is incorrect because it uses the same set for both elements
    # It should use 'b' for the second element of the tuple
    return {(x, y) for x in a for y in b}
