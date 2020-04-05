# -*- coding: utf-8 -*-
# 整数関係の汎用関数

# ToDo
# divisor : 配列をsortしているため遅い可能性あり


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
    def divisor(n: int) -> list:
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
                res.sort()
                return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()
