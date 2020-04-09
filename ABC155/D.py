# -*- coding: utf-8 -*-
# D　（WIP)
# bisect_left, right（探索）は

'''
4 3
3 3 -4 -2
'''

from bisect import bisect_left, bisect_right


N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

lb, ub = -10**18, 10**18


def judge_self(x, a):
    if a**2 < x:
        return 1
    else:
        return 0


def judge(x: int) -> bool:
    cnt = 0
    for a in A:
        # a * kがxより小さい数をカウントする
        if a < 0:
            idx = bisect_right(A, x/a)
            cnt += N - idx
        elif a == 0:
            # 積は常に0なので、xが正の数であれば全て満たす
            # 一方xが0以下であればxより小さい値にはならない
            if x > 0:
                cnt += N
        else:
            # 正の数の場合：(x/aより小さい数)
            idx = bisect_left(A, x/a)
            # print(a, idx)
            cnt += idx
        cnt -= judge_self(x, a)

    cnt = int(cnt/2)

    return cnt, cnt < K


# xの二部探索
for i in range(100):
    x = int((lb + ub) / 2)
    cnt, res = judge(x)

    # print(x, lb, ub, cnt, res)

    if res:
        lb = x
    else:
        ub = x

# print(lb, ub, x)
print(lb)


'''
# idx = bisect_left(res, temp)
l_positive = []
l_negative = []
l_negative_hat = []

num_positive, num_zero, num_negative = 0, 0, 0
for a in A:
    if a > 0:
        num_positive += 1
        l_positive.append(a)
    elif a == 0:
        num_zero += 1
    else:
        num_negative += 1
        l_negative.append(a)
        l_negative_hat.append(-a)

# print(num_positive, num_zero, num_negative)
num_nonzero = num_positive + num_negative

c_all = N * (N-1) / 2
c_nonzero = num_nonzero * (num_nonzero-1) / 2
c_zero = c_all - c_nonzero
c_negative = num_positive * num_negative


# これ以外はみる必要ない（必ず負の数）
if K <= c_negative:
    res = []
    for i in l_positive:
        for j in l_negative:
            # insort_left(res, i * j)
            res.append(i * j)
    res.sort()
    print(res[K - 1])
    sys.exit()

else:
    K = int(K - c_negative)
    if K <= c_zero:
        print(0)
        sys.exit()

# 正の数
K = int(K - c_zero)

res = []
for idx, i in enumerate(l_positive):
    for idx2, j in enumerate(l_positive):
        if idx <= idx2:
            continue
        # insort_left(res, i * j)
        res.append(i * j)

for idx, i in enumerate(l_negative):
    for idx2, j in enumerate(l_negative):
        if idx <= idx2:
            continue
        # insort_left(res, i * j)
        res.append(i * j)

res.sort()
print(res[K-1])
'''
'''
# super naive
temp = [float('inf')] * K
for i in range(1, N):
    for k in range(i):
        insort_left(temp, A[i] * A[k])
    temp = temp[:K]
    # print(temp)
print(temp[-1])
'''
