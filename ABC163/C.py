# -*- coding: utf-8 -*-
# C

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)
import collections

N = int(input())
A = map(int, input().split())

c = collections.Counter(A)

# print(c)
for i in range(1,N+1):
    print(c[i])