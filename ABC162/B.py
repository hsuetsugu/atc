# -*- coding: utf-8 -*-
# B

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())
ans = 0
for n in range(N+1):
    if (not n % 3 == 0) and (not n % 5 == 0):
        ans += n

print(ans)
