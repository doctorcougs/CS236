"""Functions for output matching in pass-off tests."""

from functools import reduce

from project3.datalogprogram import Predicate
from project3.relation import Relation, RelationTuple


def _is_only_strings(predicate: Predicate) -> bool:
    """True iff every parameter in the predicate is of type string."""
    return reduce(
        lambda is_only_string, parameter: is_only_string and parameter.is_string(),
        predicate.parameters,
        True,
    )


def _tuple_to_str(header: list[str], r: RelationTuple) -> str:
    """The string representation of a tuple given its associated header."""
    assert len(header) == len(r)
    entries = [f"{i[0]}={i[1]}" for i in zip(header, r)]
    return ", ".join(entries)


def query_report(query: Predicate, answer: Relation) -> str:
    """The string representation of a query report.

    Here the format is the query followed by yes/no with how
    many tuples match the query. The printing of the tuples
    includes the header information as in the below.

    SK(A,B)? Yes(3)
      A='a', B='b'
      A='a', B='c'
      A='b', B='c'
    """
    tuples: list[RelationTuple] = sorted(answer.set_of_tuples)
    if len(tuples) == 0:
        return f"{query}? No"

    if _is_only_strings(query):
        return f"{query}? Yes({len(tuples)})"

    entries = [_tuple_to_str(answer.header, row) for row in tuples]
    entries_str = "\n  ".join(entries)
    return f"{query}? Yes({len(tuples)})\n  {entries_str}"
