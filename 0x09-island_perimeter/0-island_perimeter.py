#!/usr/bin/python3
""" Module for the island_perimeter function """


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid

        grid is a list of list of integers:
            0 represents a water zone
            1 represents a land zone
            One cell is a square with side length 1
            Grid cells are connected horizontally/vertically (not diagonally).
            Grid is rectangular, width and height don’t exceed 100
        Grid is completely surrounded by water, and there is one island
        (or nothing).
        The island doesn’t have “lakes” (water inside that isn’t connected
        to the water around the island).
    """

    perimeter = 0

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                perimeter += 4
                if row > 0 and grid[row-1][column] == 1:
                    perimeter -= 1
                if row < len(grid) - 1 and grid[row+1][column] == 1:
                    perimeter -= 1
                if column > 0 and grid[row][column-1] == 1:
                    perimeter -= 1
                if column < len(grid[row]) - 1 and grid[row][column+1] == 1:
                    perimeter -= 1

    return perimeter
