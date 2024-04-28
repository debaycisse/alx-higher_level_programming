"""This module houses the definition of the fin_peak function"""


def find_peak(list_of_integers):
    """The find_peak function obtains the peak,
    among the elements of the passed integer list"""
    if len(list_of_integers) < 1:
        return None
    l_copy = list_of_integers.copy()
    l_copy.sort()
    return l_copy[-1]
