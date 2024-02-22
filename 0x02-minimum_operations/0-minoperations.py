#!/usr/bin/python3
"""a function to conduct min operations"""


def minOperations(n):
    # Helper function to find prime factorization
    def prime_factors(num):
        factors = []
        divisor = 2
        while divisor * divisor <= num:
            while (num % divisor) == 0:
                factors.append(divisor)
                num //= divisor
            divisor += 1
        if num > 1:
            factors.append(num)
        return factors

    factors = prime_factors(n)
    operations = 0

    # Iterate through prime factors and sum them up
    for factor in set(factors):
        count = factors.count(factor)
        operations += count

    return operations
