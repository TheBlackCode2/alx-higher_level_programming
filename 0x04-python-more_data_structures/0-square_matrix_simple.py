#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    line = []
    for row in matrix:
        for elm in row:
            line.append(elm * elm)
        new_matrix.append(line.copy())
        line.clear()
    return new_matrix
