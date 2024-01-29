#!/usr/bin/python3
"""This module houses a definition of a rectangle object,

and those of its members, properties, and attributes
"""


class Rectangle:
    """The Rectangle class where its attributes and properties are defined.
    """

    # This attribute keeps track of the number of object(s) of the class
    number_of_instances = 0

    # This attribute stores the character to be used for the shape
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """this sets an initial value for the width, height,
        and the number_of_instances.
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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
                    print(self.print_symbol, end="")
                    j += 1
                if i + 1 < self.__height:
                    print()
                i += 1
        return ""

    def __repr__(self):
        """This method get called when a repr() function takes an

        instance of this class as a parameter.

        Returns:
            the string formatted version or official representation
            of the class which this instance belongs.
        """
        return (
                "Rectangle({self.width}, {self.height})"
                .format(self=self)
               )

    def __del__(self):
        """This method handle the destructor aspect of an

        instance of this class.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This method compares two instances of this class and
        returns the bigger of the two instances

        Returns:
            The bigger of the two given instances is returned

        Raises:
            TypeError: This will be raised if any of the given
            instances is not an instance of the Rectangle class
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """This method creates an instance of a Rectangle
        class for a square shape.

        Args:
            cls: This references the class (Rectangle).
            size: This is the same for all the square sides.

        Returns:
            The new instance of the Rectangle class is returned

        Raises:
            TypeError: If the size is not an integer
            ValueError: If the size is less than zero or 0
        """
        if type(size) not in [int, float]:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        return (cls(size, size))
