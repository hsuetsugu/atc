# -*- coding: utf-8 -*-
# A

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

S = input()
T = input()

if (S == T[:-1]) and (len(S)+1 == len(T)):
    print('Yes')
else:
    print('No')
