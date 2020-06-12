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

s = input()[:-1]

ans = True
for i in range(len(s)):
    if (i+1) % 2 == 1:
        # print(1, s[i])
        if s[i] == 'L':
            ans =False
            break
    if (i + 1) % 2 == 0:
        # print(2, s[i])
        if s[i] =='R':
            ans = False
            break

if ans:
    print('Yes')
else:
    print('No')

