# Coding Portion of Homework 1

## Table of Contents
- [0. Learning Goals](#0-learning-goals)
- [1. Clone the Starter Repository](#1-clone-the-starter-repository)
- [2. Explore Project Structure](#2-explore-project-structure)
- [3. Set up your Python Environment with `venv`](#3-set-up-your-python-environment-with-venv)
  - [3.1 Deactivate Conda (if active)](#31-deactivate-conda-if-active)
  - [3.2 Create a Virtual Environment ](#32-create-a-virtual-environment-)
  - [3.3 Activate the Virtual Environment](#33-activate-the-virtual-environment)
- [5 Configure Project](#5-configure-project)
- [6. Unit Tests for the Union Function](#6-unit-tests-for-the-union-function)
  - [Unit Tests and Integration Tests](#unit-tests-and-integration-tests)
  - [6.1 Types of Unit Tests](#61-types-of-unit-tests)
  - [6.2 Positive Test](#62-positive-test)
  - [6.3 Negative Test](#63-negative-test)
  - [6.4 TypeError Test](#64-typeerror-test)
- [7. Run Tests from the Terminal](#7-run-tests-from-the-terminal)
- [8. Running Tests in VS Code](#8-running-tests-in-vs-code)
  - [8.1 Tell VS Code to Use the Correct Python Interpreter](#81-tell-vs-code-to-use-the-correct-python-interpreter)
  - [8.2 Configure and Run Tests in VS Code](#82-configure-and-run-tests-in-vs-code)
- [9. Understanding Failing Tests: Example with Intersection](#9-understanding-failing-tests-example-with-intersection)
  - [9.1 Positive Test Fails](#91-positive-test-fails)
  - [9.2 Negative Test Fails](#92-negative-test-fails)
  - [9.3 Type-Checking Tests Still Pass](#93-type-checking-tests-still-pass)
  - [9.4 Fix the implementation for the intersection function](#94-fix-the-implementation-for-the-intersection-function)
- [10. Cartesian Product Tests](#10-cartesian-product-tests)
- [11. Integration Tests and GitHub Classroom Autograding](#11-integration-tests-and-github-classroom-autograding)
  - [11.1 Viewing Results from GitHub Classroom Autograding](#111-viewing-results-from-github-classroom-autograding)
  - [11.2 Integration Test Buckets](#112-integration-test-buckets)

---

## 0. Learning Goals

- Review
  - Installing and activating virtual environments
  - Configuring a package
  - Using `git`
- Practice **set operations**: union, intersection, Cartesian product
- Use **math** to construct and reason about test cases
- Write and categorize **three types of unit tests**:
  - Positive tests: what *should* happen
  - Negative tests: what *should not* happen
  - TypeError tests: when invalid input should raise an error
- Run tests from both the **command line** and the **VS Code Testing Panel**

---

## 1. Clone the Starter Repository
The steps are:
- Get the repo URL from the `Code` button on GitHub
- Open a new window in VS Code and click **Clone Repository**
- Paste your repo URL
- Choose `CS236/` as the destination folder.


---

## 2. Explore Project Structure

The root folder is the `CS236` directory you created earlier. Inside that folder is another folder named something like `homework1`. The precise name might vary, but you'll see the name `homework1` somewhere in the name. Inside the `homework1` folder are a handful of other files and folders. The general structure of the files and folders is 

```
homework1/
├── pyproject.toml
├── README.md
├── src/
│   └── homework1/
│       ├── __init__.py
│       └── set_operations.py
└── tests/
    └── test_set_operations.py
```

The key files and folders are:

- **README.md** – this tutorial  
- **pyproject.toml** – configuration file that defines project metadata 
- **src/** - source directory containing the Python module that defines various set operations
- **src/homework1** - the folder for the `homework1` Python package
- **tests/** –  directory where you'll use unit tests to verify your code automatically

---

## 3. Set up your Python Environment with `venv`

Recall that a _virtual environment_ is a lightweight, local Python environment used to isolate project-specific packages from the default Python settings on your computer. Using a virtual environment prevents dependency conflicts and ensures that `pytest` behaves consistently across machines. The name of the virtual environment we will use is `venv`.

### 3.1 Deactivate Conda (if active)
If the prompt in the integrated terminal starts with `(base)` or has some other environment indicator in parentheses `(myenv)` then deactivate conda by typing

```bash
conda deactivate
```

You'll know you've been successful if the `(base)` part of the prompt will have disappeared.

### 3.2 Create a Virtual Environment 
You did this in Project 0, but it's helpful to review the steps because you'll have to do it for each project in the class. Make sure you are in your `CS236/` directory. What you type next depends on what type of computer you are using and how it is configured. Usually, PCs install the latest version of Python so that you can execute it by typing `python`. Macs usually ship with an old version of Python, and the command `python` points to that old version. To overcome this, you run Python by typing `python3`. Thus,

If on a PC then you should type 
```bash
python -m venv .venv
```
and if on a Mac or a computer configured to use Linux then you should type
```bash
python3 -m venv .venv
```
This creates a hidden directory called `.venv` in your project folder containing a standalone Python environment.

### 3.3 Activate the Virtual Environment
You now have to tell VS Code that you want to use the virtual environment. This is called _activating_ the environment. How you activate `venv` depends on your machine. 

For a Windows machine running PowerShell,
```bash
venv\Scripts\Activate.ps1
```

and on a Mac or Linux-based machine
```bash
source .venv/bin/activate
```
If you are having trouble activating the virtual environment, ask your favorite AI tool.

You'll know that you've been successful if the name of the prompt changes and starts with `(.venv)`.

---


## 5. Configure Project
On most PCs, 
```bash
pip install --editable ".[dev]"
```

On most Macs and Linux-based machines
```bash
pip3 install --editable ".[dev]"
```

The file `pyproject.toml` is used when we run the `install` command. Let's look at one part of `pyproject.toml`.
```python
[project.optional-dependencies]
dev = [
  "pytest",
  "mypy",
  "ruff",
  "pre-commit",
]
```
The line `[project.optional-dependencies]` says that the project depends on some external packages. The line `dev = [ ... ]` lists the packages that will be used when you are **developing** your code. This homework uses  only `pytest`, but subsequent homeworks and projects will use the others. We'll explain those tools when we get there.  

Note that the word **dev** from the install command `pip3 install --editable ".[dev]"` says that you are installing the package in **development** mode.

Finally, note that this homework does not use a Command-Line Interface (CLI). If you have the energy, you can compare the `pyproject.toml` file for this homework with the one for Project 0 and notice the absence of any reference to CLI in the `.toml` file for this homework.

---

## 6. Unit Tests for the Union Function
### Unit Tests and Integration Tests
Computer scientists distinguish between two types of tests:
- A **unit test** checks whether a _single, small part of the code_ (usually one function) works correctly in isolation.
- An **integration test** checks whether _multiple parts of the program work together_ as expected.

Many of you are probably used to thinking about testing in terms of integration tests because that is the kind of testing that has been done in your previous classes: does the code work right or not. Like your other classes, passing off projects in CS 236 will use integration tests, but you'll also be required to write _unit tests_. 

It might seem like a pain to write unit tests, but there are three reasons to do so:
- The unit tests in this class are designed to help you connect the mathematical concepts taught in class with the functions you implement in the projects.
- Debugging small, isolated pieces of code is much easier than debugging an entire program.Since each project in the class builds on the previous project, you'll end up writing a larger program than many of you have written before, so testing small chunks of the program makes sense.
- It is easier to modify code when you write unit tests because running the unit tests will tell you whether any small change you make introduces a new error.

Our goal is to have you **write tests before you begin programming**, but we understand that some of you will be in "survivor mode" because of the demands of the semester and, consequently, will write the tests after you've written your code.  Try your best.

### 6.1 Types of Unit Tests
There are three types of unit tests used in CS 236:
- a **positive test** provides evidence that the _code produces the correct result_ for valid input because the test is based on a known math fact or expected behavior 
- a **negative test** provides evidence that the _code does not produce an incorrect result_, and is used to detect logical errors or incorrect outcomes in your code
- a **type-checking test** confirms that a function you've written _raises the correct kind of error_ when given input of the wrong type, and is used to "enforce contracts" so that your code only operates on the kinds of inputs you expect

In this assignment, we'll write type-checking tests, but later in the class we'll use the tool called `mypy` that helps us do _static type checking_ so that we don't have to write so many tests. The tool `mypy` was one of the packages specified in `pyproject.toml`.



### 6.2 Positive Test
Suppose that we are given two sets _A = {1, 2}_  and _B = {2, 3}_. The union of two sets is the collection of all elements that are either in the first set or in the second or both. Thus, _A ∪ B = {1, 2, 3}_.
If we write a function called `union` that tries to implement the _union_ set operation then it should output the set _{1,2,3}_ if its inputs are set _A_ and set _B_. This is the basis of the positive test.

Open the file `tests/test_set_operations.py` and look at the `test_union_positive()` function.

```python
def test_union_positive() -> None:
    # Function inputs
    A: set[int] = {1,2}
    B: set[int] = {2,3}

    # Expected output
    expected: set[int] = {1, 2, 3}
    
    # Assert that the union function works correctly
    assert union(A, B) == expected
```
Notice four things about the `test_union_positive()`.
1. It's a function. All unit tests in the `pytest` framework are functions. When we run `pytest`, the function for each unit test is run.
2. The `test_union_positive` function defines two sets, _A={1,2}_ and _B={2,3}_.  These two sets were chosen because we "did the math" above and know what to expect when we take the union of the sets.
3. The `test_union_positive` function defines the expected output based on the known behavior of the mathematical union operation, _A ∪ B = {1,2,3}_.
4. The `assert` statement in the code `assert union(A,B) == expected`
  checks whether the actual result of `union(A, B)` is equal to the expected result `{1, 2, 3}`. In other words, the `assert` calls the `union` function with the arguments $A$ and $B$, receives the return value $A\cup B$ and compares the returned value with what we expected to happen.  If the value returned by the function matches the expected result then **nothing happens**, which means that the test passes silently. If the value returned by the function does not match the expected result, Python raises an `AssertionError`, and the test fails. This will be captured by `pytest` and information about the failure will be given to us.


### 6.3 Negative Test

A negative test checks that the function **does not** return an incorrect result. Let's make up something incorrect by defining _A = {1}_ and _B = {2}_, and then noting that _A ∪ B ≠ {1}_.

```python
def test_union_negative() -> None:
    # Function inputs
    A: set[int] = {1}
    B: set[int] = {2}

    # Incorrect output
    incorrect_result: set[int] = {1,2}
    
    # Assert that the union function works does not work incorrectly
    assert union(A, B) != incorrect_result
```

This test follows the same structure as the positive test, but here `pytest` verifies that the output is not equal to an incorrect result. If the output differs from the incorrect result, the `assert` statement passes silently, which indicates that the function behaved as expected for this case. If the output matches the incorrect result, `pytest` raises an `AssertionError`, signaling that the function produced an incorrect value. `Pytest` captures that error and prints out information about the error.

Note that I chose this test to check whether I accidentally implemented the union as an intersection, since the intersection of _A_ and _B_ is _A ∩ B = {1}_
This test was designed to detect a logical error that might occur if we accidentally implement an intersection when we meant to implement a union.

### 6.4 TypeError Test

The function `test_union_invalid_input_type_1` makes sure that if you pass `union` an argument that is not a set then your `union` function detects that error. The `union` function in `src/homework1/set_operations.py` was only implemented for sets of integers. The type error tests check whether things other than integers are handled well by `union`.

```python
def test_union_invalid_input_type_1() -> None:
    # one input is the wrong type
    A: str = "not a set"
    B: set[int] = {1,2}

    # Ask an LLM what is happening here
    with pytest.raises(TypeError):
        union(A, B)
```

Notice how this statement uses `with pytest.raises()` instead of an `assert` statement. More specifically, it has the structure 
```python
with pytest.raises(TypeError):
    union(A, B)
```

What's happening is that the `union` function has code that makes sure the arguments passed to the function are the right type. In the `union` function is code that says
```python
# Check if inputs are sets
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError("Arguments must be sets")
    # Check if all set elements are integers
    if not all(isinstance(x, int) for x in a | b):
        raise TypeError("All elements of the sets must be integers")
```
The `raise` keyword is Python’s way of signaling that an error has occurred. The `pytest.raises` in the type check function `test_union_invalid_input_type_1` checks to see that the expected type of error is raised when you give `union` the wrong input type.

**Ask your favorite AI tool** what that piece of code does. Explain that you are doing a tutorial on `pytest` and ask for help understanding what is going on with the `with` statement. You can even attach this `README.md` to your query so the AI tool has some more context. An example prompt is:

```text
What does 

    with pytest.raises(TypeError):
        union(A, B) 

do in the function 

    def test_union_invalid_input_type_1() -> None:
        # one input is the wrong type
        A: str = "not a set"
        B: set[int] = {1,2}

        with pytest.raises(TypeError):
        union(A, B)

How does the `with` statement work?
What does it mean to call the function `pytest.raises`?
What is a `TypeError`?
```

There are other functions in `tests/test_set_operations.py` that check other type errors that might occur for the `union` function. One checks whether the second input is a set, and the other checks whether one of the elements of the set is not a integer.

---
## 7. Run Tests from the Terminal

From the integrated terminal in VS Code, type
```bash
pytest
```
You'll be given a list of which tests fail. Notice that none of the tests involving union appear in the terminal. That's because they all pass. Tests that succeed only output `.` in the `pytest` output (unless verbose mode is enabled). Tests that fail show more output when we run `pytest` from the command line. Passing tests do not display detailed output (unless `pytest` is run in verbose mode). The final summary line in your terminal output should look something like:
```bash
== 4 failed, 11 passed in 0.04s ==
```

---

## 8. Running Tests in VS Code
You can run and debug `pytest` directly in VS Code. 

### 8.1 Tell VS Code to Use the Correct Python Interpreter

The first thing to do is tell VS Code that you are using the version of Python from the virtual environment. Go to `View` in the VS Code menu and select `Command Palette`. Select `Python: Select Interpreter` and choose the version of Python that has `.venv` in it. The correct version of the interpreter will look something like `Python 3.12.5 (.venv)`. If you don't see a version of the interpreter that includes `.venv` it means that you haven't installed or activated the virtual environment.


### 8.2 Configure and Run Tests in VS Code
The second thing to do is to tell VS Code which testing tool you are going to use (and where to find the tests).

- **Open the Testing Panel**  
   Click the beaker icon in the sidebar to open the **Testing panel**.

- **Configure VS Code for pytest (if needed)**  
   - From the `View` menu in VS Code, open the Command Palette (`Ctrl+Shift+P` or `⌘+Shift+P`)
   - Click on: `Python: Configure Tests`
   - Select `pytest`
   - Set the test folder to `tests/`

- **View Your Tests**  
   You should now see a list of test functions from `test_set_operations.py`. Each function has:
   - An open left triangle that pops up if you mouse over the function.
   - A red ❌ or green ✔ to indicate pass/fail status

If you run all the tests, you should see that all the tests for the `union` function pass, but some of the other tests fail.

---

## 9. Understanding Failing Tests: Example with Intersection

In this assignment, the `intersection` function is implemented incorrectly — it returns the **union** instead. Here's what is happening with the tests that fail.

### 9.1 Positive Test Fails
The first test for intersection is called `test_intersection_positive()` and is defined as

```python
def test_intersection_positive() -> None:
    # Function inputs
    A: set[int] = {1,2}
    B: set[int] = {2,3}

    # Expected output
    expected: set[int] = {2}

    # Assert that the intersection function works correctly
    assert intersection(A, B) == expected
```

When we do the math to take the intersection of $A = \{1,2\}$ and $B = \{2,3\}$ we know the answer should be $A \cap B = \{2\}$.

Unfortunately, `intersection()` is not implemented correctly. It's actually implemented as a union, so `intersection(A,B)` returns  $A \cup B = \{1, 2, 3\} $ and the test fails because:
```python
{1, 2, 3} != {2}
```

### 9.2 Negative Test Fails
The second test is a negative test and checks for the logical error that might occur if we implement the `intersection` function as a union by accident. We define the two input sets, identify the incorrect result, 

```python
def test_intersection_negative() -> None:
    # Function inputs
    A: set[int] = {1}
    B: set[int] = {2}

    # Expected output
    incorrect_result: set[int] = {1,2}
    
    # Assert that the intersection function works does not work incorrectly
    assert intersection(A, B) != incorrect_result
```

This negative test is based on the math that says $ A \cap B = \emptyset $ but an incorrect implementation might say $ A \cup B = \{1, 2\}$.  The negative test **fails**, because the function returns the incorrect result the test was trying to catch.

The failure of the negative test is actually more informative than the failure of the positive test. The failure of the positive test tells us that something was wrong for that particular input. The failure of the negative test suggests a reason for the failure: we implemented the function incorrectly but with a predictable logical error.


### 9.3 Type-Checking Tests Still Pass

The **TypeError tests** still pass as long as your function checks that:
- Both inputs are sets
- All elements are integers

These tests are valuable because they help catch mistakes **even when other logic is broken**.


### 9.4 Fix the implementation for the intersection function
Fix the code that causes the intersection function to fail the tests. Rerun the test to see if the tests now pass. 

---

## 10. Cartesian Product Tests

Use the tests to diagnose why the Cartesian product function fails. The code includes the source of the error in the comments, so you can check your diagnosis pretty quickly. Fix the function and confirm that it passes all tests.

---

## 11. Integration Tests and GitHub Classroom Autograding
GitHub Classroom can be set up to run tests automatically. CS 236 will use this capability to automatically evaluate whether your code works. All integration tests will be run automatically in GitHub Classroom when you commit your repo.

This semester, CS 236 will provide you the same integration tests that will be run in Github in the repository you clone for each project. This means:
- You can run integration tests locally before committing to ensure they pass.
- When you push your changes, GitHub Classroom will run the same integration tests remotely.
- You can view the results of your tests in GitHub Classroom.

### 11.1 Viewing Results from GitHub Classroom Autograding
Let's talk about how to view the results of the integration tests in GitHub Classroom. Once you've fixed the errors in the intersection and Cartesian product functions, run `pytest` and confirm that all tests pass. 

**Push your repo to GitHub** using the steps shown in Project 0. Here are the steps for your review.

  1. Modify your code
  2. Stage your changes (`git add`)
  3. Commit those changes (`git commit`)
  4. Push those commits to GitHub (`git push` or **Sync** in VS Code)

Once you’ve committed and pushed your code, GitHub Classroom will automatically run the `run-autograding-tests` workflow. You can check the results in **two ways**:  


#### **Option 1 – On GitHub.com**
1. Go to your repository on GitHub.  
2. Click the **Actions** tab at the top of the page. 
3. Click on the topmost workflow. That will open a new page.  
3. Open the most recent `run-autograding-tests` workflow run.  
4. Scroll to find the **Autograding Reporter** section.  
5. Expand it to see the detailed integration test results, including the table showing scores for each test.  The summary should look something like the following:


| Test Runner Name                 | Test Score | Max Score |
|-----------------------------------|------------|-----------|
| test_union_integration_disjoint   | 2          | 2         |
| test_union_integration_overlap    | 2          | 2         |
| test_union_integration_with_empty | 2          | 2         |
| test_intersection_integration_basic | 2        | 2         |
| test_intersection_integration_disjoint | 2    | 2         |
| test_intersection_integration_with_empty | 2 | 2         |
| test_cartesian_product_integration_ints_and_strings | 2 | 2 |
| test_cartesian_product_integration_strings_and_bools | 2 | 2 |
| test_cartesian_product_integration_with_empty | 2 | 2 |
| **Total:**                        | **18**     | **18**    |

#### **Option 2 – Inside VS Code** (if you installed the GitHub Actions extension in Project 0)
1. Click the **GitHub Actions** icon in the Activity Bar (left side of VS Code).  
   - If you don’t see it, open the Extensions panel, search for **GitHub Actions** (publisher: GitHub), and install it.  
2. In the **Workflows** list, select your repository if prompted.  
3. Look for the most recent run of `run-autograding-tests`.  
4. Click it to view the workflow jobs and their pass/fail status.  
5. Click on the job named **Autograding tests** to view the log for the test run.  

> **Note:** The **Autograding Reporter** step will show up in the list, but detailed output (such as the integration test score table) can’t be displayed directly in VS Code.  
> To view the full table, hover over **Autograding Reporter** and click the **globe icon** that appears — this will open the GitHub web interface with the complete log.  

### 11.2 Integration Test Buckets
Each project will have several integration tests. The integration tests are organized into **buckets**, which are subsets of the integration tests. Rather than assigning points for each test, points are assigned based on passing all tests in a given bucket. For example, for a project with two buckets you might see results like the following:

| Test Runner Name | Test Score | Max Score |
|------------------|------------|-----------|
| bucket-80        | 80         | 80        |
| bucket-100       | 20         | 20        |
| **Total:**       | **100**    | **100**   |

The reason tests are grouped into buckets is because each project in CS 236 builds on the previous project. That means that the code for Project 1 has to work before the code for Project 2 will be able to work. We've tried to organize the tests so that if you pass all tests in `bucket-80` you can make good progress on the subsequent project even if your code isn't perfect. You might have to go back and fix a few things in your code that pop-up in the subsequent project, but it won't be a catastrophe.

That means that the tests in `bucket-80` are usually easier to pass than the tests in `bucket-100`.

If you'd like to see more about how the buckets work, open up your Project 0 again. Navigate to the `tests` folder and notice the two files
- `test_passoff_80.py`
- `test_passoff_100.py`
These two files sequence the testing operations so that all tests in each bucket are run. If you open the `tests/resources` folder, you'll see two folders: `80` and `100`. When you open the folders, you'll see two types of files: inputs and answers. The inputs are what is passed to your code, and the answers are what your code should generate. 

That means that for each project, you will know the set of inputs used in the integration tests, and you will also have available the answer that your code should generate.

If you navigate to your GitHub repo for Project 0, click on `Actions`, and open up the test results, you should see a table showing that you passed all of the tests in both bucket 80 and bucket 100.
