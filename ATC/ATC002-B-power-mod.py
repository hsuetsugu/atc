# -*- coding: utf-8 -*-
# B - 繰り返し最小二乗法

'''
123456789 234567894 6574837563712
'''
import time


def power_mod_naive(n, k, m):
    return n**k % m


def power_mod(n, k, m):
    if k == 0:
        return 1
    elif k % 2 == 1:
        return power_mod(n, k-1, m) * (n % m) % m
    elif k % 2 == 0:
        temp = power_mod(n, k/2, m)
        return (temp % m) * (temp % m) % m


N, M, P = map(int, input().split())

st = time.time()
print(power_mod(N, P, M))
# print(power_mod_naive(N, P, M))

print(f'time : {time.time() - st} [sec]')