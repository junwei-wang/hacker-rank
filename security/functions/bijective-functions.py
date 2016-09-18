#!/usr/bin/env python

n = int(raw_input())
line = raw_input().split()
num = set(map(int, line))
print 'YES' if n == len(num) else 'NO'
