# -*- coding: utf-8 -*-
# E
# Biは、Aの最小公倍数/Aiで求まる
# Aiについて素因数分解を効率的に実施可能
# ただ愚直にLCM計算してそれぞれのBiを足していくやり方でも十分であった（組み込みのpow関数を使うと早い）

import sys

# シンプルにpow使うと早い
# https://atcoder.jp/contests/abc152/submissions/9609584
mod=10**9+7
n=int(input())
a=list(map(int,input().split()))
def gcd(a,b):
    while b:a,b=b,a%b
    return a
def lcm(a,b):return a*b//gcd(a,b)

l=a[0]
for i in range(1,n):
    l=lcm(l,a[i])
ans=0
l%=mod
for i in range(n):
    ans+=l*pow(a[i],mod-2,mod)
    ans%=mod
print(ans)

sys.exit()



DIVISOR = 10**9 + 7

N = int(input())
A = tuple(map(int, input().split()))
max_el = max(A)


def enumerate_prime(n: int) -> (list, list):
    lis_prime = [True] * (n + 1)
    lis_prime[0] = False
    lis_prime[1] = False
    div_prime = [i for i in range(n+1)]

    primes = []
    primes_idx = {}

    cnt = 0
    for i in range(2, n + 1):
        if lis_prime[i]:
            primes.append(i)
            primes_idx[i] = cnt
            cnt += 1

            j = 2 * i
            while True:
                if j > n:
                    break
                lis_prime[j] = False
                div_prime[j] = i
                j += i

    return primes, primes_idx, div_prime



primes, primes_idx, div_prime = enumerate_prime(max_el)
# print(primes, primes_idx, div_prime)


max_prime = [0] * len(primes)
res = [[0] * len(primes) for i in range(N)]

for i, a in enumerate(A):
    next_idx = a
    while True:
        div = div_prime[next_idx]
        res[i][primes_idx[div]] += 1
        max_prime[primes_idx[div]] = max(res[i][primes_idx[div]], max_prime[primes_idx[div]])
        if next_idx == div:
            break
        next_idx = int(next_idx / div)

# print(res)
# print(max_prime)

ans = 0
for i, a in enumerate(A):
    temp = 1
    for j, prime in enumerate(primes):
        val = max_prime[j] - res[i][j]
        if val > 0:
            temp *= iterated_power(prime, val, DIVISOR)
    ans += temp % DIVISOR


print(ans % DIVISOR)
