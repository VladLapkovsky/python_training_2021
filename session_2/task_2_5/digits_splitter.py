"""Implement a function get_digits(num: int) -> Tuple[int] which returns a tuple of a given integer's digits.

Example:
split_by_index(87178291199
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
"""


def get_digits(num: int) -> tuple:
    return tuple(int(num) for num in str(num))


if __name__ == "__main__":
    print(get_digits(87178291199))
