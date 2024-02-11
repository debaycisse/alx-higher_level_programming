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
