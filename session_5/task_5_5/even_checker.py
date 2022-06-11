"""Task 7.5.

Implement function for check that number is even, at least 3.
Throw different exceptions for this errors.
Custom exceptions must be derived from custom base exception(not Base Exception class).
"""


class NumberChecker(Exception):
    """Base class for other exceptions"""
    pass


class NumberNotInt(NumberChecker):
    """Raised when the input value is not integer"""
    pass


class NumberLowerThanThree(NumberChecker):
    """Raised when the input value is lower than three"""
    pass


class NumberIsComplex(NumberChecker):
    """Raised when the input value is complex"""
    pass


def check_number(number):
    try:
        number = int(number)
    except ValueError:
        raise NumberNotInt("Number must be an integer") from ValueError
    else:
        if isinstance(number, complex):
            raise NumberIsComplex("Number must be an integer")
        if number < 3:
            raise NumberLowerThanThree("Number must be greater or equal than three")
        return True


def is_even(number) -> bool:
    if check_number(number):
        return int(number) % 2 == 0


def main():
    while True:
        number = input("Enter your number ('q' for exit): ")
        if number == "q":
            break
        print(is_even(number))


if __name__ == "__main__":
    main()
