# -*- coding: utf-8 -*-
# C

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

X = int(input())


def is_prime(n: int) -> bool:
    if n == 1:
        return False
    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
        if i * i > n:
            return True

while True:
    if is_prime(X):
        print(X)
        sys.exit()
    X += 1