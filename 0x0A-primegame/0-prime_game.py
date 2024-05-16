#!/usr/bin/python3
"""
Prime Game
"""


def primeNumbers(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): The upper boundary of the range (inclusive).
        The lower boundary is always 1.
       Returns:
        List[int]: A list of prime numbers between 1 and n inclusive.  
    """
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNos


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): The number of rounds in the game.
        nums (List[int]): A list of integers representing the upper limit
        of the range for each round.
    Return:
        str: The name of the winner ("Maria" or "Ben"),
        or None if there is no clear winner.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNos = primeNumbers(nums[i])
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
