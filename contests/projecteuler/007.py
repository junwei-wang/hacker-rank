#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt, ceil

# any primer bigger than 3 can be written in 6k+1 or 6k-1
def generate_n_primes(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    cnt = len(primes)

    def is_prime(n):
        sqr = ceil(sqrt(n))
        for p in primes:
            # a number can only have one factor bigger than its squre
            # hence, a prime number has no factor lower than its squre
            if p > sqr:
                return True
            if n % p == 0:
                return False
        return True

    num = 18
    while True:
        num += 6
        if cnt >= n:
            return primes
        if is_prime(num-1):
            cnt += 1
            primes.append(num-1)
        if is_prime(num+1):
            cnt += 1
            primes.append(num+1)

def solve(num, primes):
    return primes[num-1]

if __name__ == '__main__':
    numbers = list()
    n = input()
    while n > 0:
        numbers.append(input())
        n -= 1
    max_num = max(numbers)
    primes = generate_n_primes(max_num)
    for num in numbers:
        print solve(num, primes)
