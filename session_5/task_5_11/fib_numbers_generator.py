"""Task 7.11.

Implement a generator which will generate Fibonacci numbers endlessly.

Example:
gen = endless_fib_generator()
while True:
print(next(gen))
1 1 2 3 5 8 13
"""
import time


def generate_fib_numbers(sleep_time):
    previous, current = 0, 1
    while True:
        yield current
        time.sleep(sleep_time)
        previous, current = current, previous + current


def main():
    gen = generate_fib_numbers(0.2)
    while True:
        print(next(gen))


if __name__ == "__main__":
    main()
