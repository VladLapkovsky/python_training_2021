"""This module provides one function based decorator which runs a function or method once.

Functions:
    call_once(func)
"""


def call_once(func):
    """Run function once and cash its last result.

    Launch "_cashing" function, which cash result of decorated function
    and runs decorated function only one time. When the decorated function called again,
    it returns cashed result.

    Parameters:
        func: function it decorates

    Returns:
        last result of the decorated function
    """

    def _cashing(*args, **kwargs):
        if _cashing.result is None:
            _cashing.result = func(*args, **kwargs)
        return _cashing.result

    _cashing.result = None
    return _cashing


@call_once
def sum_of_numbers(first_elem, second_elem):
    return first_elem + second_elem


class TestClass:
    def __init__(self):
        self.test_value = 2

    @call_once
    def func(self):
        self.test_value = self.test_value * 2
        return self.test_value


def main():
    """Test call_once decorator on method func in class TestClass and on function sum_of_numbers."""
    test_variable = TestClass()
    print(test_variable.func())
    print(test_variable.func())
    print(test_variable.func())
    print()

    print(sum_of_numbers(13, 42))
    # >> > 55
    print(sum_of_numbers(999, 100))
    # >> > 55
    print(sum_of_numbers(134, 412))
    # >> > 55
    print(sum_of_numbers(856, 232))
    # >> > 55


if __name__ == "__main__":
    main()
