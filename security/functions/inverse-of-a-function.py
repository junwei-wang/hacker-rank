#!/usr/bin/env python

n = int(raw_input())
f = map(int, raw_input().split())
g = [0] * len(f)
for i, v in enumerate(f):
    g[v-1] = i+1
for n in g:
    print n
