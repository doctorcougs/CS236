# Project 1

Project 1 is to implement a lexer for Datalog programs. A lexer takes as input a Datalog program and turns it onto a sequence of _tokens_ that form the input to a Datalog parser. A token is a representation of a syntactic element of Datalog such as a keyword or an identifier. _Grammars_ are defined over tokens, and grammars are the subject of Project 2, so more on those later in the course. In general though, a **token is a syntactic element of a language** with the characters from the input associated with that element. The task in Project 1 is to take a Datalog program, saved as a `.txt` file, read it into an input stream, run the input stream through the lexer, and output a stream of tokens.
```text
+----------------+
| Datalog program|
+----------------+
        |
        v
+---------------+
| Input Stream  |
+---------------+
        |
        v
    +-------+
    | Lexer |
    +-------+
        |
        v
+---------------+
| Token Stream  |
+---------------+
```

The process to turn an input stream for a Datalog program into a token stream relies on giving the input string to a set of _finite state machines_ (FSMs). Each FSM in the set detects a specific syntactic element of Datalog. The input string is read sequentially by each FSM to see which token should be generated next.  The FSM that reads the longest **prefix** of the input string with the highest priority determines the next token in the token stream. The longest read prefix is then removed from the input string and the process repeats. See [LEXER.md](docs/LEXER.md) for a complete description of the token types and lexer algorithm.

To create an FSM in Python, we define an abstraction of an FSM state named `State`. A `State` is a function that takes as input a single character and returns as output a `tuple[bool, State]` where the `bool` is `True` if the FSM is not able to read any more input and `False` otherwise. The `State` is the _next state_ resulting from reading the input character. A `State` is _accepting_ if it has the string `"accept"` in it's name. You must use this `State` abstraction to implement the FSMs to detect syntactic elements of the Datalog language. See [CODE.md](docs/CODE.md) for a complete overview of the code that you are to use for this project.

Additional resources for understanding tokens, FSMs, the lexer algorithm, and the code provided for this project are provided in the _Lectures: Reading, Topics, and Slides_ section of the _Content_ pane on [learningsuite.byu.edu](https://learningsuite.byu.edu). Look for _FSMs in Project 1_ in the _September Lectures_.  _We strongly recommend that you review that content, including the Jupyter notebook, before proceeding further._

**Summary of Documentation**
- [README.md](README.md): describes project logistics
- [LEXER.md](docs/LEXER.md): describes each token type and gives examples
- [CODE.md](docs/CODE.md): describes the starter code
- Lecture notes and Jupyter notebook on _FSM in Project 1_ in [learningsuite.byu.edu](https://learningsuite.byu.edu)
---

## Table of Contents

- [Developer Setup](#developer-setup)
- [Project Requirements](#project-requirements)
- [Unit Tests](#unit-tests)
- [Integration Tests (pass-off)](#integration-tests-pass-off)
- [Code Quality Tools](#code-quality-tools)
- [Submission and Grading](#submission-and-grading)
- [Best Practices](#best-practices)

## Developer Setup

The `vscode` extensions for developing Project 1 are already installed as part of Project 0. You should not need to install any new extensions. You do need to set up the project locally on your machine. The below steps outline the process.

1. Clone the repository to your machine. Accepting the Project 1 assignment on GitHub classroom creates a repository for your submission. You need to clone that repository to your machine. Copy the URL generated after accepting the assignment and in a terminal on your machine in a sensible location. From an intergrated terminal, type ``git clone \<URL\>` where `\<URL\>` is the one you copied. Or open a new vscode window, select _Clone Git Repository_, and paste the URL you copied. If you followed the URL to GitHub, then you can recopy the URL using the "<> Code ▼" button.
1. Create and activate a virtual environment in the project directory.  Revisit Project 0 for a reminder on how to create the virtual environment. There is also a _cheat sheet_ at [learningsuite.byu.edu](https://learningsuite.byu.edu) _Content_ &rarr; _Projects_ &rarr; _Projects Cheat Sheet_.
1. Install the project package. **Be sure your virtual environment is active before installing the package!** In a terminal in the virtual environment in the project directory do: `pip install --editable ".[dev]"`. Use `pip3` instead of `pip` if your system requires it.
1. Verify the package installation. From the terminal in which you activated the virtual environment and installed the project package, type `project1` and hit enter. You should see the below output.
    
    ```
    $ project1
    usage: project1 <input file>
    ```
1. Verify that tests are ready to run. Open the _Testing Pane_ in VS Code by clicking on the test tube icon. If you see 
    ```
    pytest Discovery Error [project-1]
    ```
    then you must open the _Command Palette_ from the _View_ menu, choose `Python: Select Interpreter`, and choose the interpreter for the virtual environment (probably `Python 3.12.5 (.venv)`).

## Project Requirements

1. The project must be completed individually -- there is no group work.
1. Project pass-off is on GitHub. You will commit your final solution to the `master` branch of your local repository and then push that commit to GitHub. Multiple commits, and pushes, are allowed. A push triggers a GitHub action that is the auto-grader for pass-off. The TAs look at the result of the auto-grader on GitHub, and your code, to determine your final score.
1. You must pass all integration tests up to, and including, `tests/test_passoff_80.py` to move on to the next project. Bucket 80 is the minimum functionality to complete the course.
1. You must implement, with no AI help except syntax and formatting questions, the `lexer` function in `src/project1/lexer.py` using the algorithm discussed in class. See [LEXER.md](docs/LEXER.md) for a complete description of the token types and lexer algorithm along with input to output examples.
1. All tokens must be detected using FSMs. Regular expression libraries, loops, etc. are not allowed.
1. You must implement, with no AI help except syntax and formatting questions, the FSMs for the following tokens:
    * `ID`
    * `COMMENT`
    * `STRING`
1. You may use AI to write code for any of the other remaining tokens.
1. Your code must not report any issues with the following code quality tools run in the integrated `vscode` terminal from the root of the project directory:
    * `ruff check .` -- detects and reports code smells
    * `ruff format .` -- enforces consistent formatting
    * `mypy src/project1/*.py` -- type checks the files

Consider using a branch as you work on your submission so that you can `commit` your work from time to time. Once everything is working, and the auto-grader tests are passing, then you can `merge` your work into your master branch and push it to your GitHub repository. Ask your favorite AI for help learning how to use Git branches for feature development.

## Unit Tests

There are basic accept/reject unit tests defined in `tests/test_fsm.py` for the `Colon`, `Eof`, and `Whitespace` FSMs. See [CODE.md](docs/CODE.md) for a complete overview of the code that you are to use for this project.

**We strongly encourage you to add unit tests for the `ID`, `COMMENT`, and `STRING` FSMs at a minimum.** That aside, here are some of the edge cases that appear in the integration tests for pass-off that you might consider as part of your unit test efforts:

- An empty input file.
- A colon immediately followed by another token (no space between the colon and the next token).
- An identifier that contains a number.
- An identifier that contains a keyword.
- An empty string (nothing between the quotes `''`).
- An unterminated string.
- A string with multiple quote (`\'\'\'`)

You might also consider adding test cases to `tests/test_lexer.py` as you implement different FSMs. Once an FSM is done, then you can add it to the `lexer` function with a test to be sure the added FSM works as expected.

See the notes from class and the homework on how do to do testing using `pytest` in the projects. In general, the `Testing Pane` in VS Code is super convenient for running, and debugging tests. The integrated terminal is also super helpful. The `-k` flag is the easiest way to find and choose a test since it uses matching. Try it out.

```
$ pytest -k lexer
=================================================================================================================================================== test session starts ===================================================================================================================================================
platform linux -- Python 3.12.3, pytest-8.2.0, pluggy-1.5.0
rootdir: /workspaces/project-1
configfile: pyproject.toml
collected 42 items / 38 deselected / 4 selected

src/project1/lexer.py .                                                                                                                                                                                                                                                                                             [ 25%]
tests/test_lexer.py ..F                                                                                                                                                                                                                                                                                             [100%]

...
```

Here the first test is the _doctest_ in the _docstring_ for the module. (A _docstring_ is the triple-quoted string at the top of a file or function. If unfamiliar with _docstring_, ask your favorite AI tool for a tutorial.) Anytime `pytest` sees what appears to be a something that might be typed into an interactive Python shell session inside a _docstring_, it turns it into a test. These tests are called "doctests" and they are useful not just for examples but as a means to be sure the intended usage still works as intended. The doctest is also a very quick, and simple, way to test a function. Here is how to run just the doctest for the `project1` function in `project1.py`.

```
$ pytest -k project1.project1.project1
```

**WARNING**: if there are syntactic, or other errors, in your code, then the testing pane will fail to show your tests.

## Integration Tests (pass-off)
There are some limited integration tests in `tests/test-project1.py` but the primary tests are found in the `tests/test_passoff_xx.py` files. These tests are used for project pass-off. The `xx` on each bucket denotes the available points for passing the tests in that bucket. The value of each test in each bucket is uniform: _points-for-bucket/number-of-tests-in-bucket_. Bucket 80 is the minimum requirement to pass the course. See [CODE.md](docs/CODE.md) for a complete overview of the pass-off tests.

## Code Quality Tools

The `ruff` and `mypy` tools are integrated into `vscode` with the extensions you installed from Project 0. The _Problems_ pane reports both code "smells" from `ruff` and type errors from `mypy` on opened files and is helpful for correcting issues. (You can find the _Problems_ pane in VS Code by opening the intergrated terminal. Above the terminal, look for the `PROBLEMS` tab.) Both `ruff` and `mypy` can be run via command line in the root directory for the project as detailed in the [Project Requirements](#project-requirements).

## Submission and Grading

The minimum standard for this project is **bucket 80**. That means that if all the tests pass in all buckets up to and including bucket 80, then the next project can be started safely. You can run each bucket from the testing pane or with `pytest` on the command line. Passing everything up to and including `test_passoff_80.py` is the minimum requirement to move on to the next project.

Submit Project 1 for grading by doing the following:

  * Commit your solution on the master branch
  * Push the commit to GitHub -- that should trigger the auto-grader
  * Goto [learningsuite.byu.edu](https://learningsuite.byu.edu) at _Assignments_ &rarr; _Projects_ &rarr; _Project 1_ to submit the following:
    1. Your GitHub ID and Project 1 URL for grading.
    1. A short paragraph outlining (a) how you prompted the AI to generate any code (if you used it) and (b) how you determined the quality and correctness of that code.
    1. A screen shot showing no issues with `mypy`, `ruff check`, and `ruff format`.
  * Confirm on the GitHub Actions pane that the pass-off tests passed, or alternatively, goto the Project 1 URL, find the green checkmark or red x, and click it to confirm the auto-grader score matches the pass-off results from your system.

### Paragraph on AI

Guidelines for answering

_"A short paragraph outlining (a) how you prompted the AI to generate any code (if you used it) and (b) how you determined the quality and correctness of that code."_

These guidelines give examples from Project 1.

* Brief means no more than 500 words.
* Be specific about what code was generated. _"AI generated FSM code for `QMARK`, `LEFT_PAREN`, `RIGHTPAREN`, and `COMMA`."_
* Be general about the final form of the prompts used to generate the code and any prompt iteration that was required. _"I gave the AI example code and asked it to create code that matched the pattern, and style, in that example code. I had to revise the prompt to specifically ask it to not generalize an FSM to detect a supplied string."_
* Be specific about how you determined the quality and correctness of generated code. _"A manual visual inspection was sufficient to determine quality and correctness because the generated code was trivial. I also ran the code quality tools on the generated code as a second level check."_
* Be specific about where else AI was leveraged. _"I used AI to breakdown and explain the pseudo-code for the `lexer` algorithm as well as the `FiniteStateMachine` class. AI also provided test inputs for my `STRING` FSM to help debug the apostrophe escape sequence."_

## Best Practices

Remember that the intent of the project is to learn about FSMs while you implement the `lexer` function. The best practice for doing this learning is to design an FSM, write a test for that FSM, and repeat. There are FSMs that are *easier* and FSMs that are *harder*. Perhaps the easiest FSMs are
- `COMMA`
- `PERIOD`
- `Q_MARK`
- `LEFT_PAREN`
- `RIGHT_PAREN`
- `COLON` (implemented in starter code)
- `EOF` (implemented in starter code)

Implement one or two of these easiest FSMs by hand (e.g., COMMA and PERIOD) and then use AI to create the code for the rest of the easier FSMs. The idea is to offload tedious tasks to AI but **not until you understand what you are doing**. We want the AI-generated code to use the same style as your code, and we insist that the AI-generated code be FSMs (and not, for example, string comparisons).

One way to prompt AI for the code generation is the following

1. Write tests for the input string `"("`
1. Tell the AI that you want it to remember the code you are going to type in since you'll be asking about in a subsequent prompt
1. Copy and past the base FSM into the AI
1. Copy the `COLON` FSM into the AI and tell the AI that you'll be asking about that code in a subsequent prompt
1. Tell the AI to create a class that follows the pattern of the `COLON` FSM so that it accepts the string `")"` and generates the `RIGHT_PAREN` token. Make sure that each state reads one character at a time.
1. Copy the AI code into your FSM class
1. Run your test on the code
1. Repeat for the other easier FSMs

Consider also prompting the AI to also generate the unit tests for `tests/tests_fsm.py` and `tests/tests_lexer.py`.

---

Other _easier_ FSMs are
- `COLON_DASH` (demonstrated in Jupyter notebook tutorial)
- `SCHEMES`
- `FACTS`
- `RULES`
- `QUERIES`

By hand, write a test, implement, and test the `SCHEMES` FSM using the pattern in the `COLON_DASH` FSM. Use AI to generate the code for the `FACTS`, `RULES`, `QUERIES`, etc. Make sure the code uses the same FSM-style class and test each FSM.

---
The hardest FSMs are the ones that require some more thought about how to design the FSM correctly.
- `WHITESPACE` (implemented in the starter code)
- `ID`
- `COMMENT`
- `STRING`

You may not use AI to write these FSMs. Instead, use the following steps, which are written assuming you are creating the `ID` FSM
1. Draw the FSM that ends in an accept state for any input string that matches the `ID` pattern and in a reject sync state for any other string
1. Step through the FSM by hand for a string that should end in the accept state
1. Step through the FSM by hand for a string that should not end in the accept state
1. Write a test for both of the examples you used when you stepped through by hand
1. Implement the `ID` FSM and run the test

Look through the integration tests for some of the trickier tests. Especially look for inputs that will produce an `UNDEFINED` token like a weird string or an input that doesn't match the `ID` pattern.
