# -*- coding: utf-8 -*-
# A

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

A, B = map(int, input().split())
if A < 10 and B<10:
    print(A*B)
else:
    print('-1')
