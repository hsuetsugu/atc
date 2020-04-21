# -*- coding: utf-8 -*-
# TSP : Traveling Salesman Problem
# bit DP（集合に対するDP）

# 0からスタートして、すべての頂点を通って戻ってくるルートの合計距離（重み）の最小値を求める
# dp[S][v] : Sを訪問済みの頂点のルートの集合として現在vにいる場合に、残り全てを通って帰ってくる重みの最小値とする
# dp[V][0]=0 :全て訪問し終わった状態
# dp[S][v] = min(dp[S U {u}][u] + d(v, u) | u not in S)
# 初期状態では0は未訪問だとする必要がある

# ノードがN個ある場合、訪問したかどうかは0/1ビットで2進数N桁で表現することができる
# 集合の数は、2**N(N=15なら32,768)

'''
5 8
0 1 3
0 3 4
1 2 5
2 3 5
2 0 4
3 4 3
4 0 7
4 1 0
'''


def Base_10_to_n(K, X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)

    if K > 0:
        out = '0' * (K - len(out)) + out
    return out


def get_unvisited(s):
    return [idx for idx, i in enumerate(list(s)[::-1]) if i == '0']


class Tsp(object):
    def __init__(self, n:int):
        self.adjacency_dict = {}
        self.n = n
        for i in range(n):
            self.add_vertex(i)
        self.dp = None

    def add_vertex(self, v: int):
        """ ノードを追加する """
        self.adjacency_dict[v] = {}

    def add_edge(self, v1: int, v2: int, w: float, undirected=False):
        """ 重み付きの辺を追加する"""
        self.adjacency_dict[v1][v2] = w
        if undirected:
            self.adjacency_dict[v2][v1] = w

    def solve(self):
        # df[S][v] 訪問済みSをした時のv（初期値は-1）
        self.dp = [[-1] * self.n for _ in range(2**self.n)]
        # Sは2進数表記で:0110110101と表現したときに1になっているものを訪問済みだとする
        # 未訪問リストは上記から0を持って来れば良い

        # 初期状態：Sを整数値で表現した場合
        self.dp[(2**self.n)-1][0] = 0
        # 求めたいのは、dp[0][0]
        res = self.calc(0, 0)

        print(self.dp)

        return res

    def calc(self, S: int, v: int):
        # 集合を2進数表記に変更
        S_base2 = Base_10_to_n(self.n, S, 2)
        # 未訪問のノードを取得
        unvisited = get_unvisited(S_base2)

        print(f'FORWARD : (S, unvisited, v, reachable) : {S_base2}, {unvisited}, {v}, {self.adjacency_dict[v].keys()}')

        # 計算済みであればreturn
        if self.dp[S][v] > 0:
            return self.dp[S][v]

        if S == (1 << self.n - 1) and v == 0:
            self.dp[S][v] = 0
            return 0

        res = float('inf')

        # vから行ける訪問済みでないノードについて
        # dp[S][v] = min(dp[S U {u}][u] + d(v, u) | u not in S)
        reachable = self.adjacency_dict[v].keys()
        candidates = list(set(reachable) & set(unvisited))
        for u in candidates:
            # print(f'S, u : {S}, {u}')
            res = min(res, self.calc(int(S+2**u), u) + self.adjacency_dict[v][u])

        print(f'RETURN({res}) : (S, unvisited, v, reachable) : {S_base2}, {unvisited}, {v}, {self.adjacency_dict[v].keys()}')
        self.dp[S][v] = res
        return res


if __name__ == '__main__':
    N, Q = map(int, input().split())
    g = Tsp(N)

    for _ in range(Q):
        v1, v2, w = map(int, input().split())
        g.add_edge(v1, v2, w)

    print(g.adjacency_dict)

    print(g.solve())
