# -*- coding: utf-8 -*-
# C

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, M = map(int, input().split())



class Graph(object):
    def __init__(self, n:int):
        """ ノードのつながりを辞書型で表現する
        要素数nであり、要素は0からn-1である想定
        >> - usage
        g = Graph(n=n)

        """
        self.adjacency_dict = {}
        self.val = [0] * n
        self.good = [1] * n
        self.n = n
        for i in range(n):
            self.add_vertex(i)

    def add_vertex(self, v: int):
        """ ノードを追加する """
        self.adjacency_dict[v] = []

    def add_edge(self, v1: int, v2: int, undirected=False):
        self.adjacency_dict[v1].append(v2)
        if undirected:
            self.adjacency_dict[v2].append(v1)


g = Graph(N)

h = list(map(int, input().split()))
for i in range(N):
    g.val[i] = h[i]

for m in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    g.add_edge(a, b, undirected=True)
    val_a, val_b = h[a], h[b]

    if val_a == val_b:
        g.good[a] = 0
        g.good[b] = 0
    if val_a > val_b:
        g.good[b] = 0
    if val_a < val_b:
        g.good[a] = 0


ans = 0
for i in g.good:
    if i == 1:
        ans += 1
print(ans)
