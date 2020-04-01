# -*- coding: utf-8 -*-
# A - 深さ優先探索
"""
高橋君の住む街は長方形の形をしており、格子状の区画に区切られています。
長方形の各辺は東西及び南北に並行です。 各区画は道または塀のどちらかであり、
高橋君は道を東西南北に移動できますが斜めには移動できません。 また、塀の区画は通ることができません。
高君が、塀を壊したりすることなく道を通って魚屋にたどり着けるかどうか判定してください。
"""

import numpy as np
import sys

# 再起回数上限変更
sys.setrecursionlimit(20000)

converter = {'s': 0, 'g': 1, '.': 2, '#': 3}

H, W = map(int, input().split())
mat = np.zeros((H, W))
reached = np.zeros((H, W))

# matとstart, goal のindex
for ind_h in range(H):
    temp = input()
    for ind_w in range(W):
        mat[ind_h, ind_w] = converter[temp[ind_w]]
        if temp[ind_w] == 's':
            sh, sw = ind_h, ind_w
        elif temp[ind_w] == 'g':
            gh, gw = ind_h, ind_w


def search(x, y):
    """ x,y でサーチ試す，行けたらreached = 1に設定 """
    if (x < 0) | (x > H - 1) | (y < 0) | (y > W - 1):
        return
    if mat[x, y] == 3:
        return
    if reached[x, y] == 1:
        return
    reached[x, y] = 1
    if (x, y) == (gh, gw):
        print('Yes')
        sys.exit()

    search(x + 1, y)
    search(x - 1, y)
    search(x, y + 1)
    search(x, y - 1)


search(sh, sw)
print('No')