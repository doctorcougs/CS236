import sys  # noqa

sys.argv = ["project5", "arg1"]

from project5.project5 import project5cli  # noqa

if __name__ == "__main__":
    project5cli()
