# -*- coding: utf-8 -*-
# F (WIP)

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

r1, c1, r2, c2 = map(int, input().split())
DIVISOR = 10**9 + 7

'''
1 1 2 2
'''


def comb(n, r):
    # nCi mod m (i=0からnまでを全て求める）
    res1 = [1] * (r+1)
    res2 = [1] * (r+1)

    for i in range(1, r + 1):
        # 分子
        res1[i] = (res1[i-1] * (n-i+1)) % DIVISOR
        # 分母
        # res2[i] = (res2[i-1] * i) % DIVISOR
        # res2[i] = power_mod(res2[i], DIVISOR - 2, DIVISOR)
        res2[i] = power_mod((res2[i-1] * i), DIVISOR - 2, DIVISOR)

    res = [(r1 * r2) % DIVISOR for r1, r2 in zip(res1, res2)]

    return res


def power_mod(n, k, m):
    if k == 0:
        return 1
    elif k % 2 == 1:
        return power_mod(n, k-1, m) * (n % m) % m
    elif k % 2 == 0:
        temp = power_mod(n, k/2, m)
        return (temp % m) * (temp % m) % m


# r1+c1 C r1
ans0 = comb(r1+c1, r1)[-1]
# print(ans0)

rs = r2-r1
cs = c2-c1

dp = [[0] * (cs+1) for _ in range(rs+1)]
dp[0][0] = ans0


for c in range(1, cs+1):
    dp[0][c] = (dp[0][c-1] * (r1 + c1 + c) / (c1 + c)) % DIVISOR
    # dp[0][c] = dp[0][c-1] * ((r1 + c1 + c) % DIVISOR) / (c1 + c)
    # dp[0][c] = dp[0][c-1] * ((r1 + c1 + c) % DIVISOR) * power_mod(c1 + c, DIVISOR - 2, DIVISOR)

for r in range(1, rs+1):
    dp[r][0] = (dp[r - 1][0] * (r1 + c1 + r) / (r1 + r)) % DIVISOR
    # dp[r][0] = dp[r - 1][0] * ((r1 + c1 + r) % DIVISOR) / (r1 + r)
    # dp[r][0] = dp[r - 1][0] * ((r1 + c1 + r) % DIVISOR) * power_mod(r1 + r, DIVISOR - 2, DIVISOR)
    for c in range(1, cs+1):
        dp[r][c] = (dp[r][c-1] * (r1 + c1 + r + c) / (c1 + c)) % DIVISOR
        # dp[r][c] = dp[r][c-1] * ((r1 + c1 + r + c) % DIVISOR) * power_mod(c1 + c, DIVISOR - 2, DIVISOR)
        # print(r, c)

# print(dp)
print(int(sum([sum(i) % DIVISOR for i in dp]) % DIVISOR))
