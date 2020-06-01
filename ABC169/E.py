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


N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if N % 2 == 0:
    min_x = (A[N//2] + A[(N//2)-1]) / 2
    max_x = (B[N//2] + B[(N//2)-1]) / 2
    # print(min_x, max_x)
    ans = (max_x - min_x)*2 + 1
else:
    min_x = A[N//2]
    max_x = B[N//2]
    # print(min_x, max_x)
    ans = max_x - min_x + 1

print(int(ans))
