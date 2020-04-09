# -*- coding: utf-8 -*-
# E (WIP) 


DIVISOR = 10**9 + 7
n, k = map(int, input().split())


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
    # res = [(r1 / r2) for r1, r2 in zip(res1, res2)]

    return res


def power_mod(n, k, m):
    if k == 0:
        return 1
    elif k % 2 == 1:
        return power_mod(n, k-1, m) * (n % m) % m
    elif k % 2 == 0:
        temp = power_mod(n, k/2, m)
        return (temp % m) * (temp % m) % m


res1 = comb(n, k)
res2 = comb(n-1, k)

result = 0
for i in range(k+1):
    result += (res1[i] * res2[i]) % DIVISOR

print(result)
