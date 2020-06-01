# -*- coding: utf-8 -*-
# F

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
from itertools import accumulate, combinations
input = sys.stdin.readline

mod = 998244353

N, S = map(int, input().split())
A = list(map(int, input().split()))
A.sort()


def calc_cnt(n, s):
    cnt = 0
    for i in combinations(A, n+1):
        # print(i)
        if sum(i) == s:
            cnt += 1
    return cnt

A_cum = list(accumulate(A))

vs = []
for i in range(0, N):
    if A_cum[i] > S:
        vs.append(0)
        continue
    res = calc_cnt(i, S)
    print(i, S, res)

    vs.append(calc_cnt(i, S))

print(vs)

ans = 0
for idx, v in enumerate(vs):
    if idx > 0:
        ans += v + ans*(N-idx)//idx
    else:
        ans += v
    ans = ans % mod

print(ans)

