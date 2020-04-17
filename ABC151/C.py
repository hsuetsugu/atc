# -*- coding: utf-8 -*-
# C

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N, M = map(int, input().split())

data = {}

ps = [0] * N
num_ac = 0
num_wa = 0

for i in range(M):
    p, S = input().split()
    p = int(p) - 1

    if ps[p] == 0:
        ps[p] = 1
        data[p] = {'AC':0, 'WA':0}

    if S == 'AC' and data[p]['AC'] == 0:
        data[p]['AC'] += 1
        num_ac += 1
        num_wa += data[p]['WA']

    if S == 'WA' and data[p]['AC'] == 0:
        data[p][S] += 1

print(num_ac, num_wa)


