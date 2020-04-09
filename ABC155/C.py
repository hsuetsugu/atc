# -*- coding: utf-8 -*-
# C


import collections


N = int(input())
S = [None] * N
for i in range(N):
    S[i] = input()

count = collections.Counter(S)
max_n = max(count.values())
# print(max_n)

keys = [k for k, v in count.items() if v == max_n]
keys.sort()

for s in keys:
    print(s)
