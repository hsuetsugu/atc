# -*- coding: utf-8 -*-
# B

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())
S = list(input())

for s in S:
    temp = ord(s)+N
    if temp > ord('Z'):
        temp = ord('A') + temp - ord('Z') -1
    print(chr(temp), sep="", end="")
print()
