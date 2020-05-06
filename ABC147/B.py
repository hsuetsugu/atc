# -*- coding: utf-8 -*-
# B

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

S = input()
ans = 0
for i in range(len(S)//2):
    if S[i] != S[len(S) - i -1]:
        ans += 1

print(ans)

