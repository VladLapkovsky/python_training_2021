"""Implement a function, that receives changeable number of dictionaries and combines them into one dictionary.

Keys - letters, values - numbers. Dict values should be summarized in case of identical keys.

dict_1 = {"a": 100, "b": 200}
dict_2 = {"a": 200, "c": 300}
dict_3 = {"a": 300, "d": 100}

print(combine_dicts(dict_1, dict_2))
{"a": 300, "b": 200, "c": 300}


print(combine_dicts(dict_1, dict_2, dict_3))
{"a": 600, "b": 200, "c": 300, "d": 100}
"""
from collections import defaultdict


def combine_dicts(*args) -> dict:
    result_dict = defaultdict(int)
    for dct in args:
        for key_dct, value_dct in dct.items():
            result_dict[key_dct] += value_dct
    return dict(result_dict)


if __name__ == "__main__":
    dict_1 = {"a": 100, "b": 200}
    dict_2 = {"a": 200, "c": 300}
    dict_3 = {"a": 300, "d": 100}
    print(combine_dicts(dict_1, dict_2))
    #  {"a": 300, "b": 200, "c": 300}.
    print(combine_dicts(dict_1, dict_2, dict_3))
    #  {"a": 600, "b": 200, "c": 300, "d": 100}.
