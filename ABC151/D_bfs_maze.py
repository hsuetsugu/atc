# -*- coding: utf-8 -*-
# D

# BFSで各点から到達可能な最も遠いところを探索する
# 1回探索はO(HW)なのでO(HHWW)
# dequeでBFSする

# 周囲に'#'で埋めると処理がシンプルになる（W+2, H+2にするのを忘れずに）



'''
3 5
...#.
.#.#.
.#...
'''

import sys
from collections import deque

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces


H, W = na()
# data = [ns() for _ in range(H)]

data = [list("#" * (W + 2))]
# 周りを'#'で埋めておく
for _ in range(H):
    data.append(["#"] + list(input()) + ["#"])
data += [list("#" * (W + 2))]


def bfs(h, w):
    dist = [[-1] * (W+2) for _ in range(H+2)]
    q = deque()

    max_dist = 0
    dist[h][w] = 0
    q.append((h, w, 0))

    # while len(q) > 0:
    while len(q) > 0:
        h, w, val = q.popleft()

        m = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in m:
            h_new, w_new = h + dx, w + dy
            if data[h_new][w_new] == '.' and dist[h_new][w_new] == -1:
                q.append((h_new, w_new, val+1))
                dist[h_new][w_new] = val + 1
                max_dist = max(max_dist, val + 1)

    return max_dist


ans = 0
for h in range(H+2):
    for w in range(W+2):
        if data[h][w] == '.':
            res = bfs(h, w)
            if ans < res:
                ans = res

print(ans)
