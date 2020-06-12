# -*- coding: utf-8 -*-
# C

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, K, Q = map(int, input().split())
d = [0] * N
for _ in range(Q):
    a = int(input())
    d[a-1] += 1

for i in range(N):
    # print(K - Q + d[i])
    if K - Q + d[i] >0:
        print('Yes')
    else:
        print('No')
