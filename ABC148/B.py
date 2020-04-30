# -*- coding: utf-8 -*-
# B

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())
S, T = list(input().split())
res = []
for i in range(N):
    res.append(S[i])
    res.append(T[i])
print(''.join(res))
