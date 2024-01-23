#!/usr/bin/python3
"""This module defines Square shape and its fields.

It is going to define all attributes of Square shape with
all possible operations that can be performed on it
"""


class Square:
    """Represents a real world square shape object.

    It is going to define and implement the fields of square shape.
    The size of an instance object is implemenented for now
    """

    def __init__(self, size):
        """This initializes the size of the square.

        The size determines the calculation of the area of a square

        Args:
           size (int): this is the size of any square instances
        """
        self.__size = size
