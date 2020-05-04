# -*- coding: utf-8 -*-
# D

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

x = int(input())

for i in range(-200, 200):
    for j in range(-200, 200):
        if int(i ** 5 - j ** 5) == x:
            print(i, j)
            sys.exit()

