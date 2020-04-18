# -*- coding: utf-8 -*-
# E

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
mod = 10**9 + 7


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


ans = 0
mint = Mint()
mint.cmb_prep(N + 5)

for i in range(N):
    if i >= K-1:
        ans += A[i] * mint.cmb(i, i-K+1)
    if N - i - 1 >= K-1:
        ans -= A[i] * mint.cmb(N-i-1, K-1)

print(ans % mod)
