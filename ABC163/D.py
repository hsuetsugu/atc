# -*- coding: utf-8 -*-
# D

# 選んだ個数がKからN+1までそれぞれについて、小さい数部分の和を考えればよく、
# Kの場合、K個作ってできる最大の数 - 小さい方から最小の数を求めれば良い

N, K = map(int, input().split())
mod = 10**9 + 7

ans = 0
for num in range(K, N+2):
    res1 = int((2*N-num+1) * num / 2) % mod
    res2 = int((num-1) * num / 2) % mod
    ans += res1 - res2 + 1
    # print(num, res1, res2)

print(ans % mod)
