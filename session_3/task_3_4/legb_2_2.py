"""Modify ONE LINE in "inner_function" to make it print variable "a" form enclosing function."""

a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        nonlocal a
        print(a)

    return inner_function()

enclosing_funcion()
