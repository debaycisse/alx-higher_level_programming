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

    def __init__(self, size=0):
        """This initializes the size of the square.

        The size determines the calculation of the area of a square

        Args:
           size (int): this is the size of any square instances

        Raises:
            TypeError: this is raised, if size is not an integer type
            ValueError: this is raised, if size is less than zero
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This area method does exactly what its name implies.

        It calculates the area of a given square object or instance
        and returns the value

        Returns:
            The area of a given square object is returned
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """size method is used to retrieve the value of the size.

        The value of the given size of an underlying object is fetched.

        Returns:
            The value of the size of a given square's instance is returned
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """This is a setter version of the size method.

        This updates the value for the size field.

        Args:
            value (int): this value is used to update the value of size.

        Raises:
            TypeError: this is raised only when a non-integer is given as the
            value for the size.
            ValueError: this is raised when a given value is negative.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """This method prints # character repeatedly in size times.

        This displays # character to represent the size of square.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
