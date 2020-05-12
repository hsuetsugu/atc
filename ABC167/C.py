# -*- coding: utf-8 -*-
# C

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

import itertools

N, M, X = map(int, input().split())
data = []
for i in range(N):
    data.append(list(map(int, input().split())))

ans = float('inf')

for case in list(itertools.product('01', repeat=N)):
    val = [0] * M
    price = 0
    # print(case)
    for j in range(N):
        if case[j]=='1':
            price += data[j][0]
            for m in range(M):
                val[m] += data[j][m+1]

    flg = True
    for m in range(M):
        if val[m] < X:
            flg = False
    if flg:
        ans = min(ans, price)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
