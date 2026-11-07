import sys  # noqa

sys.argv = ["project2", "arg1"]

from project2.project2 import project2cli  # noqa

if __name__ == "__main__":
    project2cli()
