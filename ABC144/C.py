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
a = int(N ** .5)

for num in range(a):
    num = a - num
    if N % num == 0:
        b = N // num
        # print(b, num)
        print(b + num -2)
        sys.exit()


