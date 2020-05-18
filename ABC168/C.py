# -*- coding: utf-8 -*-
# C

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

import math
PI = math.pi

a, b, h, m = map(int, input().split())
x1 = a * math.cos((PI/2) - 2*PI*(60*h+m)/720)
y1 = a * math.sin((PI/2) - 2*PI*(60*h+m)/720)
x2 = b * math.cos((PI/2) -2*PI*m/60)
y2 = b * math.sin((PI/2) -2*PI*m/60)


print(((x2-x1)**2 + (y2-y1)**2)**.5)
