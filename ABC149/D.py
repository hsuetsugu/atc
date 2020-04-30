# -*- coding: utf-8 -*-
# D

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())
score = [R, S, P]

# Kのあまりごとに独立して計算する
ans = 0
num = N // K + 1


def vic_sol(s):
    if s == 'r':
        return 2
    if s == 's':
        return 0
    if s == 'p':
        return 1


def ret_score(mine, i, mod, past_rsp):
    sol = vic_sol(T[i * K + mod])
    if (mine == sol) and (sol != past_rsp):
        return score[sol]
    else:
        return 0


for mod in range(K):
    dp = [[0] * 3 for _ in range(num+2)]
    ret = 0
    # 0: R, 1: S, 2: P
    for i in range(1, num+1):
        if (i-1) * K + mod >= N:
            break
        # print(i, num, (i-1) * K + mod)
        dp[i][0] = max(dp[i-1][1] + ret_score(0, i-1, mod, 1), dp[i-1][2] + ret_score(0, i-1, mod, 2))
        dp[i][1] = max(dp[i-1][0] + ret_score(1, i-1, mod, 0), dp[i-1][2] + ret_score(1, i-1, mod, 2))
        dp[i][2] = max(dp[i-1][0] + ret_score(2, i-1, mod, 0), dp[i-1][1] + ret_score(2, i-1, mod, 1))

        if mod == 0:
            dp[i][0] = max(dp[i][0], dp[i - 1][0] + ret_score(0, i - 1, mod, 0))
            dp[i][1] = max(dp[i][1], dp[i - 1][1] + ret_score(1, i - 1, mod, 1))
            dp[i][2] = max(dp[i][2], dp[i - 1][2] + ret_score(2, i - 1, mod, 2))

        ret = max(ret, dp[i][0], dp[i][1], dp[i][2])
    # print(dp)
    ans += ret

print(ans)
