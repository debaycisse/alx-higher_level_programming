#!/usr/bin/python3
"""This module houses the definition of a Square class."""


from models import rectangle as r


class Square(r.Rectangle):
    """This is a class for the definiton of a Square class.

    This class inherits both the properties and methods of
    the Rectangle class, where it inherits from.

    Args:
        r.Rectangle: the inherited class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """This method initializes an instance of this class.

        Args:
            size: this is the size's value of an instance.
            x: this is the x axis' dimension value of an instance.
            y: this is the y axis' dimension value of an instance.
            id: this is the id's value of an instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This method handles a call from either of the str and print.

        Returns:
            The instance representation of this class as implemented below.
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    @property
    def size(self):
        """This method obtains and returns the value of the size for an
        instance of this class
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """This method updates the value of the size with a given value.

        Args:
            value: the value with which the value of size is updated.
        """
        super().integer_validator("width", value)
        self.width = value

    def update(self, *args, **kwargs):
        """This method updates the values of all the necessary 4
        attributes of this class for a given instance.

        Args:
            args: a list of arguments in an expected order.
            kwargs: a list of keyworded arguments in any order.
        """
        if len(args) > 0:
            for num in range(len(args)):
                if num == 0:
                    self.id = args[num]
                elif num == 1:
                    super().integer_validator("width", args[num])
                    self.width = args[num]
                elif num == 2:
                    super().integer_validator("x", args[num])
                    self.x = args[num]
                elif num == 3:
                    super().integer_validator("y", args[num])
                    self.y = args[num]
        elif len(kwargs) > 0 and len(args) == 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    super().integer_validator("width", v)
                    self.width = v
                elif k == "x":
                    super().integer_validator("x", v)
                    self.x = v
                elif k == "y":
                    super().integer_validator("y", v)
                    self.y = v
