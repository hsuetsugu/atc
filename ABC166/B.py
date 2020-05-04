# -*- coding: utf-8 -*-
# B

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, K = map(int, input().split())

ans = []
for i in range(K):
    d = int(input())
    a = list(map(int, input().split()))
    ans = list(set(ans) | set(a))

print(N - len(list(ans)))

