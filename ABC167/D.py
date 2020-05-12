# -*- coding: utf-8 -*-
# D

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())
a = map(int, input().split())
a = [a-1 for a in a]

first = 0
second = 0
cnt = 0
visited = [0] * N
city = [None] * N

def nex_node(x):
    global first
    global second
    global cnt
    city[cnt] = x
    cnt += 1

    if visited[x] > 0:
        first = visited[x]
        second = cnt
        val = K - first +1
        idx = val % (second - first)
        # print(first, second, idx)
        # print(city)
        print(city[first - 1 +idx] + 1)
        sys.exit()

    visited[x] = cnt

    # print(x, cnt, a[x])
    if cnt == K:
        # print(city)
        print(a[x]+1)
        sys.exit()
    if a[x] == x:
        print(x+1)
        sys.exit()

    nex_node(a[x])


nex_node(0)
