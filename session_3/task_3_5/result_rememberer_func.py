"""This module provides one function-based decorator to remember last result of function it decorates.

Functions:
    remember_result(func)
"""


def remember_result(func):
    """Remember last result of function it decorates and print it before next call.

    A function based decorator. Launch "_last_result" function every time when decorated function called.
    Then print last result of decorated function (first value = None),
    launch decorated function and return its result.

    Parameters:
        func: function it decorates

    Returns:
        last result of the decorated function
    """

    def _last_result(*args):
        print(f"Last result = '{_last_result.cash}'")
        _last_result.cash = func(*args)
        return _last_result.cash

    _last_result.cash = None
    return _last_result


@remember_result
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
    """Test remember_result decorator on sum_list function."""
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)


if __name__ == "__main__":
    main()
