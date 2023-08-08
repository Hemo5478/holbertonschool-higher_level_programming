#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = 0
    while row < len(matrix):
        i = 0
        while i < len(matrix[row]):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(matrix[row][i]), end="")
            i += 1
        print()
        row += 1
