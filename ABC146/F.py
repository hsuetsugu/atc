# -*- coding: utf-8 -*-
# F

from collections import deque
import sys

N, M = map(int, input().split())
S = list(input())[::-1]

d = deque()
res = []
prev_idx = 0

while True:
    found = False
    idx = prev_idx
    for m in range(M):
        idx += 1
        if S[idx] == '0':
            # print(idx)
            d.append(m+1)
            found = True
            prev_idx = idx
        if idx == N:
            res.append(str(d.pop()))
            print(' '.join(res[::-1]))
            sys.exit()
    if not found:
        print(-1)
        sys.exit()
    res.append(str(d.pop()))


