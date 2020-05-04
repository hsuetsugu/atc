# -*- coding: utf-8 -*-
# A

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

S, W = map(int, input().split())

if W >= S:
    print('unsafe')
else:
    print('safe')