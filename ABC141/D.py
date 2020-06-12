# -*- coding: utf-8 -*-
# D

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
a = list(map(int, input().split()))

q = []
for t in a:
    # heappush(q, (-t, 0))
    heappush(q, -t)
# print(q)

for m in range(M):
    val = heappop(q)
    val = (-val)//2
    heappush(q, -val)

print(-sum(q))
