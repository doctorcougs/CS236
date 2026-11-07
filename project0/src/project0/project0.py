# Here is the starter code for Lab 0, Hello World.

# This is going to be the structure for future projects. This function (project#()) will
# serve as your main function. It takes in one parameter, input, which is the input string
# for the test cases. It should return a string with your answer.


# If you haven't seen this syntax before, the ": str" and "-> str" are type annotations for Python.
# They just give you a clue into what type the input variable should be and the return type of the
# function respectively. It is good practice to label your functions like this unless you need the type
# to be variable.

from sys import argv


# TODO: This code should return "Hello World" plus whatever the value of "input" is.
def compute(input: str) -> str:
    # YOUR CODE GOES HERE
    return "Hello World " + input

# This function is the entry point for our package. It is the function that runs
# for the `project0` command in the integrated terminal. Try it in the terminal!
# It is configured in the `pyproject.toml` file in the `scripts` section.
def project0cli() -> None:
    if len(argv) == 2:
        print(compute(argv[1]))
    else:
        print("usage: project0 str")
