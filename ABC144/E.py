# -*- coding: utf-8 -*-
# E
# 単純にheapqに入れていくのだとKが大きいのでTLE
# 2分探索が必要

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

A.sort(reverse=True)
F.sort()


def judge(x):
    val = 0
    for i in range(N):
        val += max(A[i] - x // F[i], 0)
        if val > K:
            return False
    if val <= K:
        return True


ub = 10**12
lb = -1

while lb + 1 < ub:
    x = (ub+lb)/2
    if judge(x):
        ub = x
    else:
        lb = x

print(int(ub))



'''
q = []
ws = []
cnt = 0

for i in range(N):
    heappush(q, (-A[i]*F[i], A[i], F[i]))
    ws.append(A[i]*F[i])

ws.append(0)
ws.sort(reverse=True)

# print(ws)

for w in ws[1:]:
    # print(w)
    while True:
        # print(w, q)
        val, a, f = heappop(q)
        if val == 0:
            print(-val)
            sys.exit()
        if -val <= w:
            heappush(q, (-a*f, a, f))
            break
        else:
            # a * f < wになるまでaを減らす
            a_n = w // f
            if w== 0:
                diff = 1
            else:
                diff = min(K - cnt, a - a_n)
            cnt += diff
            a -= diff
            heappush(q, (-a*f, a, f))
        # print(w, cnt)
        if cnt >= K:
            break

# print(q)
val, a, f = heappop(q)
print(-val)
'''

