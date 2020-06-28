# -*- coding: utf-8 -*-
# B

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

s = input()
t = input()

ans = 0
for i in range(len(s)):
    if s[i] == t[i]:
        pass
    else:
        ans += 1

print(ans)
