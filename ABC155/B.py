# -*- coding: utf-8 -*-
# B

import sys

# 再起回数上限変更
sys.setrecursionlimit(1000000)

N = int(input())
a = list(map(int, input().split()))

for i in a:
    if i % 2 == 0:
        if (i % 3 == 0) or (i % 5 == 0):
            continue
        else:
            print('DENIED')
            sys.exit()

print('APPROVED')
