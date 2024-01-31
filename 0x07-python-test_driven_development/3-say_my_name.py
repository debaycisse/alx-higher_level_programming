#!/usr/bin/python3
"""This module houses the definition of the say_my_name function.

The function takes two arguments; the former is the first name
while the latter is the last name.

The both argument must of course be of string type.
"""


def say_my_name(first_name, last_name=""):
    """This function takes two strings and prints them out.

    It prints out both the first and last name, which are
    the two strings that it takes.

    Args:
        first_name: this is the first name
        last_name: this is the last name

    Raises:
        TypeError: raises whenever the type of the
        given arguments is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
