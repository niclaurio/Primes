"""
refactor:


1. more efficient memory usage:  list of boolean instead of list of integers for primes numbers;

2. More efficient even numbers handling: even numbers greater than 2 are directly marked as non-prime at the beginning

3. Optimized Inner Loop:
   - The inner loop iterates only up to the square root of `n`,skipping over useless checks
   - Multiples of each prime number are marked starting from `el**2`, skipping over numbers that have already been marked as multiples by smaller primes.

4. more efficient primes list generation: instead of adding to primes list each element one by one, I use a list comprehension for True values
"""

from datetime import datetime
from math import isqrt
from primesAlgorithms import validate_input


@validate_input
def get_primes_lower_n(n: int) -> list[int]:
    '''
    it creates a list of boolean and it sets to False all indexes corresponding to multiple numbers;
    returns: a list of integers corresponding to the indexes of each True value
    '''

    primes = [False, False] + [True] * (n - 1)
    primes[4 : n + 1 : 2] = [False] * len(primes[4: n+1: 2])  # set to False multiples of 2

    for el in range(3, isqrt(n) + 1, 2):
       if primes[el]:
           primes[el**2 : n + 1 : el * 2] = [False] * len(primes[el**2 : n + 1 : el * 2]) # set to False multiples of each prime number

    return [i for i, is_prime in enumerate(primes) if is_prime]
