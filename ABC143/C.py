# -*- coding: utf-8 -*-
# C

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)


N = int(input())
S = input()

val = '0'
ans = 0
for s in S:
    if s == val:
       continue
    else:
        ans += 1
        val = s

print(ans)
