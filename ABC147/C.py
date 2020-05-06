# -*- coding: utf-8 -*-
# C
# 全探索：ビット演算

from itertools import product

N = int(input())
A = [0] * N
x = []

for i in range(N):
    A[i] = int(input())
    d = []
    for j in range(A[i]):
        d.append(tuple(map(int, input().split())))
    x.append(d)

ans = 0

# for case in list(product([0,1], repeat=N)):
for m in range(2**N):
    # print(case)
    flg = [-1] * N
    cond = True
    for i in range(N):
        if not cond:
            continue
        if m >> i & 1 == 0:
            continue

        for a in range(A[i]):
            c, d = x[i][a]
            c = c-1

            # print(c, d)
            if m >> c & 1 != d:
                cond = False
                # print('矛盾')
    if cond:
        # ans = max(ans, sum(case))
        ans = max(ans, bin(m).count('1'))

print(ans)
