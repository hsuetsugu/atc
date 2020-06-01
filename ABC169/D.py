# -*- coding: utf-8 -*-
# D

import sys
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
import math
import bisect
from itertools import accumulate
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

N = int(input())

def factorization(n):
    arr = defaultdict(int)
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr[i] = cnt

    if temp!=1:
        arr[temp] = 1

    if arr==[]:
        arr[n] = 1

    return arr

if N == 1:
    print(0)
    sys.exit()

d = factorization(N)
# print(d)
max_d = max(d.values())
# print(max_d)

ref = [i for i in range(1, max_d+1)]
ref = list(accumulate(ref))
# print(ref)

ans = 0
for k, v in d.items():
    # print(k, v, bisect.bisect_right(ref, v))
    ans += bisect.bisect_right(ref, v)
print(ans)

