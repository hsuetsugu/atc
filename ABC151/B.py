# -*- coding: utf-8 -*-
# B

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

res = M * N - sum(A)
if res>K:
    print('-1')
else:
    print(max(0, res))


