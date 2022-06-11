"""This module provides one function to search for most common words in the file.

It uses collections and re modules.

Functions:
    most_common_words(filepath, umber_of_words=3)
"""

from collections import Counter
from re import findall


def most_common_words(filepath, number_of_words=3):
    """Search for the most common words in the file.

    Parameters:
        filepath: path to the file.
        number_of_words: number of most common words in the result list.

    Returns:
        A list of the most common words like -> ["word", "word", "word", ].
    """
    with open(filepath, "r") as input_file:
        pattern = r"\w+"  # \w+ == words only
        # getting list like [(word, count), (word, count), ...]:
        words_collection = Counter(findall(pattern, input_file.read()))
        return [words[0] for words in words_collection.most_common(number_of_words)]


if __name__ == "__main__":
    INPUT_FILE = "lorem_ipsum.txt"
    print(most_common_words(INPUT_FILE, 5))
