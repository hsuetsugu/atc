# -*- coding: utf-8 -*-
# B

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

import math

X = int(input())
N = 10**8

a = 100
ans = 0
for i in range(N):
    a = math.floor(a * 1.01)
    ans += 1
    if a >= X:
        print(ans)
        sys.exit()
