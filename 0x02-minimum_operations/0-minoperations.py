#!/usr/bin/python3

"""
This script defines a function that calculates the minimum number of operations needed to reach
a specified number of 'H' characters in a text editor. The operations are defined as either:
1. Copy all the 'H' characters currently in the file.
2. Paste the last copied 'H' characters into the file.

The goal is to determine the fewest number of these operations required to achieve exactly 'n' 'H' characters.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to get 'n' 'H' characters.

    Parameters:
    n (int): Target number of 'H' characters.

    Returns:
    int: Minimum number of operations required.

    """

    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
