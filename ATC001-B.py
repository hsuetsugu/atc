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
N, Q = map(int, input().split())
# print(sys.getrecursionlimit())
sys.setrecursionlimit(20000)


class Graph(object):
    def __init__(self, N, directed=False):
        """ ノードのつながりを辞書型で表現する """
        self.adjacency_dict = {}
        self.directed=directed
        self.parent = [None] * N

        for i in range(N):
            self.add_vertex(i)
            # self.parent[i] = i
        self.rank = [0] * N

    def add_vertex(self, v):
        """ ノードを追加する """
        self.adjacency_dict[v] = []

    def add_edge(self, v1, v2, reconnect=False):
        """ ノード同士をつなぐ。"""
        if v1 == v2:
            return

        # 無向グラフの場合は双方向。もし有向グラフなら片側のみ。
        if reconnect:
            # 階層を小さくする場合はrootノードに直接接続する
            # v1にひもづく全ての子供をv2の親につける
            parent_v2 = self.find_parent(v2, None)
            # print(f'found parent: {v2}, {parent_v2}')
            children_v1 = self.find_children(v1, [v1])
            # print(f'found children: {v1}, {children_v1}')

            for v in children_v1:
                # 全ての接続を切る
                self.remove_edge_all(v)
                # if not self._has_direct_vertex(v, parent_v2):
                self.adjacency_dict[v].append(parent_v2)
        else:
            # if not self._has_direct_vertex(v1, v2):
            #     self.adjacency_dict[v1].append(v2)
            # v1, v2の親同士をつなげる
            p2 = self.find_parent(v2)
            p1 = self.find_parent(v1)
            print((v1, p1), (v2, p2))

            self.parent[v1] = p1
            self.parent[v2] = p2

            if p1 != p2:
                if self.rank[p1] < self.rank[p2]:
                    self.adjacency_dict[p1].append(p2)
                    self.rank[p1] += 1
                else:
                    self.adjacency_dict[p2].append(p1)
                    self.rank[p2] += 1

        if not self.directed:
            if not self._has_direct_vertex(v2, v1):
                self.adjacency_dict[v2].append(v1)

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

    def find_parent(self, v1, parent=None):
        """ vから上向きに辿って根を調べる """
        if self.adjacency_dict[v1] == []:
            return v1

        if self.parent[v1] is not None:
            # parentが格納されていればそれを用いる
            parent = self.find_parent(self.parent[v1], parent)
            return parent

        # なければ辿っていく
        for v in self.adjacency_dict[v1]:
            parent = self.find_parent(v, parent)
        return parent

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

    def remove_edge_all(self, v):
        """ あるノード同士のエッジを全て削除する。"""
        while self.adjacency_dict[v] != []:
            adjacent_vertex = self.adjacency_dict[v][-1]
            self.remove_edge(v, adjacent_vertex, both=False)

    def remove_edge(self, v1, v2, both):
        """ ノード同士のつながりを削除する。"""
        self.adjacency_dict[v1].remove(v2)
        if both:
            self.adjacency_dict[v2].remove(v1)

    def remove_vertex(self, v):
        """ ノードを削除する。"""
        while self.adjacency_dict[v] != []:
            adjacent_vertex = self.adjacency_dict[v][-1]
            self.remove_edge(v, adjacent_vertex)
        del self.adjacency_dict[v]

    def print_graph(self):
        print(self.adjacency_dict)

    def _has_direct_vertex(self, v1, v2):
        """ 直接連結しているかを確認する """
        if v2 in self.adjacency_dict[v1]:
            return True
        else:
            return False

    def has_link_naive(self, v1, v2):
        if v1 == v2:
            return True
        else:
            searched = [False] * len(self.adjacency_dict)
            found = self._has_link(v1, v2, found=False, searched=searched)
            return found

    def _has_link(self, v1: int, v2: int, found: bool, searched: list) -> bool:
        """  v1とv2が連結しているかを判定する """
        searched[v1] = True
        # print(v1, v2, found, searched)

        # 見つかっていれば終わり
        if found:
            return found

        # 直接連結されていれば終わり
        if self._has_direct_vertex(v1, v2):
            return True

        # 直接されていなければ連結ノードをさらに調べていく
        # 自身とつながっている全てのノードについて調べる
        for v in self.adjacency_dict[v1]:
            if searched[v]:
                continue
            found = self._has_link(v, v2, found, searched)
            if found:
                break
        return found


# Graph初期化
g = Graph(N=N, directed=True)

for _ in range(Q):
    query = list(map(int, input().split()))
    print(query)
    if query[0] == 0:
        # 連結クエリ
        g.add_edge(query[1], query[2], reconnect=False)
        print(g.parent)
        g.print_graph()
    elif query[0] == 1:
        # 判定クエリ
        # res = g.has_link_naive(query[1], query[2])
        res = g.has_link_fast(query[1], query[2])
        print('Yes') if res else print('No')


# g.print_graph()
