# -*- coding: utf-8 -*-
# B

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())

for i in range(1, 10):
    if N % i == 0 and N // i < 10:
        print('Yes')
        sys.exit()
print('No')
