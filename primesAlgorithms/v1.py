"""
less efficient algorith to calculate all primes number lower than n;
"""

from datetime import datetime

from primesAlgorithms import validate_input


@validate_input
def get_primes_lower_n(n: int) -> list[int]:
    print(n, datetime.now(), 'v1')
    return [el for el in range(2, n + 1) if is_prime(el)]


def is_prime(el: int) -> bool:
    for num in range(2, el):
        if not el % num:
            return False
    return True
