#!/usr/bin/python3
"""This module houses the definition of add_integer.

A function that adds two integer values together and
returns the result of this operation.
"""

def add_integer(a, b=98):
    """This function computes the addition operation on both a and b
    a and b are added and their result is returned
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
