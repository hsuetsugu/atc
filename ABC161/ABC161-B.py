# -*- coding: utf-8 -*-


'''

'''

import numpy as np

N, M = map(int, input().split())
a = list(map(int, input().split()))
a = np.array(a)
s = int(a.sum())
level = 1 / (4 * M)
# print(a)
# print(level)

cnt = (a >= level * s).sum()

if cnt >= M:
    print('Yes')
else:
    print('No')
