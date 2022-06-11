"""Task 7.9.

Implement an iterator class EvenRange.
It accepts start and end of the interval as an init arguments and gives only even numbers during iteration.
If user tries to iterate after it gave all possible numbers "Out of numbers!" should be printed.
Note: Do not use function "range()" at all.

Example:
er1 = EvenRange(7,11)
next(er1)
8
next(er1)
10
next(er1)
"Out of numbers!"
next(er1)
"Out of numbers!"
er2 = EvenRange(3, 14)
for number in er2:
print(number)
4 6 8 10 12 "Out of numbers!"
"""


class EvenRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

        self._for_flag = False
        self._flag_index = 1

    def __iter__(self):
        self._for_flag = True
        return self

    def __next__(self):
        if self.start < self.end:
            if self.start % 2 != 0:
                self.start += 1
            if self.start != self.end:
                self.start += 1
                return self.start - 1
        if self._flag_index:
            if not self._for_flag:
                return "Out of numbers!"
            self._flag_index = 0
            return "Out of numbers!"
        raise StopIteration


def main():
    er1 = EvenRange(7, 11)
    n = next(er1)
    print(n)
    # 8
    n = next(er1)
    print(n)
    # 10
    print(next(er1))
    # "Out of numbers!"
    print(next(er1))
    # "Out of numbers!"

    er2 = EvenRange(3, 14)
    for number in er2:
        print(number, end=" ")
    # 4 6 8 10 12 "Out of numbers!"


if __name__ == "__main__":
    main()
