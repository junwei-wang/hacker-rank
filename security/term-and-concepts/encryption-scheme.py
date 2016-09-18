#!/usr/bin/env python

m = int(raw_input())
print reduce(lambda x, y: x*y, range(1, m+1))
