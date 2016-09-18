#!/usr/bin/env python

m = raw_input()
k = int(raw_input())
print ''.join(map(lambda x: str((x+k)%10), map(int, m)))
