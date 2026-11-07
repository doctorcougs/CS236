def classify_function(
    mapping: set[tuple[int | str, int | str]],
    domain: set[int | str],
    codomain: set[int | str]
) -> str:
    """
    Classifies the mapping as 'function', 'partial function', or 'not a function'
    based on the provided domain and codomain.

    Args:
        mapping (set[tuple[int | str, int | str]]): A set of ordered pairs (input, output).
        domain (set[int | str]): The full set of possible inputs.
        codomain (set[int | str]): The full set of possible outputs.

    Returns:
        str: 'function' if the mapping is a function, 
             'partial function' if it is a partial function,
             'not a function' if it does not satisfy the criteria of a function.
    """
    for tpl in mapping:
        if tpl[0] not in domain:
            raise TypeError
        if tpl[1] not in codomain:
            raise TypeError
    for i in domain:
        if not isinstance(i, (int, str)):
            raise TypeError
    for i in codomain:
        if not isinstance(i, (int, str)):
            raise TypeError
    input_set = set()
    for tpl in mapping:
        if (tpl[0] in input_set):
            return "not a function"
        input_set.add(tpl[0])
    if (len(input_set) != len(domain)):
        return "partial function"
    return "function"

    # raise NotImplementedError("Function not yet implemented.")
