# -*- coding: utf-8 -*-
# Counterを利用
# 結果変数にlistを使うとTLEだが辞書にするとOK（なぜ？値参照は計算量変わらないような・・・）


'''
20 8
1 8
4 13
8 8
3 18
5 20
19 20
2 7
4 9
'''

import numpy as np
import collections

N, Q = map(int, input().split())

cnt = {}
list_l = np.zeros(N)
list_r = np.zeros(N)

li = []
ri = []

for _ in range(Q):
    l, r = map(int, input().split())
    l ,r = l-1, r-1
    li.append(l)
    ri.append(r)

l = collections.Counter(li)
r = collections.Counter(ri)

cnt[0] = l[0]
print(int(cnt[0] % 2), end='')
for i in range(1, N):
    cnt[i] = cnt[i-1] + l[i] - r[i-1]
    print(int(cnt[i] % 2), end='')

print('')


''' naive solution
for _ in range(Q):
    l, r = map(int, input().split())
    l ,r = l-1, r-1
    for i in range(N):
        if (i >= l) and (i <= r):
            s[i] += 1

for i in range(N):
    print(int(s[i] % 2), end='')
print('')
'''
