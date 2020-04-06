# -*- coding: utf-8 -*-
# Vacation

'''
3
10 40 70
20 50 80
30 60 90
'''

N = int(input())

dp = [[None] * 3 for _ in range(N)]
dp[0] = list(map(int, input().split()))
# print(dp)

for i in range(1, N):
    data = list(map(int, input().split()))
    # print(data)

    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + data[0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + data[1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + data[2]

# print(dp)
print(max(dp[N-1]))