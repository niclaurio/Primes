"""
refactor: Sieve of Eratosthenes
"""

from datetime import datetime

from primesAlgorithms import validate_input


@validate_input
def get_primes_lower_n(n: int) -> list[int]:
    """
    this function iterates over all odd numbers and:
        - if the number is a multiple of a lower number, it will be skipped
        -the number is prime: all its multiples greater than its square will be added to multiples set
    """
    primes = [2]
    multiples = set()
    for el in range(3, n + 1, 2):
        if el not in multiples:
            multiples.update(
                set(range(el**2, n + 1, el * 2))
            )  # multiples lower than el**2 are already multiples of lower numbers
            primes.append(el)
    return primes
