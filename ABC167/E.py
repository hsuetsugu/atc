# -*- coding: utf-8 -*-
# E

import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

mod = 998244353

N, M, K = map(int, input().split())

ans = 0


class Mint(object):
    def cmb(self, n, r, mod: int = 10 ** 9 + 7):
        if (r < 0) or (r > n):
            return 0
        r = min(r, n - r)
        return self.g1[n] * self.g2[r] * self.g2[n - r] % mod

    def cmb_prep(self, N: int, mod: int = 10 ** 9 + 7):
        self.g1 = [1, 1]  # 元テーブル
        self.g2 = [1, 1]  # 逆元テーブル
        inverse = [0, 1]  # 逆元テーブル計算用テーブル

        for i in range(2, N + 1):
            self.g1.append((self.g1[-1] * i) % mod)
            inverse.append((-inverse[mod % i] * (mod // i)) % mod)
            self.g2.append((self.g2[-1] * inverse[-1]) % mod)


mint = Mint()
mint.cmb_prep(N-1, mod)

for k in range(K+1):
    ans += (mint.cmb(N-1, k, mod) * M * pow(M-1, N-k-1, mod)) % mod

print(ans % mod)
