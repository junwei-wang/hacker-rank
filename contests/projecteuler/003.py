#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import ceil, sqrt

def solve(num):
    while num & 1 == 0:
        num >>= 1
    if num == 1:
        return 2

    max_prime = 3
    sqr = int(ceil(sqrt(num)))
    i = 3
    while i <= num and i <= sqr:
        while num % i == 0:
            max_prime = i
            num /= i
        i += 2
    if num > sqr:
        max_prime = num
    return max_prime

if __name__ == '__main__':
    n = input()
    while n > 0:
        print solve(input())
        n -= 1
