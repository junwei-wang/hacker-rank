#!/usr/bin/env python
# -*- coding: utf-8 -*-
def even_fib(max):
    a = 1
    b = 1
    while a < max:
        if a & 1 == 0:
            yield a
        tmp = a + b
        a = b
        b = tmp

def solve(number):
    return sum(even_fib(number))

if __name__ == '__main__':
    n = int(raw_input())
    while n > 0:
        print solve(int(raw_input()))
        n -= 1
