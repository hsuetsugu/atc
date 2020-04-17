# -*- coding: utf-8 -*-
# F
# 条件を満たさないものを考えていき、包除原理を使う
# DFSでsからtまでの辿る辺をまず持っておく
# itertoolのproduct使うと便利
# population countは、bin(xx).count("1")が便利

# (u,v)のpathについて、10進数表記で整数で持つと早い
# 1つの制約を1つの整数Mで表したとき、全て満たすべき場合はM1 | M2　で表現できる


import itertools

'''
3
1 2
2 3
1
1 3
'''


class Graph(object):
    def __init__(self, n: int):
        self.adjacency_dict = {}
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

    def dfs_init(self, u, v):
        self.visited = [False] * self.n
        self.found = False
        # self.res = [0] * self.n
        self.res = 0
        self.dfs(u, v)
        return self.res

    def dfs(self, u, v):
        if u == v:
            self.found = True
            self.res += 1 << u
            return

        self.visited[u] = True
        for child in self.adjacency_dict[u]:
            if not self.visited[child]:
                self.dfs(child, v)
            if self.found:
                break

        if self.found:
            self.res += 1 << u


N = int(input())
g = Graph(N)
for _ in range(N-1):
    a, b = map(int, input().split())
    g.add_edge(a-1, b-1, undirected=True)

M = int(input())
constraint = {}
for m in range(M):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    constraint[m] = g.dfs_init(u, v)
# print(constraint)


def calc_combi(m, constraint):
    # M個中m(001101101)の制約を全て満たす組み合わせの数を計算する
    temp = 0
    cnt = 0
    for i in range(m.bit_length()):
        if (m >> i & 1) == 1:
            temp = temp | constraint[i]
            cnt += 1
    return temp, cnt


# 包除原理で計算していく
ans = pow(2, N-1)
for m in range(1, 2**M):
    res, cnt = calc_combi(m, constraint)

    if cnt % 2 == 0:
        ans += pow(2, N - bin(res).count('1'))
    else:
        ans -= pow(2, N - bin(res).count('1'))

print(ans)

