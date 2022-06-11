"""This module provides a function to calculate the length of a string without using the `len` function."""
from session_1.type_assertor import type_assert


@type_assert(str)
def calculate_len(input_str: str) -> int:
    """Calculate the length of a string.

    Parameters:
        input_str: the string in which you want calculate the length

    Returns:
        the length of a string
    """
    if input_str:
        return sum(1 for elem in input_str)
    return 0


if __name__ == "__main__":
    print(calculate_len("hello world"))
    print(calculate_len("-1"))
    print(calculate_len(""))
    print(calculate_len(5))
