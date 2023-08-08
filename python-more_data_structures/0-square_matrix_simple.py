#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        compt = []
        for i in row:
            compt.append(i ** 2)
        new.append(compt)
    return new
