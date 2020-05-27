# -*- coding: utf-8 -*-
# B

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
import itertools

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())
d = list(map(int, input().split()))

ans = 0
for a, b in list(itertools.combinations(range(N), 2)):
    ans += d[a] * d[b]

print(ans)

