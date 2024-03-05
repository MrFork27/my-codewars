import math
from collections import Counter


def prime_factors(n):
    current_number = n
    primes = []
    primes_count = {}

    while current_number > 1:
        prime = get_first_prime(int(current_number))
        current_number = current_number / prime
        primes.append(prime)

    return "".join(
        f"({key}**{value})" if value != 1 else f"({key})"
        for key, value in Counter(primes).items()
    )


def get_first_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0 and is_prime(i):
            return i

    return number


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True
