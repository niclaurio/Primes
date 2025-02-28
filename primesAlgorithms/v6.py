"""
refactor: Optimized Sieve of Eratosthenes with NumPy for Performance Gains

"""

from datetime import datetime

import numpy as np
from math import isqrt

from primesAlgorithms import validate_input


@validate_input
def get_primes_lower_n(n: int) -> np.ndarray:
    print(n, datetime.now(), 'v6')

    primes = np.ones(n + 1, dtype=bool)

    primes[:2] = False
    primes[4 : n + 1 : 2] = False # mark even numbers as not prime

    for i in range(3, isqrt(n) + 1, 2):
        if primes[i]:
            primes[i**2 : n + 1 : i * 2] = False # mark multiples of i as not prime

    return np.where(primes)[0]
