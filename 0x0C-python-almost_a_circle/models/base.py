#!/usr/bin/python3
"""This modules houses the definiton of the class Base,
along with its properties or attributes and methods"""


class Base:
    """This is a class for the Base where its
    properties and methods are defined
    """

    # The number of objects of this class
    __nb_objects = 0

    def __init__(self, id=None):
        """This function initializes an instance of this
        class with a keyword parameter, named id

        Args:
            id: this is an optional parameter, which is
            used to either track a number of instances of this class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
