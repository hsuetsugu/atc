# -*- coding: utf-8 -*-

'''
4
10 30 40 20
'''

N = int(input())
h = list(map(int, input().split()))

dp = [None] * N

dp[0] = 0
dp[1] = abs(h[0] - h[1])

for i in range(2, N):
    dp[i] = min(dp[i-2] + abs(h[i]-h[i-2]),
                    # dp[i-2] + abs(h[i]-h[i-2]) + abs(h[i]-h[i-1])),
                dp[i-1] + abs(h[i]-h[i-1]))

print(dp[N-1])
