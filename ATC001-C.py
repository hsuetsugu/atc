# -*- coding: utf-8 -*-
# C - FFT
# https://atcoder.jp/contests/atc001/tasks/fft_c
'''
4
1 1
2 2
3 4
4 8
'''

N = int(input())
a = [0] * 2 * N
b = [0] * 2 * N

for i in range(N):
    a[i], b[i] = map(int, input().split())

for k in range(1, 2*N+1):
    sum_ = 0
    if k == 1:
        print(sum_)
        continue
    for idx_k in range(1, N+1):
        sum_ = sum_ + a[idx_k - 1] * b[k - idx_k - 1]
    print(sum_)