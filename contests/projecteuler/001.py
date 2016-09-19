#!/usr/bin/env python

def solve(number):
    number -= 1
    ret = 0

    t0 = number / 3
    ret += (t0 * (t0+1) / 2)*3
    t1 = number / 5
    ret += (t1 * (t1+1) / 2)*5
    t2 = number / 15
    ret -= (t2 * (t2+1) / 2)*15

    return ret

if __name__ == '__main__':
    n = int(raw_input())
    while n > 0:
        print solve(int(raw_input()))
        n -= 1
