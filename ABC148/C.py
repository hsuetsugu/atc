# -*- coding: utf-8 -*-
# C

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

import math
a, b = map(int, input().split())

print(int(a * b / math.gcd(a, b)))
