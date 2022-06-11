"""This module provides a function, which gets list of dictionaries and returns set of its values.

Examples:
Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Output: {"S005", "S002", "S007", "S001", "S009"}
"""


def get_unique_values(list_of_dct: list) -> set:
    return {list(dct.values())[0] for dct in list_of_dct}


if __name__ == "__main__":
    example_list = [
        {"V": "S001"},
        {"V": "S002"},
        {"VI": "S001"},
        {"VI": "S005"},
        {"VII": "S005"},
        {"V": "S009"},
        {"VIII": "S007"},
    ]
    print(get_unique_values(example_list))
