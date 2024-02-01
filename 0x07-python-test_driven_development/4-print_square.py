#!/usr/bin/python3
"""The print_square module.

This module contains the defintition of the print_square function.
"""


def print_square(size):
    """This function uses '#' character to denote how a shape of
    square of a given size will look like.

    Args:
        size: the size of the square to be printed

    Raises:
        TypeError: if the size is not integer or it is float
        and less than zero
        ValueError: if the given size is not of type integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0.0:
        raise TypeError("size must be an integer")
    i = 0
    while i < size:
        j = 0
        while j < size:
            print("#", end="")
            j += 1
        if i + 1 != size:
            print()
        i += 1
