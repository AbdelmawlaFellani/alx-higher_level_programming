#!/usr/bin/python3

def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    matrixSize = len(matrix[0])
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != matrixSize:
            raise TypeError("Each row of the matrix must have the same size")
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
        
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    
    return [[round(value / div, 2) for value in row] for row in matrix]
