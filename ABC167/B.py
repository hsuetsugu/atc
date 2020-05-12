# -*- coding: utf-8 -*-
# B

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

a, b, c, k = map(int, input().split())

ans = 0
ans += min(k, a)
k -= a
if k <= 0:
    print(ans)
    sys.exit()

k -= b
if k <= 0:
    print(ans)
    sys.exit()

ans -= k
print(ans)
