# -*- coding: utf-8 -*-
# F
# queueの使い方、累積ダメージの更新の仕方がポイント
# 参考：https://atcoder.jp/contests/abc153/submissions/9750027

'''
3 3 2
1 2
5 4
9 2
'''

from collections import deque

N, D, A = map(int, input().split())
a = sorted(list(map(int, input().split())) for _ in range(N))
D *= 2

bomb_queue = deque()
bomb_dmg = 0
ans = 0

for x, h in a:
    # 過去の爆弾が有効でない座標に達していれば、その爆弾を捨て、累積ダメージからも差し引く
    while bomb_queue and bomb_queue[0][0] < x:
        # deque.popleft : 左側から要素を削除し、値を返す
        bomb_dmg -= bomb_queue.popleft()[1]

    # これまでの累積ダメージを差し引く
    h -= bomb_dmg
    if h > 0:
        # このモンスターを倒すのに必要な回数
        cnt = (h + A - 1) // A
        ans += cnt
        # x + Dまでダメージが与えられる
        # deque.append : 右側に付け加える
        bomb_queue.append((x + D, cnt * A))
        bomb_dmg += cnt * A

print(ans)