import sys  # noqa

sys.argv = ["project1", "arg1"]

from project1.project1 import project1cli  # noqa

if __name__ == "__main__":
    project1cli()
