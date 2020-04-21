# -*- coding: utf-8 -*-
# E

N = int(input())
A = list(map(int, input().split()))
d = []
for idx, a in enumerate(A):
    d.append({'idx':idx, 'val':a})

d = sorted(d, key=lambda x:x['val'], reverse=True)


dp = [[-float('inf')]*(N+1) for _ in range(N+1)]
dp[0][0] = 0

# dp[0][1] = d[0]['val'] * (N - d[0]['idx'])
# dp[1][0] = d[0]['val'] * (d[0]['idx'] - 1)

ans = -float('inf')

# x + y = 1からNまで
for xy in range(1, N+1):
    # x = 0 から x+yまで
    for x in range(xy+1):
        y = xy - x
        if y > 0:
            dp[x][y] = max(dp[x][y], dp[x][y - 1] + d[xy - 1]['val'] * (N - y + 1 - d[xy - 1]['idx']))
        if x > 0:
            dp[x][y] = max(dp[x][y], dp[x - 1][y] + d[xy - 1]['val'] * (d[xy -1]['idx'] - x))

        if xy == N:
            ans = max(ans, dp[x][y])

print(dp)
print(ans)
