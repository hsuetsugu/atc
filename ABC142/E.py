# -*- coding: utf-8 -*-
# E
# bit DP
# AとBの論理差をとりたい場合は A & ~B でOK

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
a = []
b = []
c = []

for i in range(m):
    a_, b_ = map(int, input().split())
    c_ = list(map(int, input().split()))
    a.append(a_)
    b.append(b_)
    val = 0
    for _c_ in c_:
        val += 2 ** (_c_ -1)
    c.append(val)

max_m = 2**n

dp = [[float('inf')] * max_m for _ in range(m+1)]
dp[0][0]=0

# print(c)

for i in range(1, m+1):
    for combi in range(max_m):
        combi_diff = combi & ~c[i-1]
        dp[i][combi] = min(dp[i-1][combi], dp[i-1][combi_diff] + a[i-1])

if dp[-1][-1] == float('inf'):
    print(-1)
else:
    print(dp[-1][-1])

