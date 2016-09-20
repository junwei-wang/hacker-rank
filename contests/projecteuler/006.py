#!/usr/bin/env python
# -*- coding: utf-8 -*-
def solve(num):
    return ((num*(num+1))/2)**2 - num*(num+1)*(2*num+1)/6

if __name__ == '__main__':
    n = input()
    while n > 0:
        print solve(input())
        n -= 1
