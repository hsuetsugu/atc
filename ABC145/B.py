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
S = input()
num = len(S)
if num % 2 == 1:
    print('No')
    sys.exit()

num = num //2
if S == S[:num]*2:
    print('Yes')
else:
    print('No')