# -*- coding: utf-8 -*-
# C

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

import itertools

N, M, Q = map(int, input().split())
data = []
for i in range(Q):
    data.append(list(map(int, input().split())))

ans = 0
for ite in itertools.combinations_with_replacement(range(1,M+1), N):
    val = 0
    for q in data:
        if ite[q[1]-1] - ite[q[0]-1] == q[2]:
            val += q[3]
    ans = max(ans, val)

print(ans)

