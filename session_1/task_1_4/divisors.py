"""This module accepts a number from input and prints a list of all its divisors."""


from math import sqrt


def get_divisors(number: int) -> list:
    """Accept the number and return a list of all its divisors without using the `sort` function.

    Parameters:
        number: the number from which you want to get the divisors

    Returns:
        list of number divisors
    """
    divisors_list = []
    for num in range(1, int(sqrt(number) + 1)):
        if number % num == 0:
            divisors_list.append(num)
            if num != number // num:
                divisors_list.append(number // num)
    return sorted(divisors_list)


def main():
    """Accept the number from input, send it to the get_divisors function and print the result of it."""
    number = int(input("Input number to get it's divisors: "))
    divisors = get_divisors(number)
    print(divisors)


if __name__ == "__main__":
    main()
