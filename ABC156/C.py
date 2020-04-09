# -*- coding: utf-8 -*-
# C -

'''
7
14 14 2 13 56 2 37
'''

import sys

# 再起回数上限変更
sys.setrecursionlimit(1000000)

N = int(input())
x = list(map(int, input().split()))

P = sum(x) / N
P = int(P)

res1 = sum([(x[i] - P)**2 for i in range(N)])
if P + 1 <= 100:
    res2 = sum([(x[i] - (P+1))**2 for i in range(N)])
else:
    res2 = float('inf')

print(min(res1, res2))
