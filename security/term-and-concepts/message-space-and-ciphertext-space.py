#!/usr/bin/env python

print ''.join(map(lambda x: str((x+1)%10), map(int, raw_input())))
