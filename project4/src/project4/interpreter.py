"""Interpreter for Datalog programs.

Provides an interpreter interface for interpreting Datalog
programs using relational algebra.
"""

from typing import Iterator

from project4.datalogprogram import DatalogProgram, Predicate, Rule
from project4.relation import Relation


class Interpreter:
    """Interpreter class for Datalog.

    Defines the interface, and a place for the implementation, for interpreting
    Datalog programs. The interpreter must be implemented using relational algebra,
    so new attributes must be added to track the named relations in the Datalog
    program during the lifetime of the interpreter.

    Attributes:
        datalog (DatalogProgram): The Datalog program to interpret.
    """

    def __init__(self, datalog: DatalogProgram) -> None:
        self.datalog = datalog
        self.relations: dict[str, Relation] = {}

    def eval_schemes(self) -> None:
        """Evaluate the schemes in the Datalog program.

        Create, and store in the interpreter, a relation for each scheme
        in the Datalog program. The _name_ of the scheme must be stored
        separate from the relation since the `Relation` type has no name
        attribute.
        """
        for scheme in self.datalog.schemes:
            header: list[str] = []
            for parameter in scheme.parameters:
                header.append(parameter.value)
            self.relations[scheme.name] = Relation(header, set())

    def eval_facts(self) -> None:
        """Evaluate the facts in the Datalog program.

        Create, and store in the appropriate relation belonging to the
        interpreter, a tuple for each fact in the Datalog program.
        """
        for fact in self.datalog.facts:
            relation: Relation = self.relations[fact.name]
            relation.add_tuple(tuple(i.value for i in fact.parameters))

    def eval_queries(self) -> Iterator[tuple[Predicate, Relation]]:
        """Yield each query and resulting relation from evaluation."

        For each query in the Datalog program, evaluate the query to get a
        resulting relation that is the answer to the query, and then yield
        the resulting `(query, relation)` tuple.

        Returns:
            out (tuple[Predicate, Relation]): An iterator to a tuple where the
            first element is the predicate for the query and the second element
            is the relation for the answer.
        """
        results: list[tuple[Predicate, Relation]] = []

        for query in self.datalog.queries:
            relation = self.relations[query.name]
            new_relation = relation

            for i, param in enumerate(query.parameters):
                if param.is_string():
                    new_relation = new_relation.select_eq_lit(
                        new_relation.header[i], param.value
                    )

            seen_vars: dict[str, int] = {}
            for i, param in enumerate(query.parameters):
                if not param.is_string():
                    if param.value in seen_vars:
                        new_relation = new_relation.select_eq_col(
                            new_relation.header[i],
                            new_relation.header[seen_vars[param.value]],
                        )
                    else:
                        seen_vars[param.value] = i

            project_columns: list[str] = []
            to: list[str] = []
            seen: set[str] = set()

            for i, param in enumerate(query.parameters):
                if not param.is_string() and param.value not in seen:
                    project_columns.append(new_relation.header[i])
                    to.append(param.value)
                    seen.add(param.value)

            if project_columns:
                new_relation = new_relation.project(project_columns)
                new_relation = new_relation.rename(to)

            results.append((query, new_relation))

        return iter(results)
        # just wanted to keep this because I worked hard and even without relational algebra I got to 80
        # results = []
        # for query in self.datalog.queries:
        #     relation: Relation = self.relations[query.name]

        #     index_value = {}
        #     header = []
        #     variable_index = []

        #     for i, parameter in enumerate(query.parameters):
        #         if not parameter.is_id():
        #             index_value[i] = parameter.value
        #         else:
        #             variable_index.append(i)
        #             header.append(parameter.value)

        #     new_tuples = set()
        #     for t in relation.set_of_tuples:
        #         b = True

        #         for i, value in index_value.items():
        #             if t[i] != value:
        #                 b = False
        #                 break

        #         if b:
        #             new_tuples.add(tuple(t[i] for i in variable_index))

        #     new_relation = Relation(header, new_tuples)
        #     results.append((query, new_relation))
        # return iter(results)

    def eval_rules(self) -> Iterator[tuple[Relation, Rule, Relation]]:
        """Yield each _before_ relation, rule, and _after_ relation from evaluation.

        For each rule in the Datalog program, yield as a tuple the relation associated
        with the rule before evaluating the rule one time, the rule itself, and then
        the resulting relation after evaluating the rule one time. This process
        should repeat until the associated relations stop changing.
        All the generated facts should be stored in the appropriate relation
        in the interpreter.

        For example, given `rule_a` for relation `A`, `rule_b` for
        relation `B`, and that it takes three evaluations to see no change, then
        `eval_rules` should:

            yield((A_0, rule_a, A_1))
            yield((B_0, rule_b, B_1))
            yield((A_1, rule_a, A_2))
            yield((B_1, rule_b, B_2))
            yield((A_2, rule_a, A_3))
            yield((B_2, rule_b, B_3))

        Here `A_0` is the initial relation for `A`, `A_1` is the relation after evaluating
        `rule_a` on `A_0` etc. The same for `B`. The iteration stops because `A_2 == A_3` and
        `B_2 == B_3`.

        Returns:
            out (Iterator[tuple[Relation, Rule, Relation]]): An iterator to a tuple where the
                first element is the relation before rule evaluation, the second element is
                the rule associated with the relation, and the third element is the relation
                resulting from the rule evaluation.
        """
        changed = True  # for fixed point algorithm
        passes = 0

        while True:
            changed = False
            yield_results: list[tuple[Relation, Rule, Relation]] = []

            for rule in self.datalog.rules:
                pred_relation_list: list[Relation] = []  # list of predicate relations

                for pred in (
                    rule.predicates
                ):  # this should get all of the relations that the rule mentions
                    # evaluate pred - first rename headers to match
                    existing_relation = self.relations[pred.name]

                    pred_header = [str(param) for param in pred.parameters]
                    current_relation = existing_relation.rename(pred_header)

                    # then we select the right columns and rows
                    for i, param in enumerate(pred.parameters):
                        # check for constants the same way as eval_queries for select_lit
                        if param.is_string():
                            literal = param.value
                            current_relation = current_relation.select_eq_lit(
                                pred_header[i], literal
                            )

                    # check for duplicates the same way as eval_queries for select_col
                    seen_vars: dict[str, int] = {}
                    for i, param in enumerate(pred.parameters):
                        if not param.is_string():
                            if param.value in seen_vars:
                                current_relation = current_relation.select_eq_col(
                                    pred_header[i], pred_header[seen_vars[param.value]]
                                )
                            else:
                                seen_vars[param.value] = i

                    pred_relation_list.append(current_relation)

                # join all of my predicate relations together
                final_pred_relation = pred_relation_list[0]
                for pred_relation in pred_relation_list[1:]:
                    final_pred_relation = final_pred_relation.join(pred_relation)

                # get our header to project and then project also reorders
                header = [str(param) for param in rule.head.parameters]
                final_relation = final_pred_relation.project(header)

                # get correct header for renaming and then rename
                renamed_header = self.relations[rule.head.name].header
                final_relation = final_relation.rename(renamed_header)

                # this is so we can check for changes and I made a copy method because it wasn't working without
                previous_relation = self.relations[rule.head.name].copy()

                # union together
                new_relation = previous_relation.union(final_relation)
                self.relations[rule.head.name] = new_relation

                yield_results.append((previous_relation, rule, new_relation))

                if previous_relation != new_relation:
                    # fixed point, keep going
                    changed = True
            # just as a note if anyone reads this I spent longer on formatting this for the tests correctly than on actually writing this :(
            passes += 1
            for y in yield_results:
                yield y

            # ends the fixed point algorithm
            if not changed:
                break

    def eval_rules_optimized(self) -> Iterator[tuple[Relation, Rule, Relation]]:
        """Yield each _before_ relation, rule, and _after_ relation from optimized evaluation.

        This function is the same as the `eval_rules` function only it groups rules by strongly
        connected components (SCC) in the dependency graph from the rules in the Datalog
        program. So given the first SCC is with `rule_a` for relation `A`, `rule_b` for
        relation `B`, that takes three evaluations to see no change, and the second SCC with
        `rule_c for relation C that takes two evaluations to see no change, then
        `eval_rules_opt` should:

            yield((A_0, rule_a, A_1))
            yield((B_0, rule_b, B_1))
            yield((A_1, rule_a, A_2))
            yield((B_1, rule_b, B_2))
            yield((A_2, rule_a, A_3))
            yield((B_2, rule_b, B_3))
            yield((C_0, rule_c, C_1))
            yield((C_1, rule_c, C_2))

        Here `A_0` is the initial relation for `A`, `A_1` is the relation after evaluating
        `rule_a` on `A_0` etc. The same for `B` and `C`. The iteration on the first SCC stops
        because `A_2 == A_3` and `B_2 == B_3`. After the iteration for the second SCC starts
        and stops after two iterations when `C_1 == C_2`.

        Returns:
            out (Iterator[tuple[Relation, Rule, Relation]]): An iterator to a tuple where the
                first element is the relation before rule evaluation, the second element is the
                rule associated with the relation, and the third element is the relation resulting
                from the rule evaluation.
        """
        raise NotImplementedError

    def get_rule_dependency_graph(self) -> dict[int, list[int]]:
        """Return the rule dependency graph.

        Computes and returns the graph formed by dependencies between rules.
        The graph is used to compute strongly connected components of rules
        for optimized rule evaluation.

        Rules are zero-indexed so the first rule in the Datalog program is `0`,
        the second rules is `1`, etc. A return of `{0 : [0, 1], 1 : [2]}`
        means that `0` has edges to `0` and `1`, and `1` has an edge to `2`.

        Returns:
            out: A map with an entry for each rule and the associated rules connected to it.
        """
        raise NotImplementedError
