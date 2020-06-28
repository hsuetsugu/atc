# -*- coding: utf-8 -*-
# E

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
mod = 10**9 + 7

a = [0] * (n+1)
b = [0] * (n+1)

a[1] = m
b[1] = m-1

ans = a[1] * b[1]

for i in range(2, n+1):
    val1 = (m-i+1) * (i-1)
    val2 = (m-i) * (m- 2*i +2)
    val = int(val1 + val2)
    # print(val)
    ans *= val % mod
    ans = ans % mod

print(ans % mod)
