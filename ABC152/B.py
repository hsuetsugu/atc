# -*- coding: utf-8 -*-
# B

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)


a, b = map(int, input().split())

s1 = "".join([str(a)] * b)
s2 = "".join([str(b)] * a)

print(min(s1, s2))
