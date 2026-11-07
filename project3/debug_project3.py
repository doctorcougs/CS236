import sys  # noqa

sys.argv = ["project3", "arg1"]

from project3.project3 import project3cli  # noqa

if __name__ == "__main__":
    project3cli()
