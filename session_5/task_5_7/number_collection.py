"""Task 7.7.

Implement your custom collection called MyNumberCollection. It should be able to contain only numbers.
It should NOT inherit any other collections.
If user tries to add a string or any non numerical object there, exception "TypeError" should be raised.

Method init should be able to take either "start,end,step" arguments,
where "start" - first number of collection, "end" - last number of collection or some ordered iterable
collection (see the example).

Implement following functionality:
* appending new element to the end of collection
* concatenating collections together using "+"
* when element is addressed by index(using "[]"), user should get square of the addressed element.
* when iterated using cycle "for", elements should be given normally
* user should be able to print whole collection as if it was list.
Example:
col1 = MyNumberCollection(0, 5, 2)
print(col1)
[0, 2, 4, 5]

col2 = MyNumberCollection((1,2,3,4,5))
print(col2)
[1, 2, 3, 4, 5]

col3 = MyNumberCollection((1,2,3,"4",5))
TypeError: MyNumberCollection supports only numbers!

col1.append(7)
print(col1)
[0, 2, 4, 5, 7]

col2.append("string")
TypeError: "string" - object is not a number!

print(col1 + col2)
[0, 2, 4, 5, 7, 1, 2, 3, 4, 5]

print(col1)
[0, 2, 4, 5, 7]

print(col2)
[1, 2, 3, 4, 5]

print(col2[4])
25

for item in col1:
print(item)
0 2 4 5 7
"""
from VladLapkovsky.session_7.task_7_7.type_asserter import type_assert


@type_assert(start=(int, tuple, list), end=(int, tuple, list), step=int)
class MyNumberCollection:
    def __init__(self, start=0, end=0, step=0):
        """Contain "start,end,step" arguments.

        "start" - first number of collection, "end" - last number of collection or some ordered iterable
        collection (see the example).

        Parameters:
            start: None by default
            end: None by default
            step: None by default
        """
        self.start = start
        self.end = end
        self.step = step
        self.collection = self._form_collection()

    def _form_collection(self):
        collection = []
        for attr in self.start, self.end:
            if isinstance(attr, (tuple, list)):
                collection += list(attr)
                break
            collection += [attr]
        else:
            collection = list(range(self.start, self.end, self.step))
            collection += [self.end]
        return collection

    def append(self, item_to_append):
        if not isinstance(item_to_append, int):
            raise TypeError(f'"{item_to_append}" - object is not a number!')
        self.collection.append(item_to_append)

    def __add__(self, other):
        return self.collection + other.collection

    def __repr__(self):
        return str(self.collection)

    def __getitem__(self, item):
        return self.collection[item] ** 2

    def __iter__(self):
        self.start_iter = -1
        self.stop_iter = len(self.collection) - 1
        return self

    def __next__(self):
        if self.start_iter < self.stop_iter:
            self.start_iter += 1
            return self.collection[self.start_iter]
        else:
            raise StopIteration


def main():
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)
    # [0, 2, 4, 5]

    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)
    # [1, 2, 3, 4, 5]

    col3 = MyNumberCollection(55, (1, 2, 3, 4, 5))
    print(col3)
    # [55, 1, 2, 3, 4, 5]

    # col4 = MyNumberCollection((1, 2, 3, "4", 5))
    # # TypeError: MyNumberCollection supports only numbers!
    # print(col4)

    col1.append(7)
    print(col1)
    # [0, 2, 4, 5, 7]

    # col2.append("string")
    # # TypeError: "string" - object is not a number!
    # print(col2)

    print(col1 + col2)
    # [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]

    print(col1)
    # [0, 2, 4, 5, 7]

    print(col2)
    # [1, 2, 3, 4, 5]

    print(col2[4])
    # 25

    for item in col1:
        print(item, end=" ")
    # 0 2 4 5 7


if __name__ == "__main__":
    main()
