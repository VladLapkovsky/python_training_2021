"""This module provides a function to get integer from tuple.

Given tuple must contain positive integers.

Examples:
Input: (1, 2, 3, 4)
Output: 1234
"""


def convert_to_int(tpl: tuple) -> int:
    return int("".join(str(num) for num in tpl))


if __name__ == "__main__":
    example_tuple = (1, 2, 3, 4)
    res = convert_to_int(example_tuple)
    print(res, type(res))
