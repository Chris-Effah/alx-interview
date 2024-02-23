#!/usr/bin/python3
"""a function to conduct min operations"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    achieve n 'H' characters.

    Parameters:
        n (int): The desired number of 'H' characters in the file.

    Returns:
        int: The fewest number of operations needed.

    Raises:
        None
    """
    if n <= 1:
        return 0

    operations = n

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            operations = min(operations, i + minOperations(n // i))

    return operations
