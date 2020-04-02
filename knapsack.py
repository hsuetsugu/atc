# -*- coding: utf-8 -*-
# knapsack problem
# DP

'''
# N, W
# weight, value
4 5
2 3
1 2
3 4
2 2
'''

N, W = map(int, input().split())
ws = [None] * N
vs = [None] * N

for i in range(N):
    w, v = map(int, input().split())
    ws[i] = w
    vs[i] = v

dp = [[0] * (W+1) for _ in range(N+1)]

# 初期化
# for j in range(W + 1):
#     dp[0][j] = 0

for i in range(N):
    for j in range(W+1):
        if j < ws[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - ws[i]] + vs[i])

print(dp)
