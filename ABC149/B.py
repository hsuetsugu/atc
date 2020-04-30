# -*- coding: utf-8 -*-
# B

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

A, B, K = map(int, input().split())

print(max(0, A-K), max(B-(max(0, K-A)), 0))
