# -*- coding: utf-8 -*-
# J-Sushi
# 1,2,3の寿司が乗った寿司がN個あり、一つずつ食べて行ったときに食べ終わるまでの試行回数の期待値を求める
# 1個の皿がi, 2個の皿がj、3個の皿がkから食べ終わるまでの試行回数の期待値をdp[i][j][k]とする

# もしくはメモ化再起だとTLE...

# i, j, kの更新順序がわからなかったため、以下を参照
# https://atcoder.jp/contests/dp/submissions/4014057


'''
10
1 3 2 3 3 2 3 2 1 3
'''

import collections
import sys

# 再起回数上限変更
sys.setrecursionlimit(1000000)

N = int(input())
A = [int(i) for i in input().split()]
c = collections.Counter(A)
I, J, K = c[1], c[2], c[3]

L = I+J+K
M = J+K

""" メモ化再帰 """
dp = [[[-1]*(K+1) for i in range(M+1)] for i in range(L+1)]
dp[0][0][0] = 0


def calc(i, j, k):
    global dp

    if dp[i][j][k] > -1:
        return dp[i][j][k]

    ret = N / (i + j + k)
    if i > 0:
        ret += calc(i - 1, j, k) * (i / (i + j + k))
    if j > 0:
        ret += calc(i + 1, j - 1, k) * (j / (i + j + k))
    if k > 0:
        ret += calc(i, j + 1, k - 1) * (k / (i + j + k))
    dp[i][j][k] = ret

    return ret


ret = calc(I, J, K)
print(ret)


""" i, j, kの適切な更新順序 
https://atcoder.jp/contests/dp/submissions/4014057
"""

'''
for n in range(1,L+1):#n=i+j+k
    print(f'i+j+k:{n}')
    for m in range(min(n,M)+1):#m=j+k
        print(f'j+k={m}')
        for k in range(min(m,K)+1):
            print(f'k={k}')
            j=m-k
            i=n-m
            print(i,j,k)
            ret=N/(i+j+k)
            if i>0:
                ret+=dp[i-1][j][k]*(i/(i+j+k))
            if j>0:
                ret+=dp[i+1][j-1][k]*(j/(i+j+k))
            if k>0:
                ret+=dp[i][j+1][k-1]*(k/(i+j+k))
            dp[i][j][k]=ret
print(dp[I][J][K])
'''


