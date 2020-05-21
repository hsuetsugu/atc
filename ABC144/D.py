# -*- coding: utf-8 -*-
# D

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)
PI = math.pi

a, b, x = map(int, input().split())
x /= a

if x >= a * b / 2:
    x = a * b - x
    # print(x)
    # print(2*x/a**2)
    print(math.atan(2*x/a**2) * 180 / PI)
    sys.exit()
else:
    print(90 - math.atan(2 * x / b ** 2) * 180 / PI)
    sys.exit()


