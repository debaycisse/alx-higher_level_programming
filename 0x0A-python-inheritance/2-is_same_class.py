#!/usr/bin/python3
"""This module houses the definition of the
is_same_class function.
"""


def is_same_class(obj, a_class):
    """This function checks if an object is an
    instance of a class or not

    Args:
        obj: an instance to be checked
        a_class: a class to be checked against

    Returns:
        True if the instance (obj) is truly an
        instance of the a class (a_class), otherwise
        false is returned.
    """
    if isinstance(obj, a_class):
        type_ch = type(obj).__name__
        class_ch = a_class.__name__
        return (type_ch == class_ch)
    return (False)
