# -*- coding: utf-8 -*-
# F: 2次元での三分探査
# 最小包含円を探索する（中心と半径）

import math

N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


def calc_r(x0, y0):
    # 全ての点の中で最も遠いところまでの距離を返す
    res = 0
    for i in range(N):
        res = max(res, ((X[i] - x0)**2 + (Y[i] - y0)**2))

    return res


# lb_x, ub_x = min(X), max(X)
lb_x, ub_x = 0.0, 1000.0


def g(x):
    # lb_y, ub_y = min(Y), max(Y)
    lb_y, ub_y = 0.0, 1000.0

    # yを探索する
    for _ in range(100):
        y1 = lb_y + (ub_y - lb_y) / 3
        y2 = ub_y - (ub_y - lb_y) / 3

        if calc_r(x, y1) > calc_r(x, y2):
            lb_y = y1
        else:
            ub_y = y2
    return calc_r(x, lb_y)


for _ in range(100):
    # あるxにおいて半径が最小となる円を求める
    x1 = lb_x + (ub_x - lb_x) / 3
    x2 = ub_x - (ub_x - lb_x) / 3

    if g(x1) > g(x2):
        lb_x = x1
    else:
        ub_x = x2

print(math.sqrt(g(lb_x)))

