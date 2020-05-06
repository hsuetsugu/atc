# -*- coding: utf-8 -*-
# E: bit演算を活用して効率的に計算しないとTLEになる

# dp[[i][j]で、(i,j)で可能な偏りを格納していく
# 1, 2, 3が可能な場合は"00000111"と表現する
# n + m を可能にするには、n << mにすれば良い
# (1, 2, 3)に2を足して(3, 4, 5)を可能にするなら、
# "00011100"としたいので、n << mで良い
# (3, 4, 5)に±4する場合；
# 求めたいのは(7, 8, 9) | (-1, 0, 1)
# −１を1としたい

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

H, W = map(int, input().split())
a = []
x = []

for i in range(H):
    a.append(list(map(int, input().split())))
for i in range(H):
    x.append(list(map(int, input().split())))
    for j in range(W):
        x[i][j] = abs(x[i][j] - a[i][j])


dp = [[0 for _ in range(W)] for _ in range(H)]
dp[0][0] = 1 << x[0][0]
# print(bin(dp[0][0]))


def reverse(d, x):
    res = 0
    for i in range(x+1):
        res <<= 1
        if (1<<i) & d:
            res |= 1
    return res


for i in range(H):
    for j in range(W):
        g = x[i][j]
        if i > 0:
            d1 = dp[i-1][j]
            dp[i][j] |= d1 << g | d1 >> g | reverse(d1, g)
        if j > 0:
            d2 = dp[i][j-1]
            dp[i][j] |= d2 << g | d2 >> g | reverse(d2, g)


a = dp[H-1][W-1]
for i in range(a.bit_length()):
    if a >> i & 1 == 1:
        print(i)
        sys.exit()
