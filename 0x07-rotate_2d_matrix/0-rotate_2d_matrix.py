#!/usr/bin/python3
""" Module to rotate a 2D matrix """


def rotate_2d_matrix(matrix):
    """  Rotates a 2D matrix
    """
    left = 0
    right = len(matrix) - 1

    while left < right:
        for i in range(right - left):
            # because it's a square matrix:
            top = left
            bottom = right

            # save the top left element in a temp variable
            topLeft = matrix[top][left + i]

            # move the bottom left into the top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # move the bottom right into the bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move the top right into the bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # move the top left into the top right
            matrix[top + i][right] = topLeft

        right -= 1
        left += 1
