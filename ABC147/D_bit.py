# -*- coding: utf-8 -*-
# D : ビット演算

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())
a = list(map(int, input().split()))

max_len = len(bin(max(a))[2:])
l = [0] * max_len

ans = 0
mod = 10**9 + 7

for i in range(max_len):
    for x in a:
        l[i] += x >> i & 1
    ans += pow(2, i, mod) * l[i] * (N-l[i])

print(ans % mod)
