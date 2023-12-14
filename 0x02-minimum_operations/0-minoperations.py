#!/usr/bin/python3
"""
module function minOperations(n) returns
the fewest number of operations needed to result in
exactly n H characters in the file.
"""


def minOperations(n):
    """
    Least Common Divisors are found and added up except 1
    n = 0, impossible as delete is unavailable
    n = 1, can return without operations
    other operations are set as sum of Least common divisions
    with repeation.
    """
    ops = 0
    if n == 0 or (n//1 != n):
        return 0
    if n == 1:
        return 0
    i = 2
    while n > 1 and i <= n:
        if n % i == 0:
            n = n//i
            ops += i
        else:
            i = i + 1
    return ops
