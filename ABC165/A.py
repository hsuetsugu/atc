# -*- coding: utf-8 -*-
# A

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

K=int(input())
A, B = map(int, input().split())


for i in range(A, B+1):
    if i % K == 0:
        print('OK')
        sys.exit()

print('NG')
