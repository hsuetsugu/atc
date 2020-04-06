# -*- coding: utf-8 -*-
# D-Knapsack

# DPはnumpy使わずにpypy3で提出する(pythonより3倍くらい早い）

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

dp = [[None] * (W+1) for _ in range(N+1)]
dp[0] = [0] * (W+1)
# print(dp)

for i in range(N):
    for j in range(W + 1):
        if j >= w[i]:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w[i]] + v[i])
        else:
            dp[i + 1][j] = dp[i][j]

# print(dp)
print(dp[N][W])
