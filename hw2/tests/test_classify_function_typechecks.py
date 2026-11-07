import pytest

from homework2.classify_function import classify_function

#########################
## Type Checking Tests ##
#########################

# ⚠️ Type-check: input key not in domain
def test_classify_function_key_not_in_domain() -> None:
    # Inputs
    f = {(4, 'a')}  # 4 not in domain
    domain = {1, 2, 3}
    codomain = {'a', 'b', 'c'}

    # Expect a TypeError
    with pytest.raises(TypeError):
        classify_function(f, domain, codomain)

# ⚠️ Type-check: output value not in codomain
def test_classify_function_value_not_in_codomain() -> None:
    # Inputs
    f = {(1, 'x')}  # 'x' not in codomain
    domain = {1}
    codomain = {'a', 'b', 'c'}

    # Expect a TypeError
    with pytest.raises(TypeError):
        classify_function(f, domain, codomain)

# ⚠️ Type-check: domain contains invalid type
def test_classify_function_invalid_domain_type() -> None:
    # Inputs
    f = {(1, 'a')}
    domain = {1, 2, 3.14}  # float is invalid
    codomain = {'a', 'b'}

    # Expect a TypeError
    with pytest.raises(TypeError):
        classify_function(f, domain, codomain)

# ⚠️ Type-check: codomain contains invalid type
def test_classify_function_invalid_codomain_type() -> None:
    # Inputs
    f = {(1, 'a')}
    domain = {1}
    codomain = {'a', None}  # None is invalid

    # Expect a TypeError
    with pytest.raises(TypeError):
        classify_function(f, domain, codomain)

# ⚠️ Type-check: mapping contains invalid tuple value
def test_classify_function_invalid_mapping_type() -> None:
    # Inputs
    f = {(1, 2.71)}  # float is invalid
    domain = {1}
    codomain = {2}

    # Expect a TypeError
    with pytest.raises(TypeError):
        classify_function(f, domain, codomain)
