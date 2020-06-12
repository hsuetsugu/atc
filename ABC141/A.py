# -*- coding: utf-8 -*-
# A

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)


s = input()[:-1]

if s == 'Sunny':
    print('Cloudy')
elif s == 'Cloudy':
    print('Rainy')
else:
    print('Sunny')
