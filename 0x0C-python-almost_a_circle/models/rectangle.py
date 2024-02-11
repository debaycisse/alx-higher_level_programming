#!/usr/bin/python3
"""This module houses the definition of a
Rectangle class and its properties"""


from models import base as b


class Rectangle(b.Base):
    """This class defines the logics of a Rectangle class

    Args:
        Base: Base is a parent class from which this
        class inherits its properties
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """This class initializes an instance of this class
        with a set of required attributes

        Args:
            id: the attribute of the parent class
            width: the width of an instance
            height: the height of an instance
            x: the x-axis dimension of an instance
            y: the y-axis dimension of an instance
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
