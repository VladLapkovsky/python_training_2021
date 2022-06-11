"""Task 7.2.

Implement context manager for opening and working with file,
including handling exceptions with @contextmanager decorator.
"""

from contextlib import contextmanager


@contextmanager
def file_opener(filename, mode="r"):
    file_obj = None
    try:
        file_obj = open(filename, mode=mode)
        yield file_obj
    except Exception as error:
        print("An exception occurred in your with block:", error.__class__.__name__)
        print("Exception message:", error)
    finally:
        if file_obj:
            file_obj.close()


def main():
    with file_opener("test_file.txt", "w") as input_file:
        # print(input_file.read())
        input_file.read("hello")


if __name__ == "__main__":
    main()
