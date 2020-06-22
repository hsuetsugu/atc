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

n = int(input())
a = list(map(int, input().split()))

res = 0
for a_ in a:
    res = a_ ^ res

for a_ in a:
    print(a_ ^ res, end=' ')
print()
