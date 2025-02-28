"""
refactor: if one number has no divisors lower than its square root, that number is prime.
"""

from datetime import datetime
from math import isqrt

from primesAlgorithms import validate_input


@validate_input
def get_primes_lower_n(n: int) -> list[int]:
    print(n, datetime.now(), 'v3')
    return [2] + [el for el in range(3, n + 1, 2) if is_prime(el)]


def is_prime(el: int) -> bool:
    for num in range(3, isqrt(el) + 1, 2):
        if not el % num:
            return False
    return True
