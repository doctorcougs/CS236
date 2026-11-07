# Project 3

This project uses the instance of the `DatalogProgram` created by the `lexer` and `parser` functions from Project 1 and Project 2. This project has you write an interpreter that will take the `DatalogProgram` instance, represent the `facts` as relations in a relational database, and answer queries when there are no `rules` in the original Datalog Program. Project 3 must
  1. Create a relation for each named scheme in the Datalog program.
  1. Add each fact in the Datalog program to the appropriate relation.
  1. Evaluate each query in the Datalog program and return the answers to each one.
[QUERIES_INTERP.md](docs/QUERIES_INTERP.md) explains each of these steps in detail.

**There is no rule evaluation for project 3.** Anything related to evaluating rules, including the natural join of two relations, is **not a part of project 3.**

The interpreter **must be implemented with relational algebra.** No exceptions will be allowed. Specifically, you must implement the relational operators `project`, `rename`, and `select`.  This is a good opportunity to implement and test the relational operators `reorder`, `union`, `intersection`, and `difference` since (s) these operators are used in Project 4 and (b) this project is easier than Project 4.

**Summary of Documentation**

- [README.md](README.md): describes project logistics
- [QUERIES_INTERP.md](docs/QUERIES_INTERP.md): describes how to use relational operators to interpret queries in Datalog
- [CODE.md](docs/CODE.md): describes the starter code
- [Relational Algebra Operations Examples](docs/Relational_algebra.ipynb) (Jupyter Notebook)
- Lecture notes in [learningsuite.byu.edu](https://learningsuite.byu.edu) and specifically the slides in the lecture _Relational Operators and Project 3_.

**You are strongly encouraged to review the above documentation _before_ proceeding further**.

## Table of Contents
- [Developer Setup](#developer-setup)
- [Project Requirements](#project-requirements)
- [AI Policy for Project 3](#ai-policy-for-project-3)
- [Unit Tests](#unit-tests)
- [Integration Tests (pass-off)](#integration-tests-pass-off)
- [Code Quality](#code-quality)
- [Submission And Grading](#submission-and-grading)
- [Best Practices](#best-practices)

## Developer Setup

The `vscode` extensions for developing Project 3 are already installed as part of Project 0. You should not need to install any new extensions. You do need to set up the project locally on your machine. The below steps outline the process that is similar to what you did in Project 2, emphasizing additional files to copy over.

1. Clone the repository to your machine. Accepting the Project 3 assignment on GitHub classroom creates a repository for your submission. You need to clone that repository to your machine. Copy the URL generated after accepting the assignment and in a terminal on your machine in a sensible location. From an integrated terminal, type `git clone \<URL\>` where `\<URL\>` is the one you copied. Or open a new vscode window, select _Clone Git Repository_, and paste the URL you copied. If you followed the URL to GitHub, then you can recopy the URL using the "<> Code ▼" button.
1. Create and activate a virtual environment in the project directory.  Revisit Project 0 for a reminder on how to create the virtual environment. There is also a _cheat sheet_ at [learningsuite.byu.edu](https://learningsuite.byu.edu) _Content_ &rarr; _Projects_ &rarr; _Projects Cheat Sheet_.
1. Install the project package. **Be sure your virtual environment is active before installing the package!** In a terminal in the virtual environment in the project directory do: `pip install --editable ".[dev]"`. Use `pip3` instead of `pip` if your system requires it.
1. Verify the package installation. From the terminal in which you activated the virtual environment and installed the project package, type `project1` and hit enter. You should see the below output.
    ```
    $ project3
    usage: project3 <input file>
    ```
1. Install `pre-commit` for the project. **Be sure your virtual environment is active before installing pre-commit!**. In a terminal in the virtual environment in the project directory do: `pre-commit install`
1. Verify the `pre-commit` installation. From the terminal in which you installed `pre-commit`, type `pre-commit run --all-files` and hit enter. You should see something like the below at the end of the setup output:
    ```
    $ pre-commit run --all-files
    trim trailing whitespace.................................................Passed
    fix end of files.........................................................Passed
    check yaml...............................................................Passed
    check for added large files..............................................Passed
    CRLF end-lines remover...................................................Passed
    Tabs remover.............................................................Passed
    ruff.....................................................................Passed
    ruff-format..............................................................Passed
    mypy.....................................................................Passed
    ```
1. Verify that tests are ready to run. Open the _Testing Pane_ in VS Code by clicking on the test tube icon. If you see
    ```
    pytest Discovery Error [project-3]
    ```
    then you must open the _Command Palette_ from the _View_ menu, choose `Python: Select Interpreter`, and choose the interpreter for the virtual environment (probably `Python 3.12.5 (.venv)`).
1. **IMPORTANT**: Copy the below files from your solution to Project 2 into the `src/project3/` folder:
    * `datalogprogram.py`
    * `fsm.py`
    * `lexer.py`
    * `parser.py`
The `token.py` file is unchanged here and should not be copied over. None of test files from Project 2 should be copied over either.

**You need to fix all the imports in the copied file to replace `project2` with `project3` in the import path. You also need to make these changes in all the docstring tests. We recommend the use of the search feature in `vscode`, the magnifying class in the sidebar, to search for `project2` in all files.**

## Project Requirements

1. The project must be completed individually -- there is no group work.
1. Project pass-off is on GitHub. You will commit your final solution to the `master` branch of your local repository and then push that commit to GitHub. Multiple commits, and pushes, are allowed. A push triggers a GitHub action that is the auto-grader for pass-off. The TAs look at both the result of the auto-grader on GitHub and your code to determine your final score. Projects that use iteration instead of tail recursion will not be accepted.
1. You must pass all integration tests up to, and including, `tests/test_passoff_80.py` to move on to the next project. Bucket 80 is the minimum functionality to complete the course.
1. You must **_"do the math"_** to write positive and negative tests in `tests/test_relation.py` for the following functions in the `Relation` class in `src/project3/relation.py`. AI may be used to generate the code for the tests once you **_"do the math"_** for the inputs and outputs and write a few examples for the AI to follow using your inputs and outputs. Consider using parameterized tests and try to design your tests using input partitioning using the pattern shown in the Jupyter notebook tutorial. See [AI Policy for Project 3](#ai-policy-for-project-3) for details.
    - `intersection`,
    - `project`,
    - `rename`,
    - `reorder`,
    - `select_eq_col`,
    - `select_eq_lit`, and
    - `union`.
1. You must implement the following functions in the `Relation` class in `src/project3/relation.py`:
    - `intersection` (easy),
    - `project` (hard),
    - `rename` (super easy),
    - `reorder` (hard)
    - `select_eq_col` (moderate),
    - `select_eq_lit` (moderate), and
    - `union` (easy).
1. You must add to the `Interpreter` class in `src/project3/interpreter.py` attributes to represent, or implement, a relational database. A relational database is just a named collection of relations (see [QUERIES_INTERP.md](docs/QUERIES_INTERP.md))
1. You must interpret a Datalog program with relational algebra by implementing the following in the `Interpreter` class in `src/project3/interpreter.py`. The other functions will be implemented in later projects. See [QUERIES_INTERP.md](docs/QUERIES_INTERP.md) for details on each of the required to implement function as well as the docstrings defined for those functions.
    - `eval_schemes`
    - `eval_facts`
    - `eval_queries`
1. You must use [input partitioning](#input-partitioning) to write tests for `eval_queries` using the pattern demonstrated in the Jupyter notebook tutorial. We won't be looking for a perfect partitioning of the input when we grade your tests, but we will be looking to see if you made an effort to generate tests that had good test coverage. After you **do the math** to find inputs for each of the partitions, then you may use AI to generate the code for the actual tests. We suggest that you use a parameterized test.
1. Your code must not report any issues with the following code quality tool run in the integrated `vscode` terminal from the root of the project directory: `pre-commit run --all-files`. This tool includes _type checking_, which means that type annotations are required in your code.

Consider using a branch as you work on your submission so that you can `commit` your work from time to time. Once everything is working, and the auto-grader tests are passing, then you can `merge` your work into your master branch and push it to your GitHub repository. Ask your favorite AI for help learning how to use Git branches for feature development.

## AI Policy for Project 3

Project 3 code is very algorithmic and specific to interpreting Datalog. It does not include repeated code with similar structure that AI can learn, adapt, and repeat. As such, you are expected to write all the implementation code in the `Relation` class and `Interpreter` class without AI assist.

AI may be used to help generate code for tests **after you "Do the math" to figure out the input and expected output**. In this application, you figure out the computation with the math, and the AI then generates the test code for your given input and output relations.

We recommend that the test code for `eval_queries` be parameterized since the test for each input is the same while there should be least one test for each [input partition](#input-partitioning).


## Unit Tests

Similar to Project 2, you are required to "_do the math_" to write positive and negative unit tests for all of the relational algebra operators. The `tests/test_relation.py` file already includes some tests related to the starter code as starting point for positive

See the [AI Policy for Project 3](#ai-policy-for-project-3) for instructions on when to use and not use AI in generating tests.

## Integration Tests (pass-off)

**The pass-off test structure has changed.** All the primary tests are in a single file: `tests/test-passoff.py`. Running individual tests is the same using either `pytest` directly or the testing pane in vscode (**recommended**). As before, the `xx` on each bucket denotes the available points for passing the tests in that bucket. The value of each test in each bucket is uniform: _points-for-bucket/number-of-tests-in-bucket_. Bucket 80 is the minimum requirement to pass the course.

## Input Partitioning

Input partitioning, which is illustrated in the Jupyter notebook tutorial, is a generalization of _negative_ and _positive_ tests. The idea is to figure out the different types of output that can be generated, and then partition the input space according to those outputs.

For example, consider a helper function $\mathtt{eval\_query}: \mathtt{ParameterList} \times \mathtt{Relation} \rightarrow \mathtt{Relation}$ that is called by `Interpreter::eval_queries` for each query in the Datalog program. Here, if the Datalog program had the query `f(x,y)?`, then `eval_queries` would call `eval_query([x, y], self.db[f])` to interpret the query: the first parameter is the parameter list from the input predicate and the second parameter is the relation for `f` from the database. The return from the function is the relation resulting from the query.

[QUERIES_INTERP.md](docs/QUERIES_INTERP.md) defines different types of output that can be generated by a query:
  * If `eval_query` returns an empty relation, then the output is **No**.
  * If the query is `f('1')` and `eval_query` returns a non-empty relation, then the output is **Yes**.
  * If the query is `f(x)` and `eval_query` returns a non-empty relation, then the output is **Yes(n)** where $n$ is the number of tuples in the relation.

These different types of output caused by `eval_query` can be used to partition the input space. Here we have identified three partitions which means that we want to find an input in each partition of the input space that belongs to each type of identified output. We would then have three tests to generate each of the three possible outputs.

You can further partition the input space since that will be helpful for covering the behavior of our interpreter. For example, should you create an input partition for queries that change the number of attributes in the resulting relation? As another example, should you create an input partition for queries that have a mix of STRING and ID types in the parameter list?

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

Here is the suggested order for Project 3:

1. Read the code and order in your mind what has been provided, how it works, and what you need to implement -- **don't skip this step**.
1. For each required function in `Relation`:

    1. Write a negative test that fails.
    1. Write code to pass the negative test.
    1. Write a positive test that fails.
    1. Write code to pass the positive test.
    1. Make a good faith effort to partition the input, do the math on the resulting partition, and write parameterized tests using the input partition
    1. Modify your code to pass the parameterized tests

1. For each required function in `Interpreter`:

    1. Write a positive test that fails.
    1. Write code to pass the positive test.
    1. Make a good faith effort to partition the input, do the math on the resulting partition, and write parameterized tests using the input partition
    1. Modify your code to pass the parameterized tests

1. Run the pass-off tests -- debug as needed.


### Branches

Consider using a branch as you work on your submission so that you can `commit` your work from time to time. Once everything is working, and the auto-grader tests are passing, then you can `merge` your work into your master branch and push it to your GitHub repository. Ask your favorite search engine or LLM for help learning how to use Git feature branches.
