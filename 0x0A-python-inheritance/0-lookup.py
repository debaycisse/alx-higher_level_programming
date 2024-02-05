#!/usr/bin/python3
"""This module houses the definition of lookup() function.

The lookup() function returns a list of attributes and
methods of an object.
"""


def lookup(obj):
    """The lookup() function gets and returns a list of attributes
    and methods that are available for a given obj object.

    Args:
        obj: this is the object whose attributes and methods are obtained

    Returns:
        A list of attributes and methods of the given object are returned
    """
    return (dir(obj))
