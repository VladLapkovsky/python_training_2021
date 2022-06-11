"""Modify ONE LINE in "inner_function" to make it print variable "a" from global scope."""

a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        print(a)

    return inner_function()

enclosing_funcion()
