# -*- coding: utf-8 -*-
# B

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

A, B, C, D = map(int, input().split())

for i in range(100):
    C -= B
    if C <= 0:
        print('Yes')
        sys.exit()
    A -= D
    if A <= 0:
        print('No')
        sys.exit()
