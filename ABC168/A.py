# -*- coding: utf-8 -*-
# A

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())

num = N % 10
if num in [2,4,5,7,9]:
    print('hon')
elif num in [0,1,6,8]:
    print('pon')
else:
    print('bon')

