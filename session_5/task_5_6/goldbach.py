"""Task 7.6.

Create console program for proving Goldbach's conjecture.
Program accepts number for input and print result.
For pressing "q" program successfully close.
Use function from Task 7.5 for validating input, handle all exceptions and print user friendly output.
"""

from VladLapkovsky.session_7.task_7_5.even_checker import is_even
from VladLapkovsky.session_7.task_7_6.primes import get_primes_list


def find_goldbach_prime_numbers(primes_list, number):
    index = 0
    while primes_list[index] <= number // 2:
        diff = number - primes_list[index]
        if diff in primes_list:
            return f"{primes_list[index]} + {diff} = {number}"
        index += 1


def goldbach(number):
    if is_even(number):
        number = int(number)
        primes_list = get_primes_list(number)
        return find_goldbach_prime_numbers(primes_list=primes_list, number=number)
    return "Invalid input, number must be even"


def main():
    while True:
        number = input("Enter your number ('q' for exit): ")
        if number == "q":
            print("Bye!")
            break
        try:
            print(goldbach(number))
        except Exception as error:
            print("An exception occurred:", error.__class__.__name__)
            print("Exception message:", error)


if __name__ == "__main__":
    main()
