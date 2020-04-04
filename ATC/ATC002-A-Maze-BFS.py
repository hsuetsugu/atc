# -*- coding: utf-8 -*-
# A - 幅優先探索
# https://atcoder.jp/contests/atc002/tasks/abc007_3
"""
まず、盤面のサイズと、迷路のスタート地点とゴール地点の座標が与えられる。
次に、それぞれのマスが通行可能な空きマス(.)か通行不可能な壁マス(#)かという情報を持った盤面が与えられる。盤面は壁マスで囲まれている。
スタート地点とゴール地点は必ず空きマスであり、スタート地点からゴール地点へは、空きマスを辿って必ずたどり着ける。
具体的には、入出力例を参考にすると良い。
"""

'''
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
'''

import queue


class Bfs(object):
    def __init__(self, n_row, n_col, start, goal, data):
        self.n_row = n_row
        self.n_col = n_col
        self.start_r, self.start_c = start
        self.goal_r, self.goal_c = goal
        self.data = data

        self.found = False

        self.score = [[0] * n_col for _ in range(n_row)]
        self.visited = [[False] * n_col for _ in range(n_row)]
        self.wait_queue = queue.Queue()

        # スタートの場所をキューに入れる
        self.wait_queue.put(start)
        self.visited[self.start_r][self.start_c] = True

    def run(self):
        while not self.wait_queue.empty():
            # print(self.wait_queue.queue)
            next_node = self.wait_queue.get()
            # print(next_node)
            self.work(next_node)
            # goalまでつけば終わり
            if self.found:
                return self.score[self.goal_r][self.goal_c]

    def work(self, node):
        # goalであれば
        r, c = node
        if node == (self.goal_r, self.goal_c):
            self.found = True
            return

        self._add(r + 1, c, self.score[r][c])
        self._add(r - 1, c, self.score[r][c])
        self._add(r, c + 1, self.score[r][c])
        self._add(r, c - 1, self.score[r][c])

    def _add(self, row, col, score):
        # 条件を満たす場合はqueueに追加する
        # 1. 未訪問
        # 2. 通れる

        if (not self.visited[row][col]) and (self.data[row][col] == '.'):
            # print(f'push : {row}, {col}')
            self.score[row][col] = score + 1
            self.visited[row][col] = True
            self.wait_queue.put((row, col))
        else:
            return False


n_row, n_col = map(int, input().split())
start_r, start_c = map(int, input().split())
goal_r, goal_c = map(int, input().split())

data = [[None] * n_col for _ in range(n_row)]
# data = [None] * n_row
for i in range(n_row):
    temp = input()
    for c in range(n_col):
        data[i][c] = temp[c]

bfs = Bfs(n_row, n_col, (start_r - 1, start_c - 1), (goal_r - 1, goal_c - 1), data)

score = bfs.run()
print(score)
