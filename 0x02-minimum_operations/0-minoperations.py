#!/usr/bin/python3
""" module for minOperations function """


def checkPrime(n):
    """ Function that checks if a number is prime """
    if n > 1:
        # check if the number is divisible by any between 1 and n
        # since a prime number is only divisible by 1 and itself
        for i in range(2, (n//2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


def primeFactors(n):
    """ Function that finds the prime factors of a number
        and returns their sum """
    prime_numbers = []

    if n > 0:
        # start from the smallest prime number
        i = 2
        """
        while i <= n:
            if (n % i) == 0:
                prime_numbers.append(i)
                n //= i
            else:
                i += 1
        """
        # for efficieny, we only need to check up to √n
        while i * i <= n:
            # if i is a factor of n
            if (n % i) == 0:
                prime_numbers.append(i)
                n //= i
            else:
                # if i is not a factor, increment i and check the next number
                i += 1
        # if n is greater than 1 after the loop, it must be a prime factor
        if n > 1:
            prime_numbers.append(n)

    return sum(prime_numbers)


def minOperations(n):
    """ Function that calculates the fewest number of operations
        needed to result in exactly n H characters in a file

        It counts how many copy or paste operations """
    number_operations = 0

    if n > 1:
        # if prime
        if checkPrime(n):
            # since prime numbers have only one prime factor, the number itself
            number_operations = n
        # if not prime
        else:
            number_operations = primeFactors(n)

    return number_operations
