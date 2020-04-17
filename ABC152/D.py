# -*- coding: utf-8 -*-
# D
# DP[i]をiまでの数字での組み合わせの数として計算したが、
# 条件分岐が複雑で時間がかかった
# 普通にNまで愚直に最初の桁と最後の桁の組み合わせを記録して、その逆のペアを考えれば良いだけだった

N = int(input())


def calc(num):
    s = list(str(num))[::-1]
    s2 = int(s[-1])
    s1 = int(s[0])

    keta = 0
    while True:
        num = num // 10
        keta += 1
        if num == 0:
            break

    if s1 == s2:
        if keta == 1:
            return 1
        elif keta == 2:
            return 1 + 2
        else:
            ans = 0
            for i in range(keta - 3):
                ans += (10 ** (i+1)) * 2
            ans += (int(''.join(s[1:-1][::-1]))+1) * 2 + 3
            return ans

    elif s1 > s2:
        if keta == 2:
            return 0
        else:
            ans = 0
            for i in range(keta - 2):
                ans += 10 ** i
            return ans * 2
    else:
        if s1 == 0:
            return 0
        else:
            ans = 0
            for i in range(keta - 1):
                ans += 10 ** i
            return ans * 2


# print(10, calc(10))

dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = dp[i-1] + calc(i)

# print(dp)
print(dp[N])

