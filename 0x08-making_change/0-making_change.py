#!/usr/bin/python3
'''Given a pile of coins of different values,
    determine the fewest number of coins needed to meet
    a given amount total.
'''


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0

    coins_count = 0
    sorted_coins = sorted(coins, reverse=True)

    for coin in sorted_coins:
        while total >= coin:
            total -= coin
            coins_count += 1

    if total > 0:
        return -1

    return coins_count
