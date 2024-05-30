#!/usr/bin/python3
""" module for pascal_triangle function """


def pascal_triangle(n):
    """ function that returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    triangle = []
    # add the first row
    triangle.append([1])

    if (n > 0):
        for i in range(1, n):
            row = []

            # add the first "1"
            row.append(1)

            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])

            # add the last "1"
            row.append(1)

            triangle.append(row)

    return triangle
