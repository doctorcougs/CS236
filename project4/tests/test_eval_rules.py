from project4.datalogprogram import DatalogProgram, Parameter, Predicate, Rule
from project4.interpreter import Interpreter


def test_eval_rules_simple_copy():
    p_scheme = Predicate("p", [Parameter.id("X")])
    p_fact1 = Predicate("p", [Parameter.string("'1'")])
    p_fact2 = Predicate("p", [Parameter.string("'2'")])

    q_scheme = Predicate("q", [Parameter.id("X")])
    rule = Rule(
        Predicate("q", [Parameter.id("X")]), [Predicate("p", [Parameter.id("X")])]
    )

    dp = DatalogProgram(
        schemes=[p_scheme, q_scheme], facts=[p_fact1, p_fact2], rules=[rule], queries=[]
    )

    Interp = Interpreter(dp)
    Interp.eval_schemes()
    Interp.eval_facts()

    results = list(Interp.eval_rules())
    assert len(results) == 2

    before1, rule1, after1 = results[0]
    before2, rule2, after2 = results[1]

    assert before1.set_of_tuples == set()
    assert after1.set_of_tuples == {("'1'",), ("'2'",)}

    assert before2.set_of_tuples == after2.set_of_tuples


def test_eval_rules_no_op():
    p_scheme = Predicate("p", [Parameter.id("X")])
    q_scheme = Predicate("q", [Parameter.id("X")])

    p_fact = Predicate("p", [Parameter.string("'1'")])

    rule = Rule(
        Predicate("q", [Parameter.id("Y")]), [Predicate("p", [Parameter.id("Y")])]
    )

    dp = DatalogProgram(
        schemes=[p_scheme, q_scheme], facts=[p_fact], rules=[rule], queries=[]
    )

    Interp = Interpreter(dp)
    Interp.eval_schemes()
    Interp.eval_facts()
    results = list(Interp.eval_rules())

    assert len(results) == 2

    before1, rule1, after1 = results[0]
    before2, rule2, after2 = results[1]

    assert before1.set_of_tuples == set()
    assert after1.set_of_tuples == {("'1'",)}

    assert before2.set_of_tuples == after2.set_of_tuples


def test_eval_rules_chain():  # AI
    # p('1'), r('1','2')
    p_scheme = Predicate("p", [Parameter.id("X")])
    r_scheme = Predicate("r", [Parameter.id("X"), Parameter.id("Y")])
    q_scheme = Predicate("q", [Parameter.id("Z")])

    p_fact = Predicate("p", [Parameter.string("'1'")])
    r_fact = Predicate("r", [Parameter.string("'1'"), Parameter.string("'2'")])

    # q(Z) :- p(X), r(X,Z)
    rule = Rule(
        Predicate("q", [Parameter.id("Z")]),
        [
            Predicate("p", [Parameter.id("X")]),
            Predicate("r", [Parameter.id("X"), Parameter.id("Z")]),
        ],
    )

    dp = DatalogProgram(
        schemes=[p_scheme, r_scheme, q_scheme],
        facts=[p_fact, r_fact],
        rules=[rule],
        queries=[],
    )

    Interp = Interpreter(dp)
    Interp.eval_schemes()
    Interp.eval_facts()
    results = list(Interp.eval_rules())

    # Two passes, first adds '2'
    assert len(results) == 2
    assert results[0][2].set_of_tuples == {("'2'",)}
    assert results[1][0].set_of_tuples == results[1][2].set_of_tuples


def test_eval_rules_two_rules():  # AI
    # a('1')
    a_scheme = Predicate("a", [Parameter.id("X")])
    b_scheme = Predicate("b", [Parameter.id("X")])

    a_fact = Predicate("a", [Parameter.string("'1'")])

    # b(X) :- a(X)
    # a(X) :- b(X)
    r1 = Rule(
        Predicate("b", [Parameter.id("X")]), [Predicate("a", [Parameter.id("X")])]
    )
    r2 = Rule(
        Predicate("a", [Parameter.id("X")]), [Predicate("b", [Parameter.id("X")])]
    )

    dp = DatalogProgram(
        schemes=[a_scheme, b_scheme], facts=[a_fact], rules=[r1, r2], queries=[]
    )

    Interp = Interpreter(dp)
    Interp.eval_schemes()
    Interp.eval_facts()

    results = list(Interp.eval_rules())

    # 2 rules run per pass, and two passes occur
    assert len(results) == 4

    # first pass:
    #   r1 adds b('1')
    #   r2 adds nothing (since a already has '1')
    first_r1 = results[0]
    assert first_r1[2].set_of_tuples == {("'1'",)}

    # second pass:
    #   no rule adds anything
    assert results[-1][0].set_of_tuples == results[-1][2].set_of_tuples
