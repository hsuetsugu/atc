# -*- coding: utf-8 -*-
# E: Almost Everywhere Zero
# 桁DP
# dp[i][j][k] : (上から)i桁目までで、0でない数字がj個あり、
# k（N以下であることが確定なら1、確定していないなら0）のような数値の個数を表すとする

S = list(input())
K = int(input())
N = len(S)

# print(S)

# dp[i][j][k]
dp = [[[0] * 2 for _ in range(K+2)] for _ in range(N+1)]

dp[0][0][0] = 1

# 上の桁から調べていく
for i in range(1, N + 1):
    for j in range(K + 1):
        for k in range(2):
            for num in range(10):
                if num == 0:
                    inc = 0
                else:
                    inc = 1
                # N未満が確定していれば0-9の全ての遷移が可能なので加える
                if k == 1:
                    dp[i][j+inc][k] += dp[i - 1][j][k]
                else:
                    if num < int(S[i-1]):
                        # k = 1が確定
                        dp[i][j + inc][1] += dp[i - 1][j][k]
                    elif num == int(S[i-1]):
                        # k = 0のまま
                        dp[i][j + inc][0] += dp[i - 1][j][k]

# print(dp)

print(dp[N][K][0] + dp[N][K][1])