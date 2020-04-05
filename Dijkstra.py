# -*- coding: utf-8 -*-
# Dijkstra

import numpy as np
from heapq import heappop, heappush

'''
5 6
2 1 1
1 3 3
3 2 5
3 4 10
4 1 2
4 5 4
'''


class Dijkstra(object):
    def __init__(self, n: int):
        """ ノードのつながりを辞書型で表現する
        要素数nであり、要素は0からn-1である想定
        >> - usage
        g = Graph(n=n)

        """
        self.adjacency_dict = {}
        self.n = n
        for i in range(n):
            self.add_vertex(i)

    def add_vertex(self, v: int):
        """ ノードを追加する """
        self.adjacency_dict[v] = {}

    def add_edge(self, v1: int, v2: int, w: float, undirected=False):
        self.adjacency_dict[v1][v2] = w
        if undirected:
            self.adjacency_dict[v2][v1] = w

    def run(self, start: int) -> (list, list):
        """ startから初めてそれ以外のノードへの最短距離をダイクストラ法で求める """
        # sからの距離とその前のノードを管理する
        dist = [np.inf] * self.n
        prev = [None] * self.n
        heap_q = []

        dist[start] = 0

        # プライオリティキューでstartから各ノードの(最短距離, ノードindex)を管理する
        heappush(heap_q, (0, start))

        while len(heap_q) > 0:
            # 未確定な中から最小のノードを取得し、確定する
            d, l = heappop(heap_q)

            # 最小のノードから直接リンクしているノードについて、距離が縮まるようであれば更新する
            for node in self.adjacency_dict[l].keys():
                new_dist = dist[l] + self.adjacency_dict[l][node]
                if dist[node] > new_dist:
                    dist[node] = new_dist
                    heappush(heap_q, (new_dist, node))
                    prev[node] = l

        return dist, prev


if __name__ == '__main__':
    N, Q = map(int, input().split())

    g = Dijkstra(N)
    for _ in range(Q):
        v1, v2, w = map(int, input().split())
        g.add_edge(v1 - 1, v2 - 1, w)

    print(g.adjacency_dict)

    dist, prev = g.run(start=0)
    print(dist)
    print(prev)
