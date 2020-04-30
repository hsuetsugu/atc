# -*- coding: utf-8 -*-
# A

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

A = int(input())
B = int(input())

print(list(set([1,2,3]) - set([A, B]))[0])

