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

h,w = map(int, input().split())
if h == 1 or w == 1:
    print(1)
elif (h%2==1) and (w%2==1):
    print(int((h * w // 2)+1))
else:
    print(int(h*w/2))
