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

N, k = map(int, input().split())
h = list(map(int, input().split()))
# print(h)
h.sort()
a = bisect.bisect_left(h, k)
print(N-a)
