# type: ignore
import os

from project2.project2 import project2 as compute  # type: ignore[import-untyped]

_TEST_FUNC = compute
_TEST_ROOT_DIR = "./tests/resources/project2-passoff/"
_ANSWER_PREFIX = "answer"
_ANSWER_EXTENSION = ".txt"
_INPUT_PREFIX = "input"
_INPUT_EXTENSION = ".txt"


def _get_file_paths(bucket: int, test_index: int) -> tuple[str, str]:
    test_dir = _TEST_ROOT_DIR + str(bucket)
    input_name = _INPUT_PREFIX + str(test_index) + _INPUT_EXTENSION
    answer_name = _ANSWER_PREFIX + str(test_index) + _ANSWER_EXTENSION
    input_file = os.path.join(test_dir, input_name)
    answer_file = os.path.join(test_dir, answer_name)
    return input_file, answer_file


def _get_inputs(input_file: str, answer_file: str) -> tuple[str, str]:
    input = ""
    with open(input_file, "r") as f:
        input = f.read()
    answer = ""
    with open(answer_file, "r") as f:
        answer = f.read()
    return input, answer


def passoff(bucket: int, test_index: int) -> None:
    input_path, answer_path = _get_file_paths(bucket, test_index)
    input, answer = _get_inputs(input_path, answer_path)

    result = _TEST_FUNC(input)
    assert answer.rstrip() == result.rstrip()
