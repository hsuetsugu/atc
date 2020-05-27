# -*- coding: utf-8 -*-
# E

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)


class Warshall(object):
    """ 全てのノード間の最短路を計算する """
    def __init__(self, n:int):
        self.adjacency_dict = {}
        self.n = n
        for i in range(n):
            self.add_vertex(i)

            for j in range(n):
                if i == j:
                    self.adjacency_dict[i][j] = 0
                else:
                    self.adjacency_dict[i][j] = float('inf')

    def add_vertex(self, v: int):
        """ ノードを追加する """
        self.adjacency_dict[v] = {}

    def add_edge(self, v1: int, v2: int, w: float, undirected=False):
        self.adjacency_dict[v1][v2] = w
        if undirected:
            self.adjacency_dict[v2][v1] = w

    def run(self):
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    self.adjacency_dict[i][j] = min(
                        self.adjacency_dict[i][j],
                        self.adjacency_dict[i][k] + self.adjacency_dict[k][j]
                    )


if __name__ == '__main__':
    N, M, L = map(int, input().split())

    g = Warshall(N)
    g2 = Warshall(N)
    for _ in range(M):
        v1, v2, w = map(int, input().split())
        if w <= L:
            g.add_edge(v1 - 1, v2 - 1, w, undirected=True)
            # g2.add_edge(v1 - 1, v2 - 1, 1, undirected=True)
    g.run()

    for i in range(N):
        for j in range(N):
            if g.adjacency_dict[i][j] <= L:
                g2.adjacency_dict[i][j] = 1
    g2.run()

    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        ans = g2.adjacency_dict[s-1][t-1]
        if ans == float('inf'):
            print(-1)
        else:
            print(ans -1)
