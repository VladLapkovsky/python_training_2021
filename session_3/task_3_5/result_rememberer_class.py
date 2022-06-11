"""This module provides one class-based decorator to remember last result of function it decorates.

Class:
    RememberResult
"""


class RememberResult:
    """Remember last result of function it decorates and print it before next call.

    A class based decorator. Launch "__call__" method every time when decorated function called.
    Then print last result of decorated function (first value = None),
    launch decorated function and return its result.
    """

    def __init__(self, func):
        """Initiate last_result = None.

        Parameters:
            func: decorated function
        """
        self.last_result = None
        self.func = func

    def __call__(self, *args):
        """Magic method which launched every time when decorated function called.

        Print last result of the decorated function, launch decorated function and return its result.

        Parameters:
            args: arguments of the decorated functions

        Returns:
            last result of the decorated function
        """
        print(f"Last result = '{self.last_result}'")
        self.last_result = self.func(*args)
        return self.last_result


@RememberResult
def sum_list(*args):
    """Sum args. Args must be one type.

    Parameters:
        args: arguments

    Returns:
        res
    """
    res = ""
    for elem in args:
        if isinstance(elem, int):
            res = sum(args)
            break
        res += elem
    print(f"Current result = '{res}'")
    return res


def main():
    """Test RememberResult decorator on sum_list function."""
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)


if __name__ == "__main__":
    main()
