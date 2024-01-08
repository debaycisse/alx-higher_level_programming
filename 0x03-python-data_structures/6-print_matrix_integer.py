#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix or not matrix[0]:
        print()
    else:
        for row in matrix:
            for element in range(len(row)):
                print("{:d}"
                      .format(row[element]),
                      end="\n" if element == len(row) - 1 else " ")
