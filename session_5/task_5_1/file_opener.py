"""Task 7.1.

Implement class-based context manager for opening and working with file, including handling exceptions.
Do not use "with open()". Pass filename and mode via constructor.
"""


class FileOpener:
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode
        self.file_obj = None

    def __enter__(self):
        try:
            self.file_obj = open(self.filename, mode=self.mode)
        except FileNotFoundError as error:
            print(error)
        else:
            return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()
        if exc_type is not None:
            print("An exception occurred in your with block:", exc_type)
            print("Exception message:", exc_val)
            print("Traceback:", exc_tb)
        return True


def main():
    with FileOpener("test_file.txt", "r") as input_file:
        # print(input_file.read())
        input_file.read("hello world")


if __name__ == "__main__":
    main()
