# -*- coding: utf-8 -*-
# C

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

import math
a, b, c = map(int, input().split())

a1 = a + b - c
if a1 >0:
    print('No')
    sys.exit()

if a1**2 - 4 * a * b > 0:
    print('Yes')
else:
    print('No')