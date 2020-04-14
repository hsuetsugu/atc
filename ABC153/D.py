# -*- coding: utf-8 -*-
# D

H = int(input())


def iterated_power(z: int, n: int, mod=None) -> int:
    """ 繰り返し二乗法でn**kを求める（再帰処理は使わない）
    >>> p = Prime()
    >>> p.iterated_power(3, 10)
    59049
    >>> p.iterated_power(3, 10, 10)
    9
    """
    beta = bin(n)[2:]

    Z, q, t = z, 0, len(beta)
    while beta[t - q - 1] == '0':
        Z = Z * Z
        if mod is not None:
            Z = Z % mod
        q += 1
    result = Z

    for k in range(q + 1, t):
        Z = Z * Z
        if mod is not None:
            Z = Z % mod
        if beta[t - k - 1] == '1':
            result = result * Z
            if mod is not None:
                result = result % mod

    if mod is not None:
        result = result % mod

    return result


ans = iterated_power(2, H.bit_length()) - 1
print(ans)

'''
while True:
    H = int(H / 2)
    cnt += 1
    ans *= 2
    if H ==1:
        break
cnt += 1
ans *= 2

print(ans-1)

'''


'''
def calc(num):
    global dp

    if num == 1:
        return 1
    if dp[num] > 0:
        return dp[num]
    val = math.floor(num/2)
    res = calc(val) * 2 + 1
    dp[num] = res

    return res

ans = calc(H)
print(ans)
'''


