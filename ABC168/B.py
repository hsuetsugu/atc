# -*- coding: utf-8 -*-
# B

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

K = int(input())
S = input()

if len(S)<=K:
    print(S)
else:
    print(S[:K] + '...')
