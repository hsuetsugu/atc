# -*- coding: utf-8 -*-

'''
5 3
10 30 40 50 20
'''

N, K = map(int,input().split())
h = list(map(int, input().split()))

dp = [None] * N

dp[0] = 0
dp[1] = abs(h[0] - h[1])

# for k in range(1, K):
    # dp[k] = abs(h[0] - h[k])

for i in range(2, N):
    temp = min(i, K)
    dp[i] = min([dp[i-k] + abs(h[i] - h[i-k]) for k in range(1, temp + 1)])

# print(dp)
print(dp[N-1])
