"""Task 7.8.

Implement your custom iterator class.
It should be called MySquareIterator and gives squares of elements of collection it iterates through.
Example:
lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for item in itr:
print(item)
1 4 9 16 25
"""


class MySquareIterator:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        self.start_iter = -1
        self.stop_iter = len(self.collection) - 1
        return self

    def __next__(self):
        if self.start_iter < self.stop_iter:
            self.start_iter += 1
            return self.collection[self.start_iter] ** 2
        else:
            raise StopIteration


def main():
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item, end=" ")
    # 1 4 9 16 25


if __name__ == "__main__":
    main()
