# -*- coding: utf-8 -*-
# D

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())

d = {}
col_self = [0] * N

for i in range(N):
    d[i] = {}

cond = []
for i in range(N-1):
    cond.append(list(map(int, input().split())))
    a, b = cond[i][0]-1, cond[i][1]-1
    d[a][b] = {'cond':i, 'color':0}

# print(cond)
# print(d)

colors = []
result = [0] * N

for i in range(N):
    num = len(d[i])
    if col_self[i] > 0:
        num += 1

    if num > len(colors):
        colors = list(range(1, num+1))

    idx = 0
    for node in d[i]:
        if colors[idx] == col_self[i]:
            idx += 1
        d[i][node]['color'] = colors[idx]
        col_self[node] = colors[idx]
        result[d[i][node]['cond']] = colors[idx]
        idx += 1

print(len(colors))

for i in range(N-1):
    print(result[i])

