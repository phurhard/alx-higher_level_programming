#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        for item in element:
            print("{}".format(item), end=" ")
        print("")
