# -*- coding: utf-8 -*-
# A - 深さ優先探索
"""
高橋君の住む街は長方形の形をしており、格子状の区画に区切られています。
長方形の各辺は東西及び南北に並行です。 各区画は道または塀のどちらかであり、
高橋君は道を東西南北に移動できますが斜めには移動できません。 また、塀の区画は通ることができません。
高君が、塀を壊したりすることなく道を通って魚屋にたどり着けるかどうか判定してください。
"""

'''
10 10
s.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
g.#.#.#.#.
#.#.#.#.#.
###.#.#.#.
#.....#...
'''


import sys

# 再起回数上限変更
sys.setrecursionlimit(1000000)


class Dbs(object):
    def __init__(self, H, W, data, sh, sw, gh, gw):
        self.H = H
        self.W = W

        self.data = data
        self.visited = [[False] * W for _ in range(H)]

        self.sh = sh
        self.sw = sw
        self.gh = gh
        self.gw = gw

    def search(self, r, c):
        """ row,colでサーチ試す，行けたら visited = Trueに設定 """
        if (r < 0) | (r > H - 1) | (c < 0) | (c > W - 1):
            return
        if self.data[r][c] == '#':
            return
        if self.visited[r][c]:
            return
        self.visited[r][c] = True
        if (r, c) == (gh, gw):
            print('Yes')
            sys.exit()

        self.search(r + 1, c)
        self.search(r - 1, c)
        self.search(r, c + 1)
        self.search(r, c - 1)


H, W = map(int, input().split())
mat = [[0] * W for _ in range(H)]

# matとstart, goal のindex
for ind_h in range(H):
    temp = input()
    for ind_w in range(W):
        mat[ind_h][ind_w] = temp[ind_w]
        if temp[ind_w] == 's':
            sh, sw = ind_h, ind_w
        elif temp[ind_w] == 'g':
            gh, gw = ind_h, ind_w

print(mat)


dbs = Dbs(H, W, mat, sh, sw, gh, gw)
dbs.search(sh, sw)
print('No')
