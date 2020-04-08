# -*- coding: utf-8 -*-
# M- Candy

# 子供iまででkを作った場合の組み合わせの数をdp[i][k]とすると、
# dp[i][k] = sum_a(in a[i]) dp[i-1][k-a] と計算できるが、
# N, Kに加えて各a_iについての3重ループになってしまうため工夫が必要（naive実装：TLE）
# DPテーブルの各行について、累積を計算しおけば、
# dp[i-1][s]からdp[i-1][t]を計算するのにループにせずに、累積した値の差をとることで計算できる

'''
3 4
1 2 3
'''

from itertools import accumulate

N, K = map(int, input().split())
A = [int(i) for i in input().split()]

dp = [[0] * (K + 1) for i in range(N + 1)]
dp[0][0] = 1
DIVISOR = 10**9 + 7

dp_cum = [[0] * (K + 2) for i in range(N + 1)]
dp_cum[0] = [0] + [1]*(K+1)

for i in range(1, N + 1):
    dp[i][0] = 1

    # print(i, A[i - 1])
    for k in range(1, K + 1):
        # naive実装
        # res = 0
        # for a in range(0, A[i-1] + 1):
        #     if k - a >= 0:
        #         res += dp[i-1][k-a]
        # dp[i][k] = res % DIVISOR

        dp[i][k] = dp_cum[i-1][k+1] - dp_cum[i-1][max(0, k-A[i-1])]

    dp_cum[i] = [0] + list(accumulate(dp[i]))
    dp_cum[i] = [i % DIVISOR for i in dp_cum[i]]

# print(dp)
# print(dp_cum)

print(dp[N][K] % DIVISOR)

