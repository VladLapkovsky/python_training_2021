"""Implement a function `split_by_index which splits the `s` string by indexes specified in indexes.

Wrong indexes must be ignored.
Examples:
split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

split_by_index("no luck", [42])
["no luck"]
"""


def split_by_index(input_str: str, indexes: list) -> list:
    result_list = []
    flag_index = 0
    for index in indexes:
        result_list.append(input_str[flag_index:index])
        flag_index = index
    str_split = input_str[flag_index:]
    if str_split:
        result_list.append(str_split)
    return result_list


if __name__ == "__main__":
    print(["python", "is", "cool", ",", "isn't", "it?"])
    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18, 50]))
    print()
    print(["no luck"])
    print(split_by_index("no luck", [42]))
    print(split_by_index("no luck", [2, 4, 42]))
