# -*- coding: utf-8 -*-
# E

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)
N = int(input())
data = defaultdict(int)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# a, b = (0,0)はそれを入れるのみなので，
# カウントから抜かして(a,b)の数を最後に足せば良い
# どちらかが0の場合は，
# a=0ならb=0のモノが対比となる

cnt_zero = 0

for i in range(N):
    a, b = map(int, input().split())
    div = gcd(abs(a), abs(b))

    # マイナスはaだけ
    if a <0 and b <0:
        a, b = -a, -b
    elif b < 0:
        a, b = -a, -b

    if a ==0 and b==0:
        cnt_zero += 1
        continue

    if a ==0:
        data[(0, 1)] += 1
        data[(1, 0)] += 0
        continue

    if b ==0:
        data[(1, 0)] += 1
        data[(0, 1)] += 0
        continue

    data[(a//div, b//div)] += 1
    if a > 0:
        data[(-b//div, a//div)] += 0
    else:
        data[(b // div, -a // div)] += 0

mod = 1000000007
res = 1


for d in data:
    if d[0]>0 and d[1]>0:
        val = data[d]
        a1 = data[(-d[1], d[0])]
        # print(d, val, a1)
        if val == 0:
            res *= pow(2, a1, mod)
        elif a1 > 0:
            res *= pow(2, val, mod) + pow(2, a1, mod) - 1
            data[(-d[1], d[0])] = 0
        else:
            res *= pow(2, val, mod)
        res %= mod
        # print(res)
    # aが0の場合
    if d[0]==0:
        val = data[d]
        a1 = data[(1, 0)]

        if val == 0:
            res *= pow(2, a1, mod)
        elif a1 > 0:
            res *= pow(2, val, mod) + pow(2, a1, mod) - 1
        else:
            res *= pow(2, val, mod)
        res %= mod

print((res+cnt_zero-1)%mod)
