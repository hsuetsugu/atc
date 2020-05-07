# -*- coding: utf-8 -*-
# A

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

S = input()
for idx, s in enumerate(['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'][::-1]):
    if S == s:
        print(idx+1)

