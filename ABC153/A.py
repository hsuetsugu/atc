# -*- coding: utf-8 -*-
# A

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

H, A = map(int, input().split())

if H % A == 0:
    print(int(H / A))
else:
    print((H // A)+1)