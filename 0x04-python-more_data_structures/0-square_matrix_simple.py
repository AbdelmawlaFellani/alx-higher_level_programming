#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda x: [el**2 for el in x], matrix))
