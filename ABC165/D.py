# -*- coding: utf-8 -*-
# D

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)
import math


A, B, N = map(int, input().split())

x = min(N, B-1)

print(math.floor(A*x/B))
