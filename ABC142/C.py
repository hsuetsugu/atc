# -*- coding: utf-8 -*-
# C

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())
A = list(map(int, input().split()))

dic= defaultdict(int)
for idx, a in enumerate(A):
    dic[a] = idx + 1

for i in range(1,N+1):
    print(dic[i], end=' ')
print()
