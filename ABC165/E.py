# -*- coding: utf-8 -*-
# E

from collections import deque

N, M = map(int, input().split())

if N % 2 == 0:
    num = N - 1
else:
    num = N

num_max = N-1 // 2

used1 = list(range(1, num_max-1))
used2 = [num-a for a in used1]

d1 = deque(used1)
d2 = deque(used2)

for i in range(M):
    val1, val2 = d1.popleft(), d2.popleft()
    print(val1, val2)

