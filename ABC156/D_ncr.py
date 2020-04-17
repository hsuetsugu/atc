# -*- coding: utf-8 -*-
# D

# 繰り返し二乗法　＋　フェルマーの小定理
# mod Z(Zは素数）の世界では、Yで割ることと、Y^(Z-2)をかけることが等価
# これを使ったnCaとnCbを差し引く

'''
4 1 3
'''

import math
DIVISOR = 10**9 + 7


def comb(n, r):
    res1 = 1
    # 分子
    for i in range(r):
        res1 = (res1 * (n-i)) % DIVISOR

    # 分母
    res2 = 1
    for i in range(r):
        res2 = (res2 * (i+1)) % DIVISOR
    res2 = power_mod(res2, DIVISOR - 2, DIVISOR)
    return (res1 * res2) % DIVISOR


def power_mod(n, k, m):
    if k == 0:
        return 1
    elif k % 2 == 1:
        return power_mod(n, k-1, m) * (n % m) % m
    elif k % 2 == 0:
        temp = power_mod(n, k/2, m)
        return (temp % m) * (temp % m) % m


n, a, b = map(int, input().split())

S = 2 * power_mod(2, n-1, DIVISOR)
S = (S - 1) % DIVISOR
# print(S)

# print(comb(n, a))
# print(comb(n, b))

S = S - comb(n, a) - comb(n, b)

print(S % DIVISOR)
