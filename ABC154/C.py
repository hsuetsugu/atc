# -*- coding: utf-8 -*-
# C

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

import collections
N = int(input())
A = list(map(int, input().split()))

s = collections.Counter(A)
if len(s.keys()) == N:
    print('YES')
else:
    print('NO')
