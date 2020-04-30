# -*- coding: utf-8 -*-
# E
# 2分探索する
# X以上になる組み合わせがM個以上あるかで判定する

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)
from bisect import bisect_left
from itertools import accumulate

N, M = map(int, input().split())
A = list(map(int, input().split()))
# A.sort(reverse=True)
A.sort()

lb_x = 0
ub_x = 200000


def judge(x):
    res = 0
    for i in range(N):
        idx = bisect_left(A, x - A[i])
        res += N - idx
    return M > res


for _ in range(100):
    mid = (ub_x + lb_x) / 2
    res = judge(mid)
    print(mid, res)
    if res:
        ub_x = mid
    else:
        lb_x = mid

A_cumsum = list(accumulate(A))

ans = 0
for i in range(N):
    print(A_cumsum)
    idx = bisect_left(A, mid - A[i])
    print(i, idx)
    if idx < N:
        ans += A_cumsum[-1] - A_cumsum[idx-2]

print(ans)

''' naive (TLE)
# A1に対してをいれる
h = []
for i in range(N):
    heapq.heappush(h, (-(A[i]+A[0]), i, 0))

ans = 0
for i in range(M):
    val, idx, idx2 = heapq.heappop(h)
    ans -= val
    if idx2+1 < N:
        heapq.heappush(h, (-(A[idx]+A[idx2 + 1]), idx, idx2 + 1))

print(ans)
'''
