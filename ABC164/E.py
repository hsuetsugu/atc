# -*- coding: utf-8 -*-
# E

from heapq import heappop, heappush

MAX_V = 50
MAX_S = MAX_V*50 + 5


class Dijkstra(object):
    def __init__(self, n:int):
        self.adjacency_dict = {}
        self.n = n
        self.dp = [[float('inf')] * (MAX_S+5) for _ in range(self.n)]
        for i in range(n):
            self.add_vertex(i)
        self.heap_q = []

    def add_vertex(self, v: int):
        """ ノードを追加する """
        self.adjacency_dict[v] = {}
        self.C = []
        self.D = []

    def add_edge(self, v1: int, v2: int, a, b, undirected=False):
        self.adjacency_dict[v1][v2] = {"a":a,"b":b}
        if undirected:
            self.adjacency_dict[v2][v1] = {"a":a,"b":b}

    def push(self, v, m, x):
        if m < 0:  #お金がない
            return
        if self.dp[v][m] <= x:  #最短ではない
            return
        self.dp[v][m] = x
        heappush(self.heap_q, (x, v, m))

    def run(self, start: int, money: int) -> (list, list):
        # sからの距離とその前のノードを管理する
        # self.dp[start][money] = 0

        # プライオリティキューでstartから各ノードの(最短距離, ノードindex)を管理する
        self.push(start, money, 0)

        while len(self.heap_q) > 0:
            # 未確定な中から最小のノードを取得し、確定する
            x, v, m = heappop(self.heap_q)
            if self.dp[v][m] != x:
                continue

            # お金の更新
            nm = min(MAX_S, m + self.C[v])
            self.push(v, nm, x + self.D[v])

            # 最小のノードから直接リンクしているノードについて、時間(b)とお金(a)を更新する
            # print(v, self.adjacency_dict[v])
            for node in self.adjacency_dict[v].keys():
                self.push(node, m - self.adjacency_dict[v][node]['a'], x + self.adjacency_dict[v][node]['b'])

        return self.dp


N, M, S = map(int, input().split())

g = Dijkstra(N)

for _ in range(M):
    v1, v2, a, b = map(int, input().split())
    g.add_edge(v1 - 1, v2 - 1, a, b, undirected=True)

for _ in range(N):
    c, d = map(int, input().split())
    g.C.append(c)
    g.D.append(d)


# print(g.adjacency_dict)
# print(g.C, g.D)
res = g.run(start=0, money=S)

# print(res)

for i in range(1, N):
    print(min(res[i]))

