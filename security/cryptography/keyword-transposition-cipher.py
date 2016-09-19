#!/usr/bin/env python

def solve(key, cipher):
    m = key + sorted(set(range(0, 26)) - set(key))
    l = len(key)
    k = list()
    for c in sorted(key):
        i = key.index(c)
        k = k + m[i::l]
    reverse = dict()
    for idx, val in enumerate(k):
        reverse[chr(val+ord('A'))] = chr(idx + ord('A'))
    for s in cipher:
        print ''.join(map(reverse.get, s)),
    print

if __name__ == "__main__":
    n = int(raw_input())
    for i in range(n):
        tmp_dict = set()
        tmp_list = map(lambda x: ord(x)-ord('A'), raw_input())
        k = list()
        for t in tmp_list:
            if t not in tmp_dict:
                tmp_dict.add(t)
                k.append(t)
        c = raw_input().split()
        solve(k, c)
