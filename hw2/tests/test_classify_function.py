from homework2.classify_function import classify_function


# Test for a valid function
def test_classify_function_function() -> None:
    # Inputs
    f = {(1, 'a'), (2, 'b'), (3, 'c')}
    domain = {1, 2, 3}
    codomain = {'a', 'b', 'c'}

    # Expected output
    expected = "function"

    # Assert that actual output equals expected output
    assert classify_function(f, domain, codomain) == expected

# Test for a partial function
def test_classify_function_partial_function() -> None:
    # Inputs
    f = {(1, 'a'), (3, 'c')}
    domain = {1, 2, 3}
    codomain = {'a', 'b', 'c'}

    # Expected output
    expected = "partial function"

    # Assert that actual output equals expected output
    assert classify_function(f, domain, codomain) == expected

# Test for not a function (duplicate keys with different values)
def test_classify_function_not_a_function() -> None:
    # Inputs
    f = {(1, 'a'), (1, 'b'), (2, 'c')}  # Multiple mappings for 1
    domain = {1, 2}
    codomain = {'a', 'b', 'c'}

    # Expected output
    expected = "not a function"

    # Assert that actual output equals expected output
    assert classify_function(f, domain, codomain) == expected

# Edge case: empty domain and empty mapping
def test_classify_function_empty_domain_and_mapping() -> None:
    # Inputs
    f = set()
    domain = set()
    codomain = {'a', 'b'}

    # Expected output
    expected = "function"

    # Assert that actual output equals expected output
    assert classify_function(f, domain, codomain) == expected

# Edge case: empty mapping but non-empty domain (partial function)
def test_classify_function_empty_mapping_nonempty_domain() -> None:
    # Inputs
    f = set()
    domain = {1, 2, 3}
    codomain = {'a', 'b', 'c'}

    # Expected output
    expected = "partial function"

    # Assert that actual output equals expected output
    assert classify_function(f, domain, codomain) == expected

# Edge case: empty codomain with empty domain and mapping (function)
def test_empty_codom_and_empty_domain_function() -> None:
    # Inputs
    f = set()
    domain  = set()
    codomain = set()

    # Expected output
    expected = "function"

    # Assert that actual output equals expected output
    assert classify_function(f, domain, codomain) == expected

# Edge case: empty codomain with non-empty domain and empty mapping (partial function)
def test_empty_codom_nonempty_domain_partial_function() -> None:
    # Inputs
    f = set()
    domain = {1, 2}
    codomain = set()

    # Expected output
    expected = "partial function"

    # Assert that actual output equals expected output
    assert classify_function(f, domain, codomain) == expected