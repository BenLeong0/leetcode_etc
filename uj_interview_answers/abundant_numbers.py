"""
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""
from math import floor, sqrt
from typing import List, Set


def get_proper_divisors(n: int) -> Set[int]:
    assert n > 0
    if n == 1:
        return []
    proper_divisors = { 1 }
    for i in range(2, floor(sqrt(n))+1):    # Can't use ceil(sqrt(n))! Would ignore sqrts
        if n % i == 0:
            proper_divisors.add(i)
            proper_divisors.add(n // i)
    return proper_divisors

assert get_proper_divisors(12) == {1, 2, 3, 4, 6}


def is_abundant(n: int) -> bool:
    return sum(get_proper_divisors(n)) > n

assert is_abundant(12) is True


def get_abundant_numbers() -> List[int]:
    # Generate list of all abundant numbers (can reduce limit further?)
    return [n for n in range(1, 28123) if is_abundant(n)]


def get_abundant_sums() -> Set[int]:
    # Iterate over list of abundant numbers twice, keep set of all sums
    abundant_numbers = get_abundant_numbers()
    abundant_sums = set()
    for i in range(len(abundant_numbers)//2 + 1):
        for j in range(i, len(abundant_numbers) - i):
            abundant_sums.add(abundant_numbers[i] + abundant_numbers[j])
    return abundant_sums


def get_non_abundant_sums() -> Set[int]:
    # Get complement of abundant sums set
    abundant_sums = get_abundant_sums()
    non_abundant_sums = {n for n in range(1, 28124) if n not in abundant_sums}
    print('Largest non-abundant sum:', max(non_abundant_sums))
    return non_abundant_sums


def get_sum_of_non_abundant_sums():
    return sum(get_non_abundant_sums())


print('Sum of all non-abundant sums:', get_sum_of_non_abundant_sums())  # 4179871
