#!/usr/bin/python3
""" prime game module """


def count_primes(n):
    """ count primes up to n """
    if n < 2:
        return 0
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return sum(is_prime)


def isWinner(x, nums):
    """ returns the winner """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
