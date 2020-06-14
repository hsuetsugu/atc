# -*- coding: utf-8 -*-
# Marin 2020 C
# 区間の累積和 ; O(N)で求まる
# https://atcoder.jp/contests/tokiomarine2020/tasks

'''
5 100
1 0 0 1 0
'''

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, K = map(int, input().split())
A = list(map(int, input().split()))
prev = A

for k in range(K):
    B = [0] * N
    for i in range(N):
        l = max(0, i-prev[i])
        r = min(N-1, i+prev[i])
        B[l] += 1
        if r+1 < N:
            B[r+1] -= 1
    for i in range(1, N):
        B[i] += B[i-1]
    if prev == B:
        break
    prev = B

for b in B:
    print(b, end=' ')
print()