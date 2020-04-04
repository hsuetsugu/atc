# -*- coding: utf-8 -*-
# B - Union Find
# https://atcoder.jp/contests/atc001/tasks/unionfind_a
'''
入力例
8 9
0 1 2
0 3 2
0 2 4
0 4 2
0 0 0
0 5 7
0 2 5
1 3 5
1 0 0
'''
import sys

debug = False
N, Q = map(int, input().split())
# print(sys.getrecursionlimit())
sys.setrecursionlimit(20000)


class Graph(object):
    def __init__(self, N, directed=False):
        """ ノードのつながりを辞書型で表現する """
        self.adjacency_dict = {}
        self.directed = directed
        self.parent = [None] * N

        for i in range(N):
            self.add_vertex(i)
            self.parent[i] = i
        self.rank = [0] * N

    def add_vertex(self, v):
        """ ノードを追加する """
        self.adjacency_dict[v] = []

    def add_edge(self, v1, v2):
        """ ノード同士をつなぐ。"""
        if v1 == v2:
            return

        # if not self._has_direct_vertex(v1, v2):
        #     self.adjacency_dict[v1].append(v2)
        # v1, v2の親同士をつなげる
        p1 = self.find_parent(v1)
        p2 = self.find_parent(v2)

        self.parent[v1] = p1
        self.parent[v2] = p2

        if p1 != p2:
            if self.rank[p1] == self.rank[p2]:
                self.update(p1, p2)
                self.rank[p2] += 1
            elif self.rank[p1] < self.rank[p2]:
                self.update(p1, p2)
            else:
                self.update(p2, p1)

        if not self.directed:
            if not self._has_direct_vertex(v2, v1):
                self.adjacency_dict[v2].append(v1)

    def update(self, v, parent):
        self.adjacency_dict[v].append(parent)

        # children = self.find_children(v, [v])
        # printt(f'children of {v}:{children} to {parent}', debug)
        # or v in children:
        #     self.parent[v] = parent

    def has_link_fast(self, v1, v2):
        """ 親が同一であれば連結 """
        parent_v1 = self.find_parent(v1)
        parent_v2 = self.find_parent(v2)

        self.parent[v1] = parent_v1
        self.parent[v2] = parent_v2

        if parent_v1 == parent_v2:
            return True
        else:
            return False

    def find_parent(self, v1):
        """ vから上向きに辿って根を調べる """
        # return self.parent[v1]

        # 最上位ノード
        if self.adjacency_dict[v1] == []:
            return v1

        # parentが格納されていればそこまではジャンプする
        # if self.parent[v1] is not None:
        #     parent = self.find_parent(self.parent[v1])
        #     return parent

        # なければ辿っていく
        for v in self.adjacency_dict[v1]:
            parent = self.find_parent(v)
        return parent


    def print_graph(self):
        print(self.adjacency_dict)

    def _has_direct_vertex(self, v1, v2):
        """ 直接連結しているかを確認する """
        if v2 in self.adjacency_dict[v1]:
            return True
        else:
            return False

    def find_children(self, v_parent, children: list):
        """ vから下向きに辿ってすべての葉を列挙する"""
        current_children = [k for k, v in self.adjacency_dict.items() if v_parent in v]
        # 子がなければ戻る
        if current_children == []:
            return children
        # 子があれば今までの子供リストに加えて，その子供も調べる
        children.extend(current_children)
        for child in current_children:
            children = self.find_children(child, children)
            return children


# Graph初期化
g = Graph(N=N, directed=True)

for _ in range(Q):
    query = list(map(int, input().split()))
    # print(query)
    if query[0] == 0:
        g.add_edge(query[1], query[2])
        # print(f'parent : {g.parent}')
        # g.print_graph()
    elif query[0] == 1:
        res = g.has_link_fast(query[1], query[2])
        print('Yes') if res else print('No')

# g.print_graph()
