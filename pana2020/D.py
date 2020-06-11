# -*- coding: utf-8 -*-
# D

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
from itertools import combinations
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

n = int(input())
if n == 1:
    print('a')
    sys.exit()


def dfs(s):
    if len(s) == n:
        print(''.join([chr(s + ord('a')) for s in s]))
    else:
        for i in range(len(set(list(s))) + 1):
            dfs(s + [i])
dfs([])
