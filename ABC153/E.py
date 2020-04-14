# -*- coding: utf-8 -*-
# E

# 実質的には重複ありナップサック問題
# dp[i][j]をi番目までのパターンで体力jのモンスターを倒すのに必要な魔力の最小値とする
# 重複ありの場合、m個を全て試しているとO(NHH)かかってしまうため、
# dp[i][j] = max(dp[i][j], dp[i][j - A[i]]という形で前の結果を再利用することでO(NH)で済ませる


H, N = map(int, input().split())

data = []

for i in range(N):
    a, b = map(int, input().split())
    data.append({'a': a, 'b': b})

dp = [[float('inf')] * (H+1) for _ in range(N)]


for i in range(N):
    dp[i][0] = 0

for j in range(H+1):
    dp[0][j] = -(-j // data[0]['a']) * data[0]['b']

for i in range(1, N):
    power = data[i]['a']
    magic = data[i]['b']

    for j in range(H+1):
        dp[i][j] = dp[i - 1][j]
        if j <= power:
            dp[i][j] = min(dp[i][j], dp[i-1][max(0, j - power)] + magic)
        else:
            dp[i][j] = min(dp[i][j], dp[i][j - power] + magic)

# print(dp)
print(dp[N-1][H])
