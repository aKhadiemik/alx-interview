#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    Generates a pascal triangle for specified size

    Args:
        n: integer specifying triangle size

    Returns:
        List: List of lists
    """

    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    pascal_triangle = [[1]]
    for i in range(n-1):
        row = [1, ]
        for j in range(len(pascal_triangle[i])-1):
            row.append(pascal_triangle[i][j]+pascal_triangle[i][j+1])
        row.append(1)
        pascal_triangle.append(row)

    return pascal_triangle
