#!/usr/bin/python3
"""This module conatains the definiton
of is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """This function determines if an object is
    an instance of a class or not.

    Args:
        obj: the object to be checked against a class
        a_class: the class to be checked against an object

    Returns:
        True, if object is an instance of a class, otherwise false
    """
    return (isinstance(obj, a_class))
