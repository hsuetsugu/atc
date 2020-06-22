# -*- coding: utf-8 -*-
# F : 途中

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

k = int(input())
s = input()
l = len(s)
mod = 10**9 + 7

def cmb_(n, r):
    from operator import mul
    from functools import reduce

    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


ans = 0
for m in range(k+1):
    ans += cmb_(l+m, m) * pow(25, m, mod) * pow(26, k-m, mod)
    ans = ans % mod

print(ans)

