#!/usr/bin/python3
"""
function to determine the fewest number of coins needed
to meet a given amount total
"""


def makeChange(coins, total):
    """
    this function will take a list of coins and use
    that to calculate how much change the total will require
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        coin_count = 0
        for i in coin:
            while(total >= i):
                coin_count += 1
                total -= i
        if total == 0:
            return coin_count
        return -1
