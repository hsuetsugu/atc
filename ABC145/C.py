# -*- coding: utf-8 -*-
# C

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

from itertools import permutations

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())
data = []
for i in range(N):
    data.append(list(map(int, input().split())))

cases = list(permutations(list(range(N)), N))

ans = 0
for case in cases:
    dist = 0
    for i in range(1, N):
        a, b = case[i-1], case[i]
        dist += ((data[a][0] - data[b][0])**2 + (data[a][1] - data[b][1])**2)**.5
    ans += dist

print(ans/len(cases))


