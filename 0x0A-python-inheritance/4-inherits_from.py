#!/usr/bin/python3
"""This module houses the definition of inherits_from function
"""


def inherits_from(obj, a_class):
    """This function checks if a given object is an instance
    of an inherited (either directly or indirectly)

    Args:
        obj: the object whose class' parent or grand-parent
        or great-grand-parent  is checked
        a_class: the class, which is compared against any
        parent of the given object or instance

    Returns:
        True, if the parent (grand-parent e.t.c) of given
        object matches with the given class, otherwise
        False is returned.
    """
    if isinstance(obj, a_class):
        obj_derived = type(obj).__name__
        a_class_name = a_class.__name__
        return (not (obj_derived == a_class_name))
    return (False)
