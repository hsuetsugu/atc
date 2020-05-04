# -*- coding: utf-8 -*-
# C

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

from collections import Counter


N = int(input())
S = []
for i in range(N):
    S.append(input())

print(len(list(Counter(S))))

