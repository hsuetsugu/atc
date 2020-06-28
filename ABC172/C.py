# -*- coding: utf-8 -*-
# C

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline
import itertools

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = [0] + list(itertools.accumulate(a))
b = [0] + list(itertools.accumulate(b))


ans = 0
for i in range(n+1):
    if a[i] > k:
        break
    else:
        idx = bisect.bisect_right(b, k-a[i])
        # print(i, k-a[i], idx)
        ans = max(ans, i+idx-1)

print(ans)

