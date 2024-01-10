#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = []
    for row in matrix:
        temp = []
        for i in range(len(row)):
            temp.append(row[i] ** 2)
        sq.append(temp)
    return sq
