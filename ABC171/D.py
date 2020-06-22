# -*- coding: utf-8 -*-
# D

import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

co = defaultdict(int)

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = []
c = []

for a_ in a:
    co[a_] += 1
# print(co)

ans = sum(a)

for _ in range(q):
    b_, c_ = map(int, input().split())
    b.append(b_)
    c.append(c_)

    diff = - co[b_] * b_
    diff += co[b_] * c_
    co[c_] += co[b_]
    co[b_] = 0
    ans += diff
    print(ans)


