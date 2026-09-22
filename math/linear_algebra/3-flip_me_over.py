#!/usr/bin/env python3
'''
    The Script has a function that returns the transpose of a 2D matrix.
'''


def matrix_transpose(matrix):
    '''
        Returns The transpose of a 2d matrix.
        matrix: The 2d matrix to be transposed.
        Returns: list of list of transposed matrix.
    '''
    # Using list comprehension to transpose
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
