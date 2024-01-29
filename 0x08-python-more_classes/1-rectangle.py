#!/usr/bin/python3
"""This module houses a definition of a rectangle object,

and those of its members, properties, and attributes
"""


class Rectangle:
    """The Rectangle class where its attributes and properties are defined.
    """

    def __init__(self, width=0, height=0):
        """this sets an initial value for the width.
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """This  method that returns the value of width

        Returns:
            the value of width is returned
        """
        return self.__width

    @width.setter
    def width(self, value):
        """This method updates the value of the width.

        Raises:
            TypeError: if value is any type other than integer.
            ValueError: if value is less than zero.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This  method that returns the value of width

        Returns:
            the value of width is returned
        """
        return self.__height

    @height.setter
    def height(self, value):
        """This method updates the value of the height.

        Raises:
            TypeError: if value is any type other than integer.
            ValueError: if value is less than zero.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
