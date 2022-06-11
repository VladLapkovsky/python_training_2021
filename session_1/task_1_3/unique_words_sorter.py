"""This module accepts comma separated sequence of words and prints the unique words in sorted form.

Example:
    Input: ['red', 'white', 'black', 'red', 'green', 'black']
    Output: ['black', 'green', 'red', 'white']
"""


def transform_to_unique_sorted_items(comma_separated_sequence: str) -> list:
    """Accept comma separated sequence of words and return sorted unique items.

    Parameters:
        comma_separated_sequence: comma separated sequence of words

    Returns:
        list of sorted unique items
    """
    sequence_list = comma_separated_sequence.split(",")
    return sorted(set(sequence_list))


def main():
    """Accept the string from input, send it to the get_unique_sorted_items function and print the result of it."""
    words = input("Write comma separated sequence of words: ")
    sorted_unique_word_list = transform_to_unique_sorted_items(words)
    print(sorted_unique_word_list)


if __name__ == "__main__":
    main()
