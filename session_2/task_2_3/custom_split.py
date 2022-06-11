"""Implement a function which works the same as `str.split` method (without using `str.split` itself, ofcourse)."""


def split(input_str: str, sep=" ") -> list:
    result_list = []
    sep_flag = sep.isspace()
    if sep_flag:
        input_str = input_str.strip()
    flag_index = 0
    for index, char in enumerate(input_str):
        if char == sep:
            str_split = input_str[flag_index:index]
            if str_split or not sep_flag:
                result_list.append(str_split)
            flag_index = index + 1
    result_list.append(input_str[flag_index:])
    return result_list


if __name__ == "__main__":
    my_str = "        str safaf *      "
    print(repr(my_str))
    print(my_str.split())
    print(split(my_str))
    print(my_str.split(","))
    print(split(my_str, sep=","))
    print()
    my_str = "1,2,,3,"
    print(repr(my_str))
    print(my_str.split())
    print(split(my_str))
    print(my_str.split(","))
    print(split(my_str, sep=","))
    print()
    my_str = " 1 ,2, , 3,"
    print(repr(my_str))
    print(my_str.split())
    print(split(my_str))
    print(my_str.split(","))
    print(split(my_str, sep=","))
    print()
    my_str = " 1    2,    3   "
    print(repr(my_str))
    print(my_str.split())
    print(split(my_str))
    print(my_str.split(","))
    print(split(my_str, sep=","))
    print()
    my_str = "1,2,, 3,"
    print(repr(my_str))
    print(my_str.split())
    print(split(my_str))
    print(my_str.split(","))
    print(split(my_str, sep=","))
    print()
    my_str = "   1   2   3   "
    print(repr(my_str))
    print(my_str.split())
    print(split(my_str))
    print(my_str.split(","))
    print(split(my_str, sep=","))
    print()
