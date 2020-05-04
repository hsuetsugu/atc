# -*- coding: utf-8 -*-
# D

S = input()

ans = 0
res = [0] * 2019
idxs = {}

for i in range(len(S)):
    val = int(S[i:]) % 2019
    if val == 0:
        ans += 1
    else:
        res[val] += 1
        if res[val] > 1:
            idxs[val] = 1

for k, v in idxs.items():
    m = res[k]
    ans += int(m * (m-1) / 2)

print(ans)
