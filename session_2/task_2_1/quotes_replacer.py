"""Implement a function which receives a string and replaces all `"` symbols with `'` and vise versa."""


def replace_quotes(input_str: str) -> str:
    new_string = ""
    for char in input_str:
        if char == "\"":
            new_string += "\'"
        elif char == "\'":
            new_string += "\""
        else:
            new_string += char
    return new_string


def main():
    s_1 = "It's'\"\"\'"
    s_2 = "It\"s"
    s_3 = "I\"t\'s"
    s_4 = "Its"
    print(replace_quotes(s_1))
    print(replace_quotes(s_2))
    print(replace_quotes(s_3))
    print(replace_quotes(s_4))


if __name__ == "__main__":
    main()
