# -*- coding: utf-8 -*-
# E

from collections import Counter

N = int(input())
a = list(map(int, input().split()))

num = list(range(1, N+1))

l1 = [] * N
l2 = [] * N

for i in range(N):
    l1.append(a[i] - num[i])
    l2.append(-a[i] - num[i])

k = list(set(l1) & set(l2))
c1 = Counter(l1)
c2 = Counter(l2)

ans = 0
for k in k:
    ans += c1[k] * c2[k]

print(ans)