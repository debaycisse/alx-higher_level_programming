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

    def integer_validator(self, name, value):
        """This methods validates a passed value and responds accordingly

        Args:
            name: the name of a given value at a point in time.
            value: the value of the passed name.
        """
        if type(value).__name__ != 'int':
            raise TypeError("{} must be an integer".format(name))
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        elif name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method converts a data from a python
        dictionary to a JSON format.

        Args:
            list_dictionaries: the data to be converted to JSON format

        Returns:
            The JSON equivalent of the given list of a python dictionary.
            Empty list is returned if the given list of dictionary is empty.
        """
        if len(list_dictionaries) <= 0:
            return "[]"
        elif len(list_dictionaries) > 0:
            import json
            return json.dumps(list_dictionaries)
