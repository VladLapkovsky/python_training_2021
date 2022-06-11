"""This module provides a function to sorts input dictionary by its key."""


def sort_by_key(dct: dict) -> dict:
    return dict(sorted(dct.items()))


if __name__ == "__main__":
    dict_example1 = {
        2: 56,
        1: 2,
        5: 12,
        4: 24,
        3: 323,
    }
    dict_example2 = {
        "IBM": 205.55,
        "HPQ": 37.2,
        "ZOO": 1,
        "FB": 10.75,
        "ACME": 45.23,
        "AAPL": 612.78,
    }
    print(sort_by_key(dict_example1))
    print(sort_by_key(dict_example2))
