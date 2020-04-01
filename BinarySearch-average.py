# -*- coding: utf-8 -*-
"""
価値がv_i, 重さがw_iである商品がN個
そこからk個選んで重さあたり価値の最大値を求める

Sulution:
解の存在範囲を二分探索で狭めていき効率的に最適解を求める
mid = (UpperBound + LowerBound) / 2 が条件を満たすかどうかを判定し、
OKなら UB ← mid, NGなら LB ← mid として存在範囲を定める
"""

''' data
3 2
2 2
5 3
2 1
'''

import numpy as np

n, k = map(int, input().split())
w = np.zeros(n)
v = np.zeros(n)

for i in range(n):
    w[i], v[i] = map(int, input().split())


def judge(x):
    value = v - x * w
    value.sort()
    return value[::-1][:k].sum() > 0


# xを二分探索する
ub = (v/w).max()
lb = 0

for _ in range(100):
    mid = (ub + lb) / 2
    res = judge(mid)
    print(mid, res)
    if res:
        lb = mid
    else:
        ub = mid

