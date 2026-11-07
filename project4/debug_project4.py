import sys  # noqa

sys.argv = ["project4", "arg1"]

from project4.project4 import project4cli  # noqa

if __name__ == "__main__":
    project4cli()
