# -*- coding: utf-8 -*-
# E-LCS: Longest Common Subsequence


'''
axyb
abyxb
'''

import sys

sys.setrecursionlimit(4000)
S = input()
T = input()

lcs = [[0] * (len(T) + 1) for i in range(len(S) + 1)]

for i in range(1, len(S) + 1):
    for j in range(1, len(T) + 1):
        if S[i - 1] == T[j - 1]:
            x = 1
        else:
            x = 0
        lcs[i][j] = max(lcs[i - 1][j - 1] + x, lcs[i - 1][j], lcs[i][j - 1])

# print(lcs)


def print_lcs (S, T, lcs, i, j):
    global ans
    if (i == 0 or j == 0):
        return
    if (S[i - 1] == T[j - 1]):
        print_lcs(S, T, lcs, i - 1, j - 1)
        ans.append(S[i - 1])
    else:
        if lcs[i-1][j] >= lcs[i][j-1]:
            print_lcs(S, T, lcs, i - 1, j)
        else:
            print_lcs(S, T, lcs, i, j - 1)


ans = []
print_lcs(S, T, lcs, len(S), len(T))
print("".join(ans))
