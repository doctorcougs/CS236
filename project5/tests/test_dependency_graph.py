# type: ignore
"""Tests for the dependency graph and SCC computation"""

from project5.datalogprogram import DatalogProgram, Parameter, Predicate, Rule
from project5.interpreter import (
    Interpreter,
    get_post_order_vector,
    get_reverse_graph,
    get_sccs,
)

# ---------------------------------------------------------------------------
# Helper to build a minimal DatalogProgram for dependency-graph tests
# ---------------------------------------------------------------------------


def make_program_with_rules(rules: list[Rule]) -> DatalogProgram:
    """Create a DatalogProgram with only the given rules.

    We build schemes just so the program is well-formed.
    Facts and queries are empty because they are not needed
    for dependency-graph testing.
    """
    schemes: list[Predicate] = []

    # For each rule head, create a simple scheme with one ID parameter
    seen_heads: set[str] = set()
    for rule in rules:
        if rule.head.name not in seen_heads:
            seen_heads.add(rule.head.name)
            schemes.append(
                Predicate(rule.head.name, [Parameter.id("X")]),
            )

    return DatalogProgram(
        schemes=schemes,
        facts=[],
        rules=rules,
        queries=[],
    )


# ---------------------------------------------------------------------------
# Tests for Interpreter.get_rule_dependency_graph
# ---------------------------------------------------------------------------


def test_dependency_graph_simple_chain() -> None:
    """
    Rules:
      R0: P(X) :- Q(X).
      R1: Q(X) :- R(X).
      R2: R(X) :- S(X).   (S only from facts, no rule head)

    Expected dependency edges:
      0 -> 1
      1 -> 2
      2 -> (none)
    """
    r0 = Rule(
        Predicate("P", [Parameter.id("X")]),
        [Predicate("Q", [Parameter.id("X")])],
    )
    r1 = Rule(
        Predicate("Q", [Parameter.id("X")]),
        [Predicate("R", [Parameter.id("X")])],
    )
    r2 = Rule(
        Predicate("R", [Parameter.id("X")]),
        [Predicate("S", [Parameter.id("X")])],
    )

    dp = make_program_with_rules([r0, r1, r2])
    interp = Interpreter(dp)

    graph = interp.get_rule_dependency_graph()

    assert graph == {
        0: [1],
        1: [2],
        2: [],
    }


def test_dependency_graph_multiple_producers_and_self_loop() -> None:
    """
    Rules:
      R0: P(X) :- Q(X).
      R1: Q(X) :- P(X).
      R2: P(X) :- P(X).

    Heads:
      P produced by R0 and R2
      Q produced by R1

    Dependencies:
      R0 uses Q -> depends on R1 -> 0 -> 1
      R1 uses P -> depends on R0 and R2 -> 1 -> 0, 2
      R2 uses P -> depends on R0 and R2 -> 2 -> 0, 2
    """
    r0 = Rule(
        Predicate("P", [Parameter.id("X")]),
        [Predicate("Q", [Parameter.id("X")])],
    )
    r1 = Rule(
        Predicate("Q", [Parameter.id("X")]),
        [Predicate("P", [Parameter.id("X")])],
    )
    r2 = Rule(
        Predicate("P", [Parameter.id("X")]),
        [Predicate("P", [Parameter.id("X")])],
    )

    dp = make_program_with_rules([r0, r1, r2])
    interp = Interpreter(dp)

    graph = interp.get_rule_dependency_graph()

    assert graph == {
        0: [1],
        1: [0, 2],
        2: [0, 2],
    }


def test_dependency_graph_alpha_bravo_charlie_example() -> None:
    """
    Matches the Alpha/Bravo/Charlie example you had earlier:

      R0: Alpha(...) :- A, A, A, A, A.
      R1: Alpha(...) :- A, A, B, A, A.
      R2: Alpha(...) :- A, B, A, B, A.
      R3: Bravo(...) :- Alpha(...), A.
      R4: Charlie(...) :- Bravo(...), B.

    Heads:
      Alpha: R0, R1, R2
      Bravo: R3
      Charlie: R4

    Dependencies:
      R0, R1, R2 -> none (only A and B from facts)
      R3 uses Alpha -> depends on R0, R1, R2
      R4 uses Bravo -> depends on R3
    """
    # For schemes, we don't care about exact parameter names as long as
    # the predicate names are correct.
    alpha_head = Predicate(
        "Alpha",
        [
            Parameter.id("A"),
            Parameter.id("B"),
            Parameter.id("C"),
            Parameter.id("D"),
            Parameter.id("E"),
        ],
    )
    bravo_head = Predicate(
        "Bravo",
        [
            Parameter.id("E"),
            Parameter.id("D"),
            Parameter.id("C"),
            Parameter.id("B"),
            Parameter.id("A"),
        ],
    )
    charlie_head = Predicate(
        "Charlie",
        [
            Parameter.id("E"),
            Parameter.id("D"),
            Parameter.id("C"),
            Parameter.id("B"),
            Parameter.id("A"),
        ],
    )

    r0 = Rule(alpha_head, [Predicate("A", [Parameter.id("A")])])
    r1 = Rule(
        alpha_head,
        [Predicate("A", [Parameter.id("A")]), Predicate("B", [Parameter.id("C")])],
    )
    r2 = Rule(
        alpha_head,
        [Predicate("B", [Parameter.id("B")]), Predicate("A", [Parameter.id("A")])],
    )
    r3 = Rule(
        bravo_head,
        [Predicate("Alpha", [Parameter.id("A")]), Predicate("A", [Parameter.id("B")])],
    )
    r4 = Rule(
        charlie_head,
        [Predicate("Bravo", [Parameter.id("A")]), Predicate("B", [Parameter.id("D")])],
    )

    dp = make_program_with_rules([r0, r1, r2, r3, r4])
    interp = Interpreter(dp)

    graph = interp.get_rule_dependency_graph()

    assert graph == {
        0: [],
        1: [],
        2: [],
        3: [0, 1, 2],
        4: [3],
    }


# ---------------------------------------------------------------------------
# Tests for get_reverse_graph
# ---------------------------------------------------------------------------


def test_reverse_graph_basic() -> None:
    """
    Original:
      0 -> 1, 2
      1 -> 2
      2 -> ()

    Reversed:
      0 <- ()
      1 <- 0
      2 <- 0, 1
    """
    graph = {
        0: [1, 2],
        1: [2],
        2: [],
    }

    reversed_graph = get_reverse_graph(graph)

    assert reversed_graph == {
        0: [],
        1: [0],
        2: [0, 1],
    }


def test_reverse_graph_with_isolated_and_self_loop() -> None:
    """
    Original:
      0 -> 0, 1
      1 -> ()
      2 -> ()   (isolated)

    Reversed:
      0 <- 0
      1 <- 0
      2 <- ()
    """
    graph = {
        0: [0, 1],
        1: [],
        2: [],
    }

    reversed_graph = get_reverse_graph(graph)

    assert reversed_graph == {
        0: [0],
        1: [0],
        2: [],
    }


# ---------------------------------------------------------------------------
# Tests for get_post_order_vector
# ---------------------------------------------------------------------------


def test_post_order_no_edges() -> None:
    """
    Graph with no edges should just finish each vertex in sorted order.
    """
    graph = {
        0: [],
        1: [],
        2: [],
    }

    post = get_post_order_vector(graph)

    # DFS visits 0,1,2 in that order, each finishes immediately.
    assert post == [0, 1, 2]


def test_post_order_chain() -> None:
    """
    0 -> 1 -> 2
    DFS starting at 0 finishes in the order 2,1,0.
    """
    graph = {
        0: [1],
        1: [2],
        2: [],
    }

    post = get_post_order_vector(graph)

    assert post == [2, 1, 0]


# ---------------------------------------------------------------------------
# Tests for get_sccs
# ---------------------------------------------------------------------------


def test_sccs_two_components_cycle_and_singleton() -> None:
    """
    Graph:
      0 -> 1
      1 -> 0, 2
      2 -> ()

    SCCs:
      {0,1} and {2}

    With the particular Kosaraju + ordering in get_sccs, we expect
    that it yields [2] first, then [0,1].
    """
    graph = {
        0: [1],
        1: [0, 2],
        2: [],
    }

    scc_list = list(get_sccs(graph))

    # First SCC is the singleton {2}, second is the cycle {0,1}
    assert len(scc_list) == 2
    assert scc_list[0] == [2]
    assert scc_list[1] == [0, 1]
