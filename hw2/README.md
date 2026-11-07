# Homework 2: Functions in Mathematics and in Python

In this assignment, you’ll explore key concepts from mathematics and computer science related to **functions**. From the math perspective, this assignment discusses

- Domains and codomains
- Functions, partial functions, and mappings that are not functions
- How the definition of mathematical functions relates to the methods of a Python class, with an emphasis on a programming concept called **side effects**

From the programming perspective, this assignment includes
- Writing a function that takes a **set of ordered pairs** and says whether the set represents a function, partial function, or neither
- Reviewing how to run unit tests in VS Code and how to do passoffs in GitHub Classroom.
- Learning how to write unit tests when a Python class has methods that rely on or that modify class member variables.
- Learning about using type hints in Python and how to use the `mypy` tool to check for type errors in Python.

---

## Table of Contents

- [1. Programming Environment for Homework 2](#1-programming-environment-for-homework-2)
- [2. Definitions: Function vs. Partial Function](#2-definitions-function-vs-partial-function)
  - [2.1 Domain, Codomain, Cartesian Product](#21-domain-codomain-cartesian-product)
  - [2.2 Function](#22-function)
  - [2.3 Partial Function](#23-partial-function)
  - [2.4 Not a Function](#24-not-a-function)
  - [2.5 Edge Cases](#25-edge-cases)
- [3. Programming Task 1](#3-programming-task-1)
- [4. mypy: Static Type Checking](#4-mypy-static-type-checking)
  - [4.1 Why use mypy?](#41-why-use-mypy)
  - [4.2 How to run mypy](#42-how-to-run-mypy)
  - [4.3 Example: What mypy reports without type hints](#43-example-what-mypy-reports-without-type-hints)
- [5. Methods, Side Effects, and Mathematical Functions](#5-methods-side-effects-and-mathematical-functions)
  - [5.1 Example: Method with a Side Effect](#51-example-method-with-a-side-effect)
  - [5.2 Why This Matters](#52-why-this-matters)
  - [5.3 Functional Programming](#53-functional-programming)
- [6. Testing Methods that Use Object State](#6-testing-methods-that-use-object-state)
  - [6.1 Example](#61-example)
  - [6.2 Summary of Writing Tests with Object State](#62-summary-of-writing-tests-with-object-state)

---

## 1. Programming Environment for Homework 2
Clone the project into VS Code and configure it by doing the following steps:
- install and activate `venv`
- install the project (e.g., `pip install --editable ".[dev]"`)
- configure VS Code so that it can run tests by
  - Navigating to _View_ -> _Command Palette_ -> _Python: Select Interpreter_ and choosing the interpreter that is running in the virtual environment (e.g., `Python 3.12.5 (.venv)`)
  - Opening the Testing Panel in VS Code (the beaker) and configuring tests to use `pytest` and the `tests` directory.

This homework uses the following project structure.

```
homework2/
├── pyproject.toml
├── README.md
├── src/
│   └── homework2/
│       ├── __init__.py
|       ├── classify_function.py
│       └── score_keeper.py
└── tests/
|   ├── test_classify_function_typechecks.py
|   ├── test_classify_function.py
|   └── test_score_keeper.py
```

We'll look at both modules in `src/homework2`, and we'll work with all the test modules in `tests`.

---

## 2. Definitions: Function vs. Partial Function

### 2.1 Domain, Codomain, Cartesian Product
The definition of a function is given in the reading from the textbook. The definition uses the following notation:
- _D_ is the **domain** (a set of inputs),
- _C_ be the **codomain** (a set of possible outputs), and
- _f_ is a **mapping** represented as a set of ordered pairs _f ⊆ D × C_


### 2.2 Function

A mapping _ f _ is a **function** if:

1. Every element in the domain _D_ appears exactly once as the first element of a pair in _f_
2. Each domain element maps to **exactly one** codomain element

In other words, _every input has one and only one output_.

Notice that we are defining the function using a subset of ordered pairs. For example, for domain _D = {1, 2}_ and codomain _C = {'a', 'b'}_, we can define a mapping as _f = {(1,'a'), (2,'b')}_ which is a subset of all the possible ordered pairs that could appear in the Cartesian product _D × C_. This function maps `1 → 'a'` and `2 → 'b'`. You might be most familiar with writing this function as

- _f(1) = 'a'_
- _f(2) = 'b'_
  
The first element of the ordered pair goes inside the parentheses and the second element of the ordered pair is the value that the function produces, _f(first element) =  second element_.


This mapping is a function because
- Both elements of the domain appear as the first element of the ordered pair
- No element of the domain appears twice as the first element of the ordered pair


### 2.3 Partial Function

A mapping _f_ is a **partial function** if:

1. Some elements in _D_ may not appear in the mapping
2. Every input that **is** mapped still has **exactly one** output

That is, **some inputs might not be used**, but **none are duplicated**. Consider the following mapping:
_f = {(1,'a')}_.
The mapping is a partial function because it is defined for _1 ∈ D_ but not for _2 ∈ D_.


### 2.4 Not a Function

A mapping is **not a function** if any input in the domain appears more than once in the mapping with different outputs.
In other words, any single input maps to multiple values. Consider the following mapping.
_f = {(1,'a'), (1,'b')}_.
The mapping is not a function because _1 ∈ D_ is in the first spot in two of the ordered pairs so _f(1)_ can be either _'a'_ or _'b'_ at any time.

### 2.5 Edge Cases

You are going to write a Python function that takes a set of ordered pairs and classifies it as a function, partial function, or neither. That Python function needs to handle the following two edge cases.

1. _D=∅_, _C ≠ ∅_, and f = ∅_. The domain is empty, the codomain is not empty, and the mapping in the tuples is empty. Notice that _f_ has to be the empty set since _D × C = ∅ × C = ∅_, and the only subset of the empty set is the empty set itself.

    The mapping _f_ in this problem **is a function** because each element of the domain appears only once in _f_, which is _vacuously_ true since both _D_ and _f_ are empty. Vacuously true means that there are no elements to check. This reasoning can be a little tricky so we'll return to it later in the class when we discuss propositional logic and quantification.
1. _D  ≠ ∅_, _C  ≠ ∅_, _f = ∅_. The domain is not empty, the codomain is not empty, but the mapping is empty.

   The mapping _f_ in this problem **is a partial function** because there are elements of the domain that do not appear in the tuples in _f_ (since there are no tuples in _f_). 

1. _D  ≠ ∅_, _C =∅_, _f = ∅_. The domain is not empty, the codomain is empty, and the mapping _f_ is empty.

    The mapping _f_ in this problem **is a partial function** for the same reason as the example just above. You wouldn't label _f_ as 'not a function' because no domain element maps to _to_ outputs; rather, no elements map at all.

---

## 3. Programming Task 1


Implement the function `classify_function(...)` in `src/homework2/classify_function.py`. The first input to the function is a **set of tuples** — each tuple represents a pair `(input, output)`.

Return one of the following strings:

- `"function"` if and only if (iff) the relation maps each domain element to exactly one codomain element
- `"partial function"` iff the relation maps some (but not all) domain elements to codomain elements, without duplication
- `"not a function"` iff any domain element maps to more than one codomain element

The Python function you write must pass all tests. Note that the elements of each set can be either an integer or a string. You can see this in the type hints in the function definition. For example, `domain: set[int | str]`. The vertical `|` represents a logical _or_ and indicates that _either type_ is allowed,  so the Python variable `domain` must be a set containing either integers or strings.

**Complete the Python function** in `classify_function.py` so that it passes each test. When you push your code to GitHub Classroom, the auto-grader will run all tests in the following files to determine your score:
- `test_classify_function.py`
- `test_classify_function_typecheck.py`

The `test_classify_function.py` file provides some positive tests including the edge cases above. The other file does type-checking. We'll have more to say about type-checking shortly.

You can run all the tests in the project with `pytest`, or you can use the **Testing panel** in VS Code.

Once you have a working solution, you can **commit your code to GitHub Classroom** and use the process from Homework 1 to confirm that your code passes the auto-grading. Don't spend too much time on this problem if you get hung up on it. Here are the point allocations:
- 2 points if you pass all the tests in `test_classify_function.py`
- 2 points if you pass all the tests in `test_classify_function_typechecks.py`

---

## 4. mypy: Static Type Checking
You probably thought writing all the type-checking hints was a bit of a pain, even though you probably believe that adding those hints is a good practice in general.  We'll now discuss a tool that you can use to check types.

`mypy` is a **static type checker** for Python. Instead of waiting for tests to fail when you run `pytest`, `mypy` analyzes your code and flags type errors **before** execution. In this course, we use `mypy` so you can write *fewer* type-checking tests while still getting strong guarantees about your code. `mypy` will be required for all projects.

### 4.1 Why use mypy?

- Catches type mismatches early (e.g., wrong element types in a set of tuples)
- Documents the intent of the programmer for the code usage making it easier to use and maintain the code through its lifecycle
- Reduces the need for many runtime type-checking tests
- Plays well with VS Code (inline diagnostics, quick jumps)

Bottom line, type checkers reduce code defects that lead to emergent, unexpected, behavior and make it easier to maintain code through its lifecycle especially code that is touched by teams of developers.

### 4.2 How to run mypy

From the project root (with your virtual environment activated):

```bash
mypy .
```

You will see an output that looks something like the following
```text
src/homework2/score_keeper.py:2: error: Function is missing a return type annotation  [no-untyped-def]

src/homework2/score_keeper.py:2: note: Use "-> None" if function does not return a value

src/homework2/score_keeper.py:6: error: Function is missing a type annotation  [no-untyped-def]

Found 2 errors in 1 file (checked 3 source files)
```

We intentionally put type errors into the `score_keeper.py` file. `mypy` prints out those errors. The next section talks about those errors and how to correct them.

### 4.3 Example: What mypy reports without type hints

**1. Open `score_keeper.py`**

The file `score_keeper.py` currently contains:

```python
class ScoreKeeper:
    def __init__(self):
        self.multiplier = 1  # used in calculation
        self.total_score = 0  # altered in method

    def add_points(self, points):
        """
        Add points multiplied by self.multiplier to total_score.
        Return the amount of points added in this call.
        """
        added_points = points * self.multiplier
        self.total_score += added_points
        return added_points
```

In VS Code, you should see red squiggly lines under the code where type hints are missing. Those lines tell you where mypy found type errors. The squiggly lines provide the same information that was printed out when you ran `mypy` from the command line.

Mouse over the squiggly line under
```python
   def __init__(self):
```
You should see something like
```text
Function is missing a return type annotation Mypyno-untyped-def

Use "-> None" if function does not return a valueMypy
(method) def __init__(self: Self@ScoreKeeper) -> None
```
This error is telling you that every function needs to return something.



**2. Add Type Hint for the Return Types**

If the function is not intended to return a type, then you use `-> None` to indicate that you don't intend to return a type. Change the definition of `__init__` to be
```python
    def __init__(self) -> None:
        self.multiplier = 1  # used in calculation
        self.total_score = 0  # altered in method
```
All the squiggly lines for the function have disappeared. Rerun `mypy .` from the integrated terminal. You'll see one fewer error than before.

Now mouse over the `add_points` function and notice the error `Function is missing a type annotation`. We want this function to return an integer, so add `-> int` to the function definition,
```python
  def add_points(self, points) -> int:
        """
        Add points multiplied by self.multiplier to total_score.
        Return the amount of points added in this call.
        """
        added_points = points * self.multiplier
        self.total_score += added_points
        return added_points
```
The red squiggly line didn't go away, and running `mypy .` still returns more errors than before. This just means that you fixed the error on the return type of the function, but still need to define types for the function arguments.

The error message said that you missed a type definition for one of the function arguments. Modify the code to be

```python
    def add_points(self, points: int) -> int:
        """
        Add points multiplied by self.multiplier to total_score.
        Return the amount of points added in this call.
        """
        added_points = points * self.multiplier
        self.total_score += added_points
        return added_points
```
The red squiggly lines went away and running `mypy .` returned something like
```text
Success: no issues found in 3 source files
```

`mypy` makes some inferences about types, and the next section uncovers one of those inferences.

**3. Introduce a Type Error**

Now, let's see `mypy` catch a type mismatch. Change:

```python
self.multiplier = 1
```

to:

```python
self.multiplier = 1.0
```

You should see some squiggly red lines reappear, and if you run `mypy .` again you'll see something like

```
src/homework2/score_keeper.py:12: error: Incompatible types in assignment (expression has type "float", variable has type "int")  [assignment]

src/homework2/score_keeper.py:13: error: Incompatible return value type (got "float", expected "int")  [return-value]

Found 2 errors in 1 file (checked 3 source files)
```

When you declared in the function definition `add_points` that the `points` variable was a type `int`, `mypy` infers that the product
```python
        added_points = points * self.multiplier
```
will use integer multiplication. But`self.multiplier = 1.0` indicates that one of the arguments in the multiplication is a float.

`mypy` correctly detects that you are assigning a `float` to a variable annotated as an `int`.

The inference made by mypy is that the type for `added_points` and `self.total_score` were integers because they operated on the `points` variable, which we stated was an integer.


By using `mypy` in this way, you can catch type problems before running your tests, reducing runtime errors and improving code clarity.


---

## 5. Methods, Side Effects, and Mathematical Functions

We've defined **mathematical functions** as mappings from a domain to a codomain. This means that inputs go in and outputs come out, without hidden behavior (side effects). But many Python objects use **methods**, which can hide both inputs and outputs inside the object.

### 5.1 Example: Method with a Side Effect
Look at the `ScoreKeeper` class definition
```python
class ScoreKeeper:
    def __init__(self) -> None:
        self.multiplier = 1  # used in calculation
        self.total_score = 0  # altered in method

    def add_points(self, points: int) -> int:
        """
        Add points multiplied by self.multiplier to total_score.
        Return the amount of points added in this call.
        """
        added_points = points * self.multiplier
        self.total_score += added_points
        return added_points
```
and notice the two **class member variables**
1. `self.multiplier`
1. `self.total_score`
`ScoreKeeper` uses `self.multiplier` to compute the function and output. Additionally, `ScoreKeeper` keeps a running tally of the total score even though the function only returns the `added_points`.

Mathematically, the mapping in `add_points` isn't just a mapping from the points given input to the function to the points added to the score. It includes the parameter `self.multiplier` that is used to compute the added points. Additionally, it uses the current total score, `self.total_score` to compute a new value for the total score via
```python
        self.total_score += added_points
```
This means that the domain is made up of tuples of integers
```
(points, self.multiplier, self.total_score)
```

Something similar is happening on the output of the function. The codomain is also made up of tuples
```
(added_points, self.total_score)
```
The technical term for the change in a class variable that isn't explicit in the return from the function is **side effect**. Stated simply, a **side effect** is a change to some hidden variable that is not explicitly returned by the function.

Thus, the `add_points` function maps

```
(points, self.multiplier, self.total_score) ↦ (added_points, self.total_score)
```

- **Domain**: triples `(points, self.multiplier, self.total_score)`
- **Codomain**: pairs `(added_points, self.total_score)`

### 5.2 Why This Matters

Hidden state changes (side effects) can cause defects, especially across multiple calls or shared objects. One reason that defects can appear is that it is not always clear what side effects are occurring, and that means the programmer can forget and make a mistake. More critically, the behavior of the function changes over time because it side-effects hidden state. That means that it doesn't always return the same thing when given the same arguments because of the role of the hidden state.

### 5.3 Functional Programming
There are good reasons for programmers to use hidden state, like when we want to use a variable that is global for an entire class. In fact, that is one of the benefits of object-oriented programming. So we are not arguing that you should never do this.

Instead, we are showing a programming style that is more **function-based**, which means that the domain and codomain of the function are always explicit in the input arguments and return values. Most of the **starter code** for this class will avoid having side effects. For some of you, this will be a bit awkward because it requires the code to be explicit about the codomain at all times.

---

## 6. Testing Methods that Use Object State

When testing methods that modify object state **and** return values, you need to check both the explicit and implicit outputs.

### 6.1 Example
For example, the `ScoreKeeper` function uses `self.multiplier` as part of its input, `self.total_score` as part of its input, and it modifies both `added_points` and `self.total_score` as part of its output. We need to write tests that work for all elements of the domain and codomain.

Let's write a test. Begin by doing the math first. Suppose that the current total score is 10 and the multiplier is set to 3. Then an input of 2 points should yield

| Expression       |   =   | Result               |
|------------------|-------|----------------------|
| `added_points`     |   =   | (`points`)(`multiplier`) |
|                  |   =   | (2)(3)               |
|                  |   =   | 6                    |

Therefore, `add_points(2)` should return `6` and update `total_score` to `16`.

The current total score is computed as

| Expression        |   =   | Result                                |
|-------------------|-------|---------------------------------------|
| `new_total_score`   |   =   | `old_total_score` + (`points`)(`multiplier`) |
|                   |   =   | 10 + (2)(3)                           |
|                   |   =   | 16                                    |

```python
def test_add_points() -> None:
    # Step 1: Instantiate
    score_keeper_object = ScoreKeeper()

    ###############################
    ## Specify inputs from domain #
    ###############################
    # Step 3: Specify the input
    input = 2
    # Step 4: Set state in the object
    score_keeper_object.total_score = 10
    score_keeper_object.multiplier = 3

    #########################################
    ## Specify expected outputs in codomain #
    #########################################
    # Step 5: Specify expected number of points returned by function
    expected_return = 6
    # Step 6: Specify expected change in internal state
    expected_total_score = 16

    # Step 7: Call object method
    returned = score_keeper_object.add_points(input)

    #######################################
    ## Check values returned by function ##
    #######################################
    # Step 8: Check return value
    assert returned == expected_return
    # Step 9: Check modified state
    assert score_keeper_object.total_score == expected_total_score

```

When we run `pytest` either from the command line
```bash
tests/test_score_keeper.py
```
or from within the Testing Panel, we see that the test passed.

### 6.2 Summary of Writing Tests with Object State

When testing **methods that use and modify object state**, you need to account for both *explicit outputs* (the values the method returns) and *implicit outputs* (the changes made to the object’s internal state).  This is especially  important in object-oriented code, where methods often both return values and mutate state.

A good test should:

1. **Instantiate the object** – Create a fresh instance of the class so that you have full control over its state.
2. **Specify the inputs (domain elements)** – Set both:
   - the explicit method argument(s), and
   - any hidden inputs stored in member variables.
3. **Specify the expected outputs (codomain elements)** – Write down what you expect the method to return *and* what you expect the internal state to become after the method runs.
4. **Call the method** – Execute the method with the specified input.
5. **Assert on the explicit output** – Compare the return value with your expected result.
6. **Assert on the implicit output** – Compare the modified internal state (object fields) with your expected result.

In other words:

- **Return values** correspond to the *visible* outputs of the function.
- **State changes** correspond to the *hidden* outputs of the function.

Both must be tested to ensure correctness.

> *Tip*: Do the math or logic on paper before you write the code. This math or logic should compute both the return value and the updated state. That way, your test documents not only what your code does, but also the reasoning behind why those results are correct. This is called **test-driven development** (TDD).
