#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import ceil, sqrt

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def solve(num):
    ret = 1
    for p in primes:
        if p > num:
            break
        t = p
        while t <= num:
            t *= p
        t /= p
        ret *= t
    return ret

if __name__ == '__main__':
    n = input()
    while n > 0:
        print solve(input())
        n -= 1
