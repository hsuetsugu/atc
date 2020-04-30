# -*- coding: utf-8 -*-
# D

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())
a = list(map(int, input().split()))

num = 1
ans = 0
for i in range(N):
    if a[i] == num:
       num += 1
    else:
        ans += 1
if num == 1:
    print(-1)
else:
    print(ans)