#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix
    new_matrix = list(map(lambda x: x**2, new_matrix))
    return new_matrix
