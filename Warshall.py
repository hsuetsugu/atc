# -*- coding: utf-8 -*-
# Warshall
# O(n**3)

'''
3 2 5
1 2 3
2 3 3
'''


class Warshall(object):
    def __init__(self, n:int):
        self.cost = [[float('inf')] * n for _ in range(n)]

        self.n = n
        for i in range(n):
            self.cost[i][i] = 0

    def add_edge(self, v1: int, v2: int, w: float, undirected=False):
        self.cost[v1][v2] = w
        if undirected:
            self.cost[v2][v1] = w

    def run(self):
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    self.cost[i][j] = min(
                        self.cost[i][j],
                        self.cost[i][k] + self.cost[k][j]
                    )


if __name__ == '__main__':
    N, M, L = map(int, input().split())

    g = Warshall(N)
    for _ in range(M):
        v1, v2, w = map(int, input().split())
        if w <= L:
            g.add_edge(v1 - 1, v2 - 1, w, undirected=True)
    g.run()

    print(g.cost)
