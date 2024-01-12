#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda r: list(map(lambda i: r[i]**2, range(len(r)))), matrix))
