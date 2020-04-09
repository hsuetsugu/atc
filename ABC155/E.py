# -*- coding: utf-8 -*-
# E

# 下の桁からの繰り下がりがあるかないかで場合わけし、
# 下からi桁における最小枚数をDPで順に計算していく
# 計算量はO(N)

# 初期条件として、最初は繰り下がりはありえないため
# dp[0][0] =0, dp[0][1]=infとする


N = input()
N = [int(i) for i in list(N)][::-1] + [0]
lenN = len(N)

dp = [[float('inf')]*2 for _ in range(len(N)+1)]
dp[0][0] = 0


for i in range(1, len(N)+1):
    res0 = float('inf')
    res1 = float('inf')

    for j in range(2):
        for num in range(10):
            if j == 1:
                # 前に繰り下がりしていたらnumを減らす
                num = num - 1
            if num >= N[i-1]:
                b = num - N[i-1]
                res0 = min(res0, dp[i - 1][j] + num + b + j)
            else:
                b = num - N[i-1] + 10
                res1 = min(res1, dp[i - 1][j] + num + b + j)
    dp[i][0] = res0
    dp[i][1] = res1


print(min(dp[lenN][0], dp[lenN][1]))
