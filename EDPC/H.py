# -*- coding: utf-8 -*-
# H-Grid
# 単純に足していくだけ

'''
5 2
..
#.
..
.#
..
'''


H, W = map(int, input().split())

data = [[None] * (W+1) for i in range(H+1)]
dp = [[0] * (W+1) for i in range(H+1)]

dp[0] = [0] * (W+1)

for i in range(H):
    temp = list(input())
    dp[i + 1][0] = 0
    for j in range(W):
        data[i + 1][j + 1] = temp[j]


for i in range(1, H + 1):
    for j in range(1, W + 1):
        if (i == 1) and (j == 1):
            dp[i][j] = 1
            continue

        if data[i][j] == '.':
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        else:
            dp[i][j] = 0

# print(dp)
print(dp[H][W] % (10**9+7))
