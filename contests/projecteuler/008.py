#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(n, k, digits):
    def max_mult(s):
        cast = lambda c: int(c)
        mult = lambda a, b: a * b
        max = 1
        for i in range(0, len(s) - k + 1):
            mult_val = reduce(mult, map(cast, s[i:i+k]))
            if mult_val > max:
                max = mult_val
        return max

    digits = digits.split('0')
    digits = filter(lambda s: len(s) >= k, digits)
    digits = map(max_mult, digits)
    return max(digits) if digits else 0

if __name__ == '__main__':
    t = input()
    while t > 0:
        tmp = raw_input()
        n, k = tmp.split()
        print solve(int(n), int(k), raw_input())
        t -= 1
