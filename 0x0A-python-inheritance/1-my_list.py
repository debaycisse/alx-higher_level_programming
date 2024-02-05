#!/usr/bin/python3
"""This module houses the definition of MyList class.
"""


class MyList(list):
    """The class inherits from the built-in list class.
    It can uses the init method of the list class and
    implements its own print_sort method
    """
    def __init__(self, lists=[]):
        """This initializes the elements by calling
        the parent init method.

        Args:
            lists: an empty list with which the list is initialized
        """
        super().__init__(elm for elm in lists)

    def print_sorted(self):
        """This is method prints a sorted copy of the
        elements of the list
        """
        temp = self[:]
        temp.sort()
        print(temp)
