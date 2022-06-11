"""Implement a function foo(List[int]) -> List[int].

It's given a list of integers, return a new list such that each element at index "i" of the new list
is the product of all the numbers in the original array except the one at "i".

Example:
foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

foo([3, 2, 1])
[2, 3, 6]
"""

from math import prod


def foo(input_lst: list) -> list:
    return [prod(input_lst) // num for num in input_lst]


if __name__ == "__main__":
    print(foo([1, 2, 3, 4, 5]))
    print(foo([3, 2, 1]))
