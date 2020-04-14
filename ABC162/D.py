# -*- coding: utf-8 -*-
# D

import sys
# 再起回数上限変更
# sys.setrecursionlimit(1000000)
from bisect import bisect_left

N = int(input())
S = input()
R = []
G = []
B = []

cnt_r, cnt_g, cnt_b = 0, 0, 0
for idx, s in enumerate(S):
    if s == 'R':
        R.append(idx+1)
        cnt_r += 1
    if s == 'G':
        G.append(idx+1)
        cnt_g += 1
    if s == 'B':
        B.append(idx+1)
        cnt_b += 1
# print(R, G, B)

if (cnt_r > 0) and (cnt_g > 0) and (cnt_b > 0):
    pass
else:
    print(0)
    sys.exit()


ans = cnt_r * cnt_g * cnt_b
for i in range(N):
    for j in range(1, N):
        if i + j * 2 >= N:
            continue
        if len(set([S[i], S[i + j], S[i + 2 * j]])) == 3:
            ans -= 1
print(ans)


'''
R0, G0, B0 = R, G, B

sum = 0

for i in range(6):
    if i == 0:
        R, G, B, temp = R0, G0, B0, 'B'
    elif i == 1:
        R, G, B, temp = R0, B0, G0, 'G'
    elif i == 2:
        R, G, B, temp = B0, R0, G0, 'G'
    elif i == 3:
        R, G, B, temp = B0, G0, R0, 'R'
    elif i == 4:
        R, G, B, temp = G0, R0, B0, 'B'
    elif i == 5:
        R, G, B, temp = G0, B0, R0, 'R'

    for s in R:
        if s > G[-1]:
            break
        idx1 = bisect_left(G, s)
        for g in G[idx1:]:
            if g > B[-1]:
                break
            idx2 = bisect_left(B, g)
            sum += len(B[idx2:])
            if 2 * g - s <= N:
                if S[2 * g - s - 1] == temp:
                    sum -= 1

print(sum)

'''
