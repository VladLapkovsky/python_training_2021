r"""Implement a bunch of functions which receive a changeable number of strings and return next parameters.

1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
4) characters of alphabet, that were not used in any string

Note: use "string.ascii_lowercase" for list of alphabet letters
test_strings = ["hello", "world", "python", ]
print(test_1_1(\*strings))
{"o"}
print(test_1_2(\*strings))
{"d", "e", "h", "l", "n", "o", "p", "r", "t", "w", "y"}
print(test_1_3(\*strings))
{"h", "l", "o"}
print(test_1_4(\*strings))
{"a", "b", "c", "f", "g", "i", "j", "k", "m", "q", "s", "u", "v", "x", "z"}
"""


import string


def test_1_4(*args):
    set_result = set(string.ascii_lowercase)
    for elem in args:
        set_result = set_result.difference(elem)
    return set_result


def test_1_3(*args):
    set_result = set()
    first_elem = set(args[0])
    for elem in args[1:]:
        set_result.update(first_elem.intersection(elem))
    return set_result


def test_1_2(*args) -> set:
    set_result = set(args[0])
    for elem in args[1:]:
        set_result = set_result.union(elem)
    return set_result


def test_1_1(*args) -> set:
    set_result = set(args[0])
    for elem in args[1:]:
        set_result = set_result.intersection(elem)
    return set_result


if __name__ == "__main__":
    test_strings = ["hello", "world", "python"]
    print(test_1_1(*test_strings))
    print(test_1_2(*test_strings))
    print(test_1_3(*test_strings))
    print(test_1_4(*test_strings))
