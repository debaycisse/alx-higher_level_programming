#!/usr/bin/python3
"""This modules houses the definition of BaseGeometry class
"""


class BaseGeometry:
    """This class defines the properties and methods of a Geometry
    """

    def area(self):
        """area() method is to calculate the area of an instance of
        a Geometry, but raises exception since it is not implemented yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function validates the value that is passed to value
        parameter to ensure that it is a correct vvalue
        
        Args:
            name: this is the name parameter
            value: this is the value parameter to be validated
        """
        if type(value).__name__ != 'int':
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
