# -*- coding: utf-8 -*-
# C

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)
import math
from functools import reduce


K = int(input())
res = [[[0] * (K+1) for i in range(K+1)] for j in range(K+1)]


def gcd(numbers):
    global res

    numbers.sort()
    if res[numbers[0]][numbers[1]][numbers[2]] > 0:
        return res[numbers[0]][numbers[1]][numbers[2]]
    else:
        val = reduce(math.gcd, (numbers[0], numbers[1],numbers[2]))
        res[numbers[0]][numbers[1]][numbers[2]] = val
        return val


ans = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            ans += gcd([a, b, c])

print(ans)
