"""Task 7.10.

Implement a generator which will generate odd numbers endlessly.

Example:
gen = endless_generator()
while True:
print(next(gen))
1 3 5 7 ... 128736187263 128736187265 ...
"""


def generate_odd_numbers():
    start = 1
    while True:
        yield start
        start += 2


def main():
    gen = generate_odd_numbers()
    while True:
        print(next(gen))


if __name__ == "__main__":
    main()
