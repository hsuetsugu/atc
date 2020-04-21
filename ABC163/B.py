# -*- coding: utf-8 -*-
# B

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)


N, M = map(int, input().split())
A = list(map(int, input().split()))

if N >= sum(A):
    print(N-sum(A))
else:
    print('-1')
