"""Implement a function "get_pairs(lst: list) -> list" which returns a list of tuples containing pairs of elements.

Pairs should be formed as in the
example. If there is only one element in the list return "None" instead.

Example:
get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]

get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

get_pairs([1])
None
"""


def get_pairs(lst: list) -> list:
    return list(zip(lst[:-1], lst[1:]))


if __name__ == "__main__":
    print(get_pairs([1, 2, 3, 8, 9]))
    print(get_pairs(['need', 'to', 'sleep', 'more']))
