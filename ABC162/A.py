# -*- coding: utf-8 -*-
# A

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

S = input()
for s in S:
    if s == '7':
        print('Yes')
        sys.exit()
print('No')
