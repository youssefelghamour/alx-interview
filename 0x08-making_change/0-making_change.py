#!/usr/bin/python3
""" mdule for the makeChange function """


def makeChange(coins, total):
    """ determine the fewest number of coins needed to
        meet a given amount total
    """

    if total <= 0:
        return 0

    # initialize the DP array with a large number larger
    # than any possible number of coins needed
    max_val = total + 1
    dp = [max_val] * (total + 1)
    dp[0] = 0

    # fill the DP array
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != max_val:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # return -1 if dp[total] is still the initial large value
    if dp[total] != max_val:
        return dp[total]
    else:
        return -1
