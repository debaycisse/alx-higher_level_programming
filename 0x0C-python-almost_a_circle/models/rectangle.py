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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("x", x)
        self.__x = x
        super().integer_validator("y", y)
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """This method gets and returns a value of the width's attribute.

        Returns:
            The value of the width attribute of an instance.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """This method updates the value of the width attribute.

        Args:
            value: the value to be used in updating the width attribute.
        """
        super().integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """This method returns the value of the height attribute.

        Returns:
            The value of the height attribute of an instance.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """This method updates the height value of an instance of this class.

        Args:
            value: the value with which the value of the height is updated.
        """
        super().integer_validator("height", value)

    @property
    def x(self):
        """This method gets and returns the value of the x attribute.

        Returns:
            The value of the x attribute of an instance of this class.
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """This method updates the value of the x attribute of an instance.

        Args:
            value: the value with which the value of the
            x attribute is updated.
        """
        super().integer_validator("x", value)

    @property
    def y(self):
        """This method obtains the value of the y attribute.

        Returns:
            The value of the y attribute of a given instance.
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """This method updates the value of the y attribute.

        Args:
            value: the value with which the value of y is updated.
        """
        super().integer_validator("y", value)

    def area(self):
        """This method computes the area of an instance of this class.

        Returns:
            The value of the area computation for an instance.
        """
        return (self.__width * self.__height)
