# -*- coding: utf-8 -*-
# F

import sys
from heapq import heappop, heappush

N, X, D = map(int, input().split())
if D < 0:
    X, D = -X, -D

l_mod = [[] for _ in range(D)]

if D == 0:
    if X==0:
        print(1)
    else:
        print(N+1)
    sys.exit()

for x in range(N+1):
    l_mod[(x*X) % D].append(x)

# print(l_mod)

ans = 0
for s, ks in enumerate(l_mod):
    d = []
    for k in ks:
        l = (k-1)*k//2
        r = (N-k+(N-1))*k //2
        # print(k, l, r)

        l = (k * X - s) // D + l
        r = (k * X - s) // D + r
        heappush(d, (l, 1, l == r))
        heappush(d, (r, -1, l == r))
    # print(d)

    prev_val = 0
    prev_idx = - float('inf')
    res = {}
    while len(d) > 0:
        idx, tp, flg = heappop(d)
        val = prev_val + tp
        res[idx] = val
        prev_val = val
        prev_idx = idx
    # print(res)
    v_prev = 0
    i_prev = None

    for k, v in res.items():
        if v_prev > 0:
            ans += k - i_prev + 1
        if v_prev == 0 and v == 0:
            ans += 1
        v_prev, i_prev = v, k

print(ans)
