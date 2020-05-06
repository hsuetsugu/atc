# -*- coding: utf-8 -*-
# A

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

a = list(map(int, input().split()))

if sum(a) >= 22:
    print('bust')
else:
    print('win')
