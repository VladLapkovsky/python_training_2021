"""Implement a function that takes a number as an argument and returns a dictionary.

The key is a number and the value is the square of that number.

print(generate_squares(5))
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""


def generate_squares(num: int) -> dict:
    return {number: number ** 2 for number in range(1, num + 1)}


if __name__ == "__main__":
    print(generate_squares(5))
