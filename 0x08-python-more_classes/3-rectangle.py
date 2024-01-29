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

    def area(self):
        """This methods computes the area of a given instance of

        a rectangle and returns the value.

        Returns:
            the computed value, obtained for the area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """This methods computes the perimeter of a given instance of

        a rectangle and returns the value.

        Returns:
            the computed value, obtained for the perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """This method gets called when the print() function or

        the str() function is called on any instance of this class

        Returns:
            the rectangle shape via # character; using the width for
            the number of the # to appear on a row and repeating the
            row in a number of time of the value of the height
        """
        if self.__width != 0 and self.__height != 0:
            i = 0
            while i < self.__height:
                j = 0
                while j < self.__width:
                    print("#", end="")
                    j += 1
                if i + 1 < self.__height:
                    print()
                i += 1
        return ""
