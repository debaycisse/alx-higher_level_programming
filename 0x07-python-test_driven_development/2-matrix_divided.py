#!/usr/bin/python3
"""This is a module for matrix_divided.
This module divides each element in of matrix and return a new matrix
"""


def matrix_divided(matrix, div):
    if type(matrix) is not list: 
        raise TypeError("matrix must be a matrix (list of lists)
                        of integers/floats")
    for sub_list in matrix:
        if type(sub_list) is not list:
            raise TypeError("matrix must be a matrix (list of lists)
                            of integers/floats")
    for sub_list in matrix:
        for l_index in range(len(sub_list)):
            if type(sub_list[l_index]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)
                                of integers/floats")
    l_len = []
    for l_index in range(len(matrix)):
        l_len.append(len(matrix[l_index]))
    if len(l_len) > 1:
        for a_len in range(len(l_len)):
            if type(l_len[a_len + 1]) in [int, float] and
               l_len[a_len] != l_len[a_len + 1]:
                raise TypeError("Each row of the matrix
                                must have the same size")
            elif type(l_len[a_len - 1]) in [int, float] and
                 l_len[a_len] != l_len[a_len - 1]:
                raise TypeError("Each row of the matrix
                                must have the same size")
    if type(div) not in [int, float]: 
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
