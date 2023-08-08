#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_values = []
    i = 0
    while i < len(matrix):
        matrix_row = matrix[i]
        list_values = []
        for columns in range(len(matrix_row)):
            list_values.append(matrix_row[columns] ** 2)
            matrix_values.append(list_values)
            i += 1
            return matrix_values
