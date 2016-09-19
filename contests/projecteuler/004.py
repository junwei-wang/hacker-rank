#!/usr/bin/env python
# -*- coding: utf-8 -*-

# only search 11's multiple, since 111111=143*777
# p(x) = xyzzyx (6 digits) = 100000x + 10000y + 1000z + 100z + 10y + x
#      = 11(9091x + 910y + 100z)
def make_table():
    def is_palindromic(num):
        num = str(num)
        for i in range(len(num)/2):
            if num[i] != num[-i-1]:
                return False
        return True

    table = set()
    for i in range(990, 100, -11):
        for j in range(999, 99, -1):
            prod = i * j
            if is_palindromic(prod):
                table.add(prod)
    return sorted(table)

def solve(num, table):
    return max(filter(lambda x: x < num, table))

if __name__ == '__main__':
    table = make_table()
    n = input()
    while n > 0:
        print solve(input(), table)
        n -= 1
