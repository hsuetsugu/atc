# -*- coding: utf-8 -*-
# Friend Suggestion
# https://atcoder.jp/contests/abc157/tasks/abc157_d
# 連結しているうち、現在友達関係でもブロック関係でもない人数を調べる
# つまり、友達候補 = [連携成分の数] - [友達の数] - [ブロック数]

'''
4 4 1
2 1
1 3
3 2
3 4
4 1
'''

from UnionFind import UnionFind

N, M, K = map(int, input().split())


class UnionFindFriend(UnionFind):
    def __init__(self, n):
        super(UnionFindFriend, self).__init__(n)
        self.friends = {}
        self.blocks = {}

        for i in range(n):
            self.friends[i] = []
            self.blocks[i] = []

    def add_friends(self, v1, v2):
        self.friends[v1].append(v2)
        self.friends[v2].append(v1)

    def add_blocks(self, v1, v2):
        self.blocks[v1].append(v2)
        self.blocks[v2].append(v1)


def get_next():
    c1, c2 = map(int, input().split())
    c1, c2 = c1 - 1, c2 -1
    return c1, c2


uf = UnionFindFriend(N)

for i in range(M):
    c1, c2 = get_next()
    uf.unite(c1, c2)
    uf.add_friends(c1, c2)

for i in range(K):
    c1, c2 = get_next()
    uf.add_blocks(c1, c2)

# 全ての要素のroot（つまり自分がどのグループに所属するか）を格納
roots = [uf.root(i) for i in range(N)]
print(roots)
res = {}

# rootsからグループのリストを取得し、一つずつ処理する
for root in list(set(roots)):
    idxes = [idx for idx, element in enumerate(roots) if element == root]
    len_idxes = len(idxes)
    print(root, idxes)

    for idx in idxes:
        # 友達候補 = [連携成分の数 -1] - [友達の数] - [連結成分におけるブロック数]
        result = len_idxes - 1 - len(uf.friends[idx]) - len(set(uf.blocks[idx]) & set(idxes))
        res[idx] = result

for i in range(N):
    print(res[i], end=' ')