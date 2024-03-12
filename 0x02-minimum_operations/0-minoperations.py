#!/usr/bin/python3
"""a function to conduct min operations"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = n

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            operations = min(operations, i + minOperations(n // i))

    return operations
