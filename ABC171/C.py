# -*- coding: utf-8 -*-
# C : 26進数

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
# import numpy as np

input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

n = int(input())

n -= 1
ans = []

while True:
    if n >= 26:
        ans.append(chr(ord('a') + (n % 26)))
        n = n // 26 -1
    else:
        ans.append(chr(ord('a') + (n % 26)))
        break

print(''.join(ans[::-1]))
