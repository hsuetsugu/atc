# 行列の累乗を効率的に計算する
# フィボナッチ数列など漸化式からN項目を求める際に必要
# numpy.linalg.matrix_powerめちゃ早い
# matrix_powerでは、対角化は行わず、n>3については繰り返し二乗法により効率的に計算している
# → 行列の累乗が必要な場合はmatrix_power使えば良い

import numpy as np
import time

# 例：フィボナッチ数列
# a_n+2 = a_n + a_n+1
# N = 10**10
N = 1024
DIVISOR = 10**4

mat = np.array([[1, 1], [1, 0]])
a0 = np.array([1, 0])

# naive：劇遅い（n=10**6くらいまで）
'''
st = time.time()
a = a0
mat_n = mat
for _ in range(N):
    a = np.dot(mat, a)
    mat_n = np.dot(mat_n, mat)
print(a[1] % DIVISOR)
# print(mat_n)
print(f'(naive): time (N={N:.0f}): {time.time()-st:.3f}[sec]')
'''

# 対角化する場合: 途中から値が合わなくなる
# l, P = np.linalg.eig(mat)  # 固有値と固有ベクトル
# D = np.diag(l**N)
# P_ = np.linalg.inv(P)
# mat_n = P @ D @ P_


def power_mat(mat: np.ndarray, n: int) -> np.ndarray:
    ''' numpyのmatrix_power実装'''
    M = np.asanyarray(mat)
    if M.ndim != 2 or M.shape[0] != M.shape[1]:
        raise ValueError("input must be a square array")
    if not np.issubdtype(type(n), int):
        raise TypeError("exponent must be an integer")

    if n == 0:
        M = M.copy()
        M[:] = np.identity(M.shape[0])
        return M
    elif n < 0:
        M = np.linalg.inv(M)
        n *= -1

    result = M
    if n <= 3:
        for _ in range(n-1):
            result=np.dot(result, M)
        return result

    # binary decomposition to reduce the number of Matrix
    # multiplications for n > 3.
    beta = np.binary_repr(n)
    print(beta)
    print(bin(n)[2:])

    Z, q, t = M, 0, len(beta)
    while beta[t-q-1] == '0':
        Z = np.dot(Z, Z)
        q += 1
    result = Z
    for k in range(q+1, t):
        Z = np.dot(Z, Z)
        if beta[t-k-1] == '1':
            result = np.dot(result, Z)
    return result




st = time.time()
mat_n = power_mat(mat, N)
a = np.dot(mat_n, a0)
print(a[1] % DIVISOR)
print(f'time (N={N:.0f}): {time.time()-st:.3f}[sec]')
