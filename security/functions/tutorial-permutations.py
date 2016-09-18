#!/usr/bin/env python

n = int(raw_input())
f = map(int, raw_input().split())

for i in range(n):
    print f[f[i]-1]
