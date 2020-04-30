
N = int(input())
C = list(map(int, input().split()))
C.sort()

ans = 0
mod = 10**9 + 7

for l in range(N):
    r = N - l - 1
    if r > 0:
        ans += C[l] * (pow(2, r-1, mod) * r + pow(2, r, mod)) * pow(2, l, mod)
    else:
        ans += C[l] * (pow(2, r, mod)) * pow(2, l, mod)

print(int(ans * pow(2, N, mod)) % mod)


