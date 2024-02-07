#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """a function that returns a list of lists
    of integers representing the Pascal’s triangle
    """
    if n <= 0:
        return []
    pt = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            element = pt[i - 1][j - 1] + pt[i - 1][j]
            row.append(element)
        row.append(1)
        pt.append(row)
    return pt
