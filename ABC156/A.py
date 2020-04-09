# -*- coding: utf-8 -*-
# A -


import sys

# 再起回数上限変更
sys.setrecursionlimit(1000000)

N, R = map(int, input().split())

if N >= 10:
    print(R)
    sys.exit()

print(R + 100 * (10 - N))
