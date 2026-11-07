# Project 4

This project uses the `lexer` and `parser` functions from Project 1 and Project 2 to get an instance of a `DatalogProgram`. It also uses the `Interpreter.eval_schemes`, `Interpreter.eval_facts`, and `Interpreter.eval_queries` from Project 3. Project 4 must evaluate the rules in the Datalog program to add new facts to relations that exist in the database. This will be done by implementing the `Interpreter.eval_rule` function according to the algorithm specified in [RULE_INTERP.md](docs/RULES_INTERP.md).

You will write three algorithms (and necessary helper functions) for this Project:
- The algorithm for natural join
- The algorithm for rule evaluation
- The code for the fixed point algorithm
Each of these algorithms is described in [RULE_INTERP.md](docs/RULES_INTERP.md). A step-by-step example of using natural join and running the rule evaluation algorithm is given in [Evaluating_Rules_Algorithm.pdf](docs/Evaluating_Rules_Algorithm.pdf).


**Summary of Documentation**

- [README.md](README.md): describes project logistics
- [RULES_INTERP.md](docs/RULES_INTERP.md): describes how to use relational operators to interpret rules in Datalog
  - [JOIN_ALGORITHM.md](docs/JOIN_ALGORITHM.md)
  - [EVALUATING_RULE_ALGORITHM.md](docs/EVALUATE_RULE_ALGORITHM.md)
  - [FIX_POINT_ALGORITHM.md](docs/FIX_POINT_ALGORITHM.md)
- [CODE.md](docs/CODE.md): describes the starter code
- [Evaluating_Rules_Algorithm.pdf](docs/Evaluating_Rules_Algorithm.pdf): gives a step-by-step example of applying natural join and the rule evaluation algorithm for a specific Datalog program.
- Lecture notes in [learningsuite.byu.edu](https://learningsuite.byu.edu) and specifically the slides in the lecture _Project 4 Discussion_.

**You are strongly encouraged to review the above documentation _before_ proceeding further**.

## Table of Contents
- [Project Overview and Major Steps](#project-overview-and-major-steps)
- [Developer Setup](#developer-setup)
- [Project Requirements](#project-requirements)
- [AI Policy for Project 4](#ai-policy-for-project-4)
- [Unit Tests](#unit-tests)
- [Integration Tests (pass-off)](#integration-tests-pass-off)
- [Code Quality](#code-quality)
- [Submission And Grading](#submission-and-grading)
- [Best Practices](#best-practices)

## Project Overview and Major Steps

Project 4 is to write an interpreter that uses relational database operations to evaluate the rules in a Datalog Program. At the end of this project, you will have a fully functional Datalog interpreter. Here is a diagram illustrating the project with a given Datalog program input on the left of the diagram.

<img src="docs/figs/Project 4 Diagram.png" alt="Interpreting Queries" width="915" />

0. **Construct Database**: _already completed in Project 3_, creates the relations for the declared schemes and populates them with the declared facts.
0. **Solve Body Predicates**: this step is first in evaluating the rule in the Datalog program input. Each predicate in the list of predicates for the rule is **interpreted as a query to create a relation**. You should reuse the `Relation.eval_query` function to complete this step.
0. **Join Body Predicates**: every body predicate is combined with one or more join operation(s). You need it implement and test `Relation.join` as part of this project (see [JOIN_ALGORITHM.md](./docs/JOIN_ALGORITHM.md)).
0. **Project and Reorder Columns Specified by Head Predicate**: the head predicate ultimately decides the final relation. The result of the previous step needs to be projected and reordered according to the head predicate (see [EVALUATE_RULE_ALGORITHM.md](./docs/EVALUATE_RULE_ALGORITHM.md)).
0. **Rename with Database for Union Compatibility**: here the relation from the previous step is has its attributes renamed to match the header of the corresponding relation in the database. Renaming the attributes is necessary for the union in the next step to work.
0. **Union with Database Relation**: all the facts generated for the relation from evaluating the rule are added to the corresponding relation in the database with the `Relation.union` operator.
0. **Goto step 0 and Repeat if any Relation Gets New Facts**: we call this a _fix_point_ because we repeat evaluating all rules until no new facts are learned for any relation.
0. **Evaluate Queries**: _already completed in Project 3_ (see [FIX_POINT_ALGORITHM.md](./docs/FIX_POINT_ALGORITHM.md)).

## Developer Setup

The Project 4 setup is the same setup as for Project 3. You must create the virtual environment and activate it, install the package in the virtual environment, install pre-commit, and then copy over files for the solutions to the prior projects.

Here are the files to copy from Project 3 into the `src/project4/` folder:

  * `datalogprogram.py`
  * `fsm.py`
  * `interpreter.py`
  * `lexer.py`
  * `parser.py`
  * `relation.py`
  * `./tests/test_relation.py`
  * `./tests/test_interpreter.py`

The `token.py` file is unchanged here and should not be copied over. Other test files from older projects can be copied as needed.

**You need to fix all the imports in the copied file to replace `project3` with `project4` in the import path. You also need to make these changes in all the docstring tests. We recommend the use of the search feature in `vscode`, the magnifying glass in the sidebar, to search for `project3` in all files.**

## Project Requirements

1. The project must be completed individually -- there is no group work.
1. Project pass-off is on GitHub. You will commit your final solution to the `master` branch of your local repository and then push that commit to GitHub. Multiple commits, and pushes, are allowed. A push triggers a GitHub action that is the auto-grader for pass-off. The TAs look at both the result of the auto-grader on GitHub and your code to determine your final score. _See the cautions in the `#project-3` channel of the class Discord server about how using `fstrings` can cause problems with pass-offs._
1. You must pass all integration tests up to, and including, `tests/test_passoff_80.py` to move on to the next project. Bucket 80 is the minimum functionality to complete the course.
1. You must **use the math you did in Homework 16** to tests in `tests/test_relation.py` for `Relation.join` in `src/project3/relation.py`. AI may be used to generate the code for the tests once you **_"do the math"_** for the inputs and outputs and write a few examples for the AI to follow using your inputs and outputs. See [AI Policy for Project 4](#ai-policy-for-project-4) for details.
1. You must implement `Relation.join` in `src/project3/relation.py`. **AI may not be used for any part of the implementation.**
1. You must **use the math you did in Homework 16** to write tests for `Interpreter.eval_rules` in `src/project3/interpreter.py`. AI may be used to generate the code for the tests once you **_"do the math"_** for the inputs and outputs and write a few examples for the AI to follow using your inputs and outputs. See [AI Policy for Project 4](#ai-policy-for-project-4) for details.
1. You must interpret the Datalog program, including the rules, with relational algebra by implementing `Interpreter.eval_rules` in `src/project3/interpreter.py`. The other functions will be implemented in later projects. See [RULES_INTERP.md](docs/RULES_INTERP.md) for details. You must use `Relation.union` to add facts generated by rules to relations. **AI may not be used for any part of the implementation.**
1. Your code must not report any issues with the following code quality tool run in the integrated `vscode` terminal from the root of the project directory: `pre-commit run --all-files`. This tool includes _type checking_, which means that type annotations are required in your code.
1. Your code must pass each bucket in 150 seconds or less. If you have trouble meeting this requirement, see the FAQ in [RULES_INTERP.md](docs/RULES_INTERP.md).

Consider using a branch as you work on your submission so that you can `commit` your work from time to time. Once everything is working, and the auto-grader tests are passing, then you can `merge` your work into your master branch and push it to your GitHub repository. Ask your favorite AI for help learning how to use Git branches for feature development.

## AI Policy for Project 4

Project 4 code is very algorithmic and specific to interpreting Datalog rules. It does not include repeated code with similar structure that AI can learn, adapt, and repeat. As such, you are expected to write all the implementation code for `Relation.join` class and `Interpreter.eval_rules` class without any AI assistance.

AI may be used to help generate code for tests. You've already done the math in Homework 16, and you use the math from Homework 16 as part of the prompts for AI to generate the test code for your given input and output relations.

We recommend that the test code for `eval_rules` be parameterized since the test for each input is the same while there should be least one test for each input partition. See the Jupyter notebook in the `docs` folder of 3 for a discussion of how to write parameterized tests.

## Unit Tests

You must write tests for `Relation.join` and `Interpreter.eval_rules`. These tests should be derived from input partitioning -- divide the input space into interesting partitions and create a test for each partition. Homework 16 guides you through the process of writing good tests. Note that Homework 16 also guides you through two tests you might use for the fixed point algorithm.

## Integration Tests (pass-off)

All the primary tests are in a single file: `tests/test-passoff.py`. Running individual tests is the same using either `pytest` directly or the testing pane in vscode (**recommended**). As before, the `xx` on each bucket denotes the available points for passing the tests in that bucket. The value of each test in each bucket is uniform: _points-for-bucket/number-of-tests-in-bucket_. Bucket 80 is the minimum requirement to pass the course.

## Code Quality

Pre-commit must run on all the files and report no errors.

## Submission and Grading

The minimum standard for this project is **bucket 80**. That means that if all the tests pass in all buckets up to and including bucket 80, then the next project can be started safely. You can run each bucket from the testing pane or with `pytest` on the command line. Passing everything up to and including `test_passoff_80.py` is the minimum requirement to move on to the next project.

Submit Project 2 for grading by doing the following:

  * Commit your solution on the master branch
  * Push the commit to GitHub -- that should trigger the auto-grader
  * Goto [learningsuite.byu.edu](https://learningsuite.byu.edu) at _Assignments_ &rarr; _Projects_ &rarr; _Project 2_ to submit the following:
    1. Your GitHub ID and Project 2 URL for grading.
    1. A short paragraph outlining (a) how you prompted the AI to generate any code (if you used it) and (b) how you determined the quality and correctness of that code.
    1. A screen shot showing no issues with `pre-commit run --all-files`.
  * Confirm on the GitHub Actions pane that the pass-off tests passed, or alternatively, goto the Project 1 URL, find the green checkmark or red x, and click it to confirm the auto-grader score matches the pass-off results from your system.

### Paragraph on AI

Guidelines for answering

_"A short paragraph outlining (a) how you prompted the AI to generate any code (if you used it) and (b) how you determined the quality and correctness of that code."_

These guidelines give examples from Project 1.

* Brief means no more than 500 words.
* Be specific about what code was generated. _"AI generated FSM code for the following non-terminals: `facts`, etc."_
* Be general about the final form of the prompts used to generate the code and any prompt iteration that was required. _"I gave the AI example code and asked it to create code that matched the pattern, and style, in that example code. I had to revise the prompt to specifically ask it to not generalize an FSM to detect a supplied string."_
* Be specific about how you determined the quality and correctness of generated code. _"A manual visual inspection was sufficient to determine quality and correctness because the generated code was trivial. I also ran the code quality tools on the generated code as a second level check."_
* Be specific about where else AI was leveraged. _"I used AI to breakdown and explain the pseudo-code for the `lexer` algorithm as well as the `FiniteStateMachine` class. AI also provided test inputs for my `STRING` FSM to help debug the apostrophe escape sequence."_
* Be specific about how you used AI to write tests, and how you generated the parse trees necessary for writing tests based on the math.

## Best Practices

Here is the suggested order for Project 4:

1. Figure out the input partition for `Relation.join` -- you must consider at least three unique tests: no shared attributes, attributes shared, and a mix of shared and not shared attributes:

    1. Write a positive test that may fail (should fail the first test because no code has been written and may fail other tests depending on the code written for the first test).
    1. Write code to pass the positive test.

1. Figure out the input partition for `Interpreter.eval_rules` -- as a starting point consider if number of iterations to reach a fix-point matters in testing, if the number of rules being evaluated matters, or if the composition of rules matter:

    1. Write a positive test that may fail (should fail the first test because no code has been written and may fail other tests depending on the code written for the first test).
    1. Write code to pass the positive test.

1. Run the pass-off tests -- debug as needed.

Note that you've "done the math" for writing most of these tests in Homework 16.
