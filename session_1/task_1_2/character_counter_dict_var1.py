"""This module provides a function to count the number of characters in a string.

Case of letters is ignored.

Example:
    Input: "Oh, it is python"
    Output: {",": 1, " ": 3, "o": 2, "h": 2, "i": 2, "t": 2, "s": 1, "p": 1, "y": 1, "n": 1}
"""


from session_1.type_assertor import type_assert


@type_assert(str)
def count_chars(input_str: str) -> dict:
    """Calculate the number of characters in a string.

    Parameters:
        input_str: the string in which you want calculate the number of characters

    Returns:
        the length of a string
    """
    frequency = {}
    for char in input_str.lower():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


if __name__ == "__main__":
    print(count_chars("Oh, it is python"))
    print(count_chars("HeLLo wOrLd"))
    print(count_chars(""))
