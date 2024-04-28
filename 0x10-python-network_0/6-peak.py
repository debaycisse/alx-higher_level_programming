"""This module houses the definition of the fin_peak function"""


def find_peak(list_of_integers):
    """The find_peak function obtains the peak,
    among the elements of the passed integer list"""
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) > 2:
        split_half = len(list_of_integers) // 2
        a = find_peak(list_of_integers[:split_half + 1])
        b = find_peak(list_of_integers[split_half + 1:])
    else:
        if len(list_of_integers) == 2:
            if list_of_integers[0] > list_of_integers[1]:
                return list_of_integers[0]
            return list_of_integers[1]
        return list_of_integers[0]
    if a > b:
        return a
    return b
