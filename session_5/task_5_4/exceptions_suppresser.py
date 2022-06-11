"""Task 7.4.

Implement decorator for suppressing exceptions. If exception not occur write log to console.
"""

from functools import wraps


def suppress_exceptions(func):
    filename = "log_file.txt"

    @wraps(func)
    def wrapped(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception:
            pass
        else:
            log_file = open(filename, "a")
            log_file.write(f"There were no exceptions in '{func.__name__}' function\n")
            return res

    return wrapped


@suppress_exceptions
def zero_division():
    print("hello")
    # raise ZeroDivisionError


def main():
    zero_division()


if __name__ == "__main__":
    main()
