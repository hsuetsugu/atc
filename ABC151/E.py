# -*- coding: utf-8 -*-
# E

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, K = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9 + 7

A.sort()
# print(A)


def cmb(n, r):
    from operator import mul
    from functools import reduce

    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

ans = 0
num1=None
num2=None

memo = [[None]*K for _ in range(N)]

for i in range(N):
    if i >= K-1:
        if num2 is None:
            num2 = cmb(i, K-1) % mod
            memo[i][min(i - (K-1), K-1)] = num2
        else:
            num2 = num2 * (i % mod) * pow(i-K+1, mod-2, mod)
        # print(i, K-1, num2)

        if A[i] * num2 < 0:
            ans -= (-A[i] * num2) % mod
        else:
            ans += (A[i] * num2) % mod
        # print(f'+: {i}, {num}, {A[i]}')

for i in reversed(range(N)):
    if N - i - 1 >= K-1:
        if num1 is None:
            num1 = cmb(N-i-1, K-1) % mod
        else:
            if memo[N-i-1][min(N-i-1 - (K-1), K-1)] is not None:
                num1 = memo[N-i-1][min(N-i-1 - (K-1), K-1)]
            else:
                num1 = num1 * ((N-i) % mod) * pow(N-i-K+1, mod-2, mod)
        print(N-i-1, K-1, num1)

        if A[i] * num1 < 0:
            ans += (-A[i] * num1) % mod
        else:
            ans -= (A[i] * num1) % mod
        # print(f'-: {i}, {num}, {A[i]}')

print(ans % mod)
