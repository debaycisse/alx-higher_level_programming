#!/usr/bin/python3
"""This is a module for matrix_divided.
This module divides each element in of matrix and return a new matrix
"""


def matrix_divided(matrix, div):
    """This function divides all elements of sub-list by div
       parameter and returns them all as a new list.

    Args:
        matrix: this is the list whose sub-list are divided
        div: this is the number with which each element is divided

    Raises:
        TypeError: this is raised when a non-list type is given and
        when the length of all the sub-list is not the same
        ZeroDivisionError: this is raised whenever zero is given
        as div parameter

    Returns:
        the new list that contains result of dividing each element
        of the sub-list and rounding their respective result to
        2 decimal place value.
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    for sub_list in matrix:
        if type(sub_list) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    for sub_list in matrix:
        for l_index in range(len(sub_list)):
            if type(sub_list[l_index]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    l_len = []
    for l_index in range(len(matrix)):
        l_len.append(len(matrix[l_index]))
    if len(l_len) > 1:
        for a_len in range(len(l_len)):
            if a_len == 0 and l_len[a_len] != l_len[a_len + 1]:
                raise TypeError("Each row of the matrix \
must have the same size")
            elif (a_len + 1 < len(l_len)) and \
                 (l_len[a_len] != l_len[a_len + 1]):
                raise TypeError("Each row of the matrix \
must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    for sub_l in matrix:
        temp = []
        for element in range(len(sub_l)):
            temp.append(round(sub_l[element] / div, 2))
        new_list.append(temp)
    return new_list
