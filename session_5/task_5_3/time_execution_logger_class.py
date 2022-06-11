"""Task 7.3.

Implement decorator with context manager support for writing execution time to log-file. See contextlib module.
"""

import time
from contextlib import ContextDecorator


class time_execution_logger(ContextDecorator):
    def __init__(self, log_file):
        self.log_file = log_file

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, exc_type, exc, exc_tb):
        log_file = open(self.log_file, mode="a")
        log_file.write(
            f"Function was completed in {time.perf_counter() - self.start:.5f} sec\n",
        )
        log_file.close()
        return True


@time_execution_logger("log_file.txt")
def pow_func(first, second):
    return first ** second


def mul_func(first, second):
    return first * second


def main():
    print(pow_func(100000, 2000))

    with time_execution_logger("log_file.txt"):
        print(mul_func(100000, 2000))


if __name__ == "__main__":
    main()
