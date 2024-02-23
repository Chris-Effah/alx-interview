#!/usr/bin/python3
"""a function to conduct min operations"""


def minOperations(n):
    if n <= 1:
        return 0  # If n is less than or equal to 1, no operations needed

    operations = 0
    current_length = 1  # Start with a single 'H'

    while current_length < n:
        if n % current_length == 0:
            operations += 2  # Copy All and Paste
            current_length *= 2
        else:
            operations += current_length // 2  # Copy All and Paste multiple times
            current_length *= 2

    return operations
   
    