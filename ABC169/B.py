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

N= int(input())
A = list(map(int, input().split()))
A.sort()

ans = 1
for a in A:
    ans *= a
    if a == 0:
        print(0)
        sys.exit()
    if ans > 10**18:
        print(-1)
        sys.exit()
print(ans)
