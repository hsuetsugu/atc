# -*- coding: utf-8 -*-
# A

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

S, T = input().split()
A, B = map(int, input().split())
U = input()

if U == S:
    print(A-1, B)
else:
    print(A, B -1)