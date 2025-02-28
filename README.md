# Primes Algorithm's comparison 


Is it truly so crucial to write highly efficient code and implement optimized algorithms? To what extent can these two factors influence the execution and overall performance of a program?

The aim of this project is to provide an answer to these questions by developing various versions of an algorithm that calculates prime numbers smaller than a given value, in order to analyze their efficiency and impact on performance.

To achieve this goal, the algorithms will be executed in pairs, starting with the least efficient and progressing to the most optimized, with execution times being recorded for progressively larger numerical values. The collected execution times will then be represented graphically, allowing for a visual analysis of the trends, highlighting any increases or decreases in times as the input number parameter to the algorithm changes.

To further optimize the process, the execution time calculation will be performed using parallel programming.

## Algorithms
1) v1: Returns all numbers between 1 and nn that have no divisors other than themselves and 1. To achieve this, the algorithm examines each number in the range from 1 to nn and checks whether it is divisible by any other number besides 1 and itself.

2) v2: Since all even numbers, except for 2, are multiples of 2 and therefore not prime, the algorithm is improved by only checking odd numbers between 3 and nn. For each of these numbers, the algorithm checks for the presence of odd divisors.

3) v3: Every non-prime number can be expressed as the product of two numbers, at least one of which is smaller than or equal to its square root. Using this property, the algorithm checks for divisors of each number between 1 and its square root, thus reducing the number of checks required.

4) v4: The Sieve of Eratosthenes is an algorithm that, for each number between 1 and nn, eliminates all of its multiples less than nn. The numbers that remain after this operation are not divisible by any other numbers and, therefore, are prime.

5) v5: The algorithm follows the same logic as the Sieve of Eratosthenes, but uses a list of boolean values to represent the numbers, setting all multiples of each prime number to False. At the end, the numbers that remain marked as True are the prime numbers.

6) v6: Similarly to the previous one, a numpy array is used instead of a list. This improves the operational efficiency of the algorithm, thanks to the faster access and manipulation of data offered by numpy arrays.
