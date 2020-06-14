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

a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if v <= w:
    print('NO')
else:
    if (v-w) * t >= abs(a - b):
        print('YES')
    else:
        print('NO')
