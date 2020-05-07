# -*- coding: utf-8 -*-
# C

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

A, B, X = map(int, input().split())

max_n = X // A
max_keta = len(str(max_n)) + 1

res = []
for keta in range(1, max_keta+1):
    val = (X - keta * B) // A
    if val < 0:
        continue
    if A * val + B * len(str(val)) > X:
        continue
    if len(str(val)) == keta:
        res.append(val)
    if len(str(val)) > keta:
        res.append(int('9'*keta))

# print(res)

if len(res)==0:
    print(0)
else:
    print(min(10**9, max(res)))
