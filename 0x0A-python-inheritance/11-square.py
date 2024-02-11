#!/usr/bin/python3
"""This module houses the definition of Square
class with its attributes and methods
"""


rc = __import__("9-rectangle")


class Square(rc.Rectangle):
    """This is an implementation of a Square class.
    """

    def __init__(self, size):
        """This method instantiate a new object of this class

        Args:
            size: this is the size of a Square's object
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """This method computes and returns
        the area of a Square object
        """
        return (self.__size ** 2)

    def __str__(self):
        """This methods responds to a call from both print
        and str functions to an object of this class.
        """
        return (
            "[Square] {}/{}".format(self.__size, self.__size)
        )
