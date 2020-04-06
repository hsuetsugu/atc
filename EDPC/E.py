# -*- coding: utf-8 -*-
# D-Knapsack2

# DPはnumpy使わずにpypy3で提出する(pythonより3倍くらい早い）
# Dとの違い：Wが大きく、vは小さい

'''
3 8
3 30
4 50
5 60
'''

N, W = map(int, input().split())
w, v = [None] * N, [None] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())

v_max = (max(v)+1) * N
dp = [[None] * v_max for _ in range(N+1)]
dp[0] = [float('inf')] * v_max
dp[0][0] = 0

for i in range(N):
    for j in range(v_max):
        if j > v[i]:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i])
        else:
            dp[i + 1][j] = min(dp[i][j], w[i])

# print(dp)
print(len([i for i in dp[N] if i <= W]) - 1)
