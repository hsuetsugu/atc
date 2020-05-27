# -*- coding: utf-8 -*-
# D

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())
L = list(map(int, input().split()))

L.sort(reverse=True)
acm_l = []

for i in range(1, N-1):
    acm_l.append([ -(L[i] + L[j]) for j in range(i+1, N)])

# print(L)
# print(acm_l)


ans = 0
for i, l in enumerate(L[:-2]):
    for j in range(i, N-2):
        idx = bisect.bisect_left(acm_l[j], -l)
        # print(acm_l[j], l, idx)
        ans += idx

print(int(ans))
