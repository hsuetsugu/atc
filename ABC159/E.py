# -*- coding: utf-8 -*-

# H <= 10であるため2^(H-1)を全探索し、
# W <= 1000 については貪欲に左から探索していけば良い

'''
4 10 4
1110010010
1000101110
0011101001
1101000111
'''

import numpy as np


def main():
    H, W, K = map(int, input().split())

    data = np.array([[None] * W for _ in range(H)])

    for i in range(H):
        temp = input()
        for j in range(W):
            data[i, j] = int(temp[j])

    current_best = np.inf

    # Hに関する全ての場合を試す
    for cnt in range(2 ** (H-1)):
        # bitで1の場所が切れ目とする
        option_h = np.array([int(s) for s in list(bin(cnt))[2:][::-1]])
        kireme = np.where(option_h == 1)[0]

        # 各グループについて1の数を列ごとに集計する
        li = 0
        g = np.array([[None] * W for _ in range(len(kireme) + 1)])
        if len(kireme) == 0:
            g[0] = data[li:, :].sum(axis=0)
        else:
            for idx, j in enumerate(kireme):
                g[idx] = data[li:j+1, :].sum(axis=0)
                li = j + 1
            g[-1] = data[li:, :].sum(axis=0)

        # 左から順に足していく
        score = len(kireme)
        if score > current_best:
            # すでにこの時点で回数かかっていれば探索打ち切り
            continue

        res = np.zeros(len(kireme) + 1)
        for col in range(W):
            res = res + g[:, col]
            # どこか1つのグループでもKを超えてしまったらその左で切る
            if (res > K).any():
                score += 1
                # 最小を求めたいので、それまでの結果と同じ値になってしまったら終了
                if score >= current_best:
                    break
                res = g[:, col]
                # 現在の列だけで条件を満たせないのであれば不可能なので終了
                if (res > K).any():
                    score = np.inf
                    break
        # スコアの更新
        # print(cnt, score)
        if score < current_best:
            current_best = score

    print(current_best)


if __name__ == '__main__':
    main()
