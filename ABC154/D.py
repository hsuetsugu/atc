# -*- coding: utf-8 -*-
# D

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

from itertools import accumulate

N, K = map(int, input().split())
P = list(map(int, input().split()))

cumsum = [0] + list(accumulate(P))
# print(cumsum)

res = []
for i in range(N-K+1):
    res.append(cumsum[i+K] - cumsum[i])

print((max(res)+K)/2)
