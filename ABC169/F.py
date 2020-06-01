# -*- coding: utf-8 -*-
# F

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
from itertools import accumulate, combinations
input = sys.stdin.readline

mod = 998244353

N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (S+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(S+1):
        dp[i][j] += dp[i-1][j] * 2
        if j + A[i-1] <= S:
            dp[i][j+A[i-1]] += dp[i-1][j]
        dp[i][j] %= mod

# print(dp)
print(dp[-1][S] % mod)
