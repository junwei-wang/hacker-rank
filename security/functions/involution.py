#!/usr/bin/env python

n = int(raw_input())
f = map(int, raw_input().split())

flag = True
for i in range(n):
    if f[f[i]-1] != i+1:
        flag = False
        print "NO"
        break

if flag:
    print "YES"
