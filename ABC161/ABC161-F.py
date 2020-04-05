# -*- coding: utf-8 -*-

# Nが Kで割り切れるとき、Nを N/Kに置き換える。
# そうでないとき、Nを N − Kに置き換える。
# その結果1となるKは幾つ存在するか

# 効率的にNの約数を求める方法があれば良い

'''
20
'''

N = int(input())


class Prime(object):
    @staticmethod
    def is_prime(n: int) -> bool:
        """
        素数判定
        >>> p = Prime()
        >>> p.is_prime(2)
        True
        >>> p.is_prime(43)
        True
        >>> p.is_prime(4)
        False
        """

        if n == 1:
            return False
        if n == 2:
            return True

        for i in range(2, n):
            if n % i == 0:
                return False
            if i * i > n:
                return True

    @staticmethod
    def divisor(n: int, sort: bool = False) -> list:
        """
        約数列挙
        >>> p = Prime()
        >>> p.divisor(6)
        [1, 2, 3, 6]
        """
        res = []
        if n == 1:
            return [1]

        for i in range(1, n):
            if n % i == 0:
                res.append(i)
                if i != n / i:
                    res.append(int(n / i))
            if (i+1) * (i+1) > n:
                if sort:
                    res.sort()
                return res


# N-1の約数：1以外が全て当てはまる
temp1 = Prime.divisor(N - 1, sort=False)
# print(temp1)
cnt1 = len(temp1) - 1

# Nの約数K：Kで割り切った後でN % K == 1かどうかを見る
temp2 = Prime.divisor(N, sort=True)[1:]
# print(temp2)
cnt2 = 0

for temp in temp2:
    a = N
    while a % temp == 0:
        a = a / temp
    if a % temp == 1:
        cnt2 += 1

print(cnt1 + cnt2)
