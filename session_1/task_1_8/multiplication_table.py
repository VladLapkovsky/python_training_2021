"""This module provides a functions to pretty print of a part of the multiplication table.

Examples:
    Input:
        a = 2
        b = 4
        c = 3
        d = 7
    Output:
            3	4	5	6	7
        2	6	8	10	12	14
        3	9	12	15	18	21
        4	12	16	20	24	28

"""
NUMBER_SEP = "\t"


def print_multiplication_table(a, b, c, d):
    print(NUMBER_SEP, end="")
    print(*range(c, d + 1), sep=NUMBER_SEP)
    for num_row in range(a, b + 1):
        print(num_row, end=NUMBER_SEP)
        for num_column in range(c, d + 1):
            print(num_row * num_column, end=NUMBER_SEP)
        print()


def get_values() -> list:
    lst = []
    chars = ["a", "b", "c", "d"]
    print('Input size of multiplication table (values must be greater than zero):')
    for char in chars:
        lst.append(int(input(f"{char} = ")))
    return lst


def main():
    a, b, c, d = get_values()
    if a < b and c < d:
        print_multiplication_table(a, b, c, d)
    else:
        print("'a' must be lower than 'b' and 'c' must lower than 'd'")


if __name__ == "__main__":
    main()
