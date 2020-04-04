# -*- coding: utf-8 -*-
# 尺取法の例

'''
7 6
4
3
1
1
2
10
2
'''

import sys

N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

current_row = 0
current_best = 0
c = 1

for col in range(N):
    if S[col] == 0:
        print(N)
        sys.exit()

    c *= S[col]

    while True:
        if current_row > col:
            break
        if c <= K:
            break
        else:
            c /= S[current_row]
            current_row += 1

    if col - current_row + 1 > current_best:
        current_best = col - current_row + 1

print(current_best)

