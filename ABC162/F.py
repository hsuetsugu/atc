# -*- coding: utf-8 -*-
# F
# DPで解く
# dp[i][j][k] : i番目まででj個選び、直前を選んだものの合計の最大値

# ToDo: O(N)のはずなんだけどTLEになってしまう・・・

import math

N = int(input())
num = math.floor(N/2)

A = list(map(int, input().split()))

# iまででj個を選び、状態がk（i番目を選んでいる（もしくはいない））の場合の最大値
# j : [(i-1)/2] -1, 0, 1

dp = [[[- float('inf')] * 2 for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(1, N+1):
    min_j = math.floor((i-1)/2) - 1
    # print(i, min_j)

    for j in range(3):
        # k = 1なら次は必ず選ばない（その場合jは変わらない）
        dp[i][min_j + j][0] = max(dp[i][min_j + j][0], dp[i-1][min_j + j][1])
        # k = 0なら選んでも選ばなくてもいい
        dp[i][min_j + j][0] = max(dp[i][min_j + j][0], dp[i-1][min_j + j][0])
        dp[i][min_j + j + 1][1] = max(dp[i][min_j + j + 1][1], dp[i-1][min_j + j][0] + A[i-1])


'''
# print(dp)
for i in range(1, N+1):
    min_j = math.floor((i-1)/2)
    print(i, min_j, dp[i][min_j-1:min_j + 2])
'''

print(max(dp[N][num][0], dp[N][num][1]))
