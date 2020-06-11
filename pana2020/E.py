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

a = input()[:-1]
b = input()[:-1]
c = input()[:-1]
max_shift = max(len(a),len(b),len(c))*2

ans = float('inf')

for i in range(-max_shift, max_shift):
    for j in range(-max_shift, max_shift):
        start = min(i, j, 0)
        end = max(len(a), i+len(b), j+len(c))
        if (end - start) > ans:
            continue

        s = ['?'] * (end - start)
        flg = False

        for idx in range(len(a)):
            s[idx - start] = a[idx]

        for idx in range(len(b)):
            if flg:
                break
            if s[i - start + idx] == '?':
                s[i - start + idx] = b[idx]
            elif (b[idx] == '?') or (s[i - start + idx] == b[idx]):
                pass
            else:
                flg=True

        for idx in range(len(c)):
            if flg:
                break
            if s[j - start + idx] == '?':
                s[j - start + idx] = c[idx]
            elif (c[idx] == '?') or (s[j - start + idx] == c[idx]):
                pass
            else:
                flg=True

        if not flg:
            # print(s)
            ans = min(ans, (end-start))

print(ans)



