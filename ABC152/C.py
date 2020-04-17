# -*- coding: utf-8 -*-
# C

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())
P = list(map(int, input().split()))

current_min = float('inf')
cnt = 0
for i in range(N):
    if P[i] <= current_min:
        cnt += 1
        current_min = P[i]

print(cnt)
