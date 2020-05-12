# -*- coding: utf-8 -*-
# E

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, T = map(int, input().split())
data = []
for i in range(N):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x: x[0])
A = [d[0] for d in data]
B = [d[1] for d in data]

dp = [[0]*T for _ in range(N+1)]

used = [[0]*T for _ in range(N+1)]

for i in range(1, N+1):
    idx = i - 1
    for j in range(T):
        dp[i][j] = dp[i - 1][j]
        if j - A[idx] >= 0:
            if dp[i-1][j-A[idx]] + B[idx] > dp[i-1][j]:
                dp[i][j] = dp[i-1][j-A[idx]]+ B[idx]
                used[i][j] = A[idx]

t = T-1
items = []

# print(dp[N])
# print(used)

for i in list(range(1, N+1))[::-1]:
    val = used[i][t]
    if val>0:
        items.append(i-1)
        t -= val

# print(items)
if len(items) == N:
    print(dp[N][T - 1])
    sys.exit()

a = [b for idx, b in enumerate(B) if idx not in items]
print(dp[N][T-1] + max(a))

