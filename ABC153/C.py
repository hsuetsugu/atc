# -*- coding: utf-8 -*-
# C

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, K = map(int, input().split())
H = list(map(int, input().split()))

H.sort()
H = H[::-1]


if len(H) <= K:
    print(0)
    sys.exit()

H = H[K:]
print(sum(H))

