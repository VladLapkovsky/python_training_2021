"""Write a function that check whether a string is a palindrome or not.

Usage of any reversing functions is prohibited. To check your implementation you can use
strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
"""


def is_palindrome(input_str: str) -> bool:
    input_str = input_str.lower()
    for index, _char in enumerate(input_str):
        if input_str[index] != input_str[-index - 1]:
            return False
    return True
    # return input_str.lower() == input_str.lower()[::-1]


if __name__ == '__main__':
    s_1 = 'Repaper'
    s_2 = 'Repazer'
    s_3 = 'qwq'
    print("s_1 is palindrome:", is_palindrome(s_1))
    print("s_2 is palindrome:", is_palindrome(s_2))
    print("s_3 is palindrome:", is_palindrome(s_3))
