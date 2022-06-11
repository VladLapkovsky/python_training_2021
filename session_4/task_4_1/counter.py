"""This module provides one class to increment incoming values.

Class:
    Counter
"""


class Counter:
    """A class to increment incoming values.

    If the start value is not specified the counter begin with 0.
    If the stop value is not specified it counting up infinitely.
    If the counter reaches the stop value, it prints "Maximal value is reached."
    """

    def __init__(self, start=0, stop=None):
        """Accept the start value and the counter stop value.

        Parameters:
            start: start value
            stop: value to stop incrementing
        """
        self.start = start
        self.stop = stop

    def increment(self):
        """Increment start value until reaching stop value.

        If start < stop then start += 1; else only print("Maximal value is reached.").

        Raises:
            ValueError: raise when maximal value is reached
        """
        if self.stop is None or self.start < self.stop:
            self.start += 1
        else:
            raise ValueError("Maximal value is reached.")
            # print("Maximal value is reached."):

    def get(self):
        """Return actual start value.

        Returns:
            start value
        """
        return self.start


def main():
    """Test Counter class."""
    first = Counter(start=42)
    first.increment()
    print("first =", first.get())
    first.increment()
    print("first =", first.get())

    print()

    second = Counter()
    print("second =", second.get())
    second.increment()
    print("second =", second.get())
    second.increment()
    print("second =", second.get())

    print()

    third = Counter(start=42, stop=43)
    third.increment()
    print("third =", third.get())
    third.increment()
    print("third =", third.get())

    print()

    fourth = Counter(start=-2, stop=0)
    fourth.increment()
    print("fourth =", fourth.get())
    fourth.increment()
    print("fourth =", fourth.get())
    fourth.increment()
    print("fourth =", fourth.get())


if __name__ == "__main__":
    main()
