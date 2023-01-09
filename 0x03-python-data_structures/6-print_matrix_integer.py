#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print()
    for element in range(len(matrix)):
        for item in range(len(matrix[element])):
            if item != len(matrix[element]) - 1:
                endspace = " "
            else:
                endspace = ""
            print("{}".format(matrix[element][item]), end=endspace)
        print()
