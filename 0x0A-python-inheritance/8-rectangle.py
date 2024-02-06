#!/usr/bin/python3
"""This module houses the definition of both Ractangle
class with its attributes and methods
"""


gm = __import__("7-base_geometry")


class Rectangle(gm.BaseGeometry):
    """This is a Rectangle class.
    It implements the logic of a Rectangle object with the
    properties and methods
    """
    def __init__(self, width, height):
        """This instantiation method validates the
        values of the both width and height

        Args:
            width: this is the value for the width
            height: this is the value for the height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
