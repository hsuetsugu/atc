# -*- coding: utf-8 -*-
# I-Coin
# i枚中j枚が表である確率を(i-1, j), (i-1, j-1）を使って求める

'''
5
0.42 0.01 0.42 0.99 0.42
'''


N = int(input())
p = list(map(float, input().split()))

dp = [[0] * (N+1) for i in range(N+1)]

# i=0: 0枚中j(>0)枚が表の確率 = 0
dp[0][0] = 1

# j=0: i(>0)枚中0枚が表の確率 = 全て裏の確率
for i in range(1, N + 1):
    dp[i][0] = dp[i - 1][0] * (1 - p[i - 1])

# 漸化式で更新
for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i-1][j-1] * p[i - 1] + dp[i-1][j] * (1 - p[i - 1])

# print(dp)
print(sum(dp[N][int((N+1)/2):]))

