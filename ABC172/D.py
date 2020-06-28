# -*- coding: utf-8 -*-
# D

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
import itertools
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

n = int(input())

ans = 0

for i in range(1, n+1):
    num = n // i
    last = num * i
    ans += int((i + last) * num / 2)

print(ans)