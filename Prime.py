# -*- coding: utf-8 -*-

# from helper import elapsed_time

# n個からr個を選ぶ組み合わせ（nCr）を求める上では、scipy.special.comb() が高速で安定
# ただ競プロではscipy使えないため別のやり方が必要

# 最大公約数はmath.gcdを使えば良い


class Prime(object):
    """ 整数のお役立ち計算
    - 繰り返し二乗法で効率的にn**kを求める（必要であればmodを指定）
    - 素数判定
    - 約数列挙
    - nCrの計算(ピンポイントで求める or r=1:nまで一気に求める）
    - ToDo:
    # divisor : 配列をsortしているため遅い可能性あり
    """

    @staticmethod
    def cmb(n, r):
        """ nCrを求める
        >>> p = Prime()
        >>> p.cmb(10, 2)
        45
        """
        from operator import mul
        from functools import reduce

        r = min(n - r, r)
        if r == 0:
            return 1
        over = reduce(mul, range(n, n - r, -1))
        under = reduce(mul, range(1, r + 1))
        return over // under

    def cmb_precalc(self, n, r, mod: int = 10 ** 9 + 7):
        """ nCr（r=1:nまで）
        >>> p = Prime()
        >>> p.cmb_prep(10)
        >>> p.cmb_precalc(10, 2)
        45
        """
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

    @staticmethod
    def iterated_power(z: int, n: int, mod=None) -> int:
        """ 繰り返し二乗法でn**kを求める（再帰処理は使わない）
        >>> p = Prime()
        >>> p.iterated_power(3, 10)
        59049
        >>> p.iterated_power(3, 10, 10)
        9
        """
        beta = bin(n)[2:]

        Z, q, t = z, 0, len(beta)
        while beta[t - q - 1] == '0':
            Z = Z * Z
            if mod is not None:
                Z = Z % mod
            q += 1
        result = Z

        for k in range(q + 1, t):
            Z = Z * Z
            if mod is not None:
                Z = Z % mod
            if beta[t - k - 1] == '1':
                result = result * Z
                if mod is not None:
                    result = result % mod

        if mod is not None:
            result = result % mod

        return result

    @staticmethod
    # def enumerate_prime(n: int) -> list:
    def enumerate_prime(n: int) -> int:
        """
        n以下の素数を列挙する
        >>> p = Prime()
        >>> p.enumerate_prime(11)
        5
        """

        lis_prime = [True] * (n+1)
        lis_prime[0] = False
        lis_prime[1] = False

        primes = []
        for i in range(2, n+1):
            if lis_prime[i]:
                primes.append(i)
                j = 2 * i
                while True:
                    if j > n:
                        break
                    lis_prime[j] = False
                    j += i

        return len(primes)

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

    p = Prime()

    # 繰り返し二乗法
    n = 10**15
    divisor = 10**9 + 7
    print(p.iterated_power(3, n, divisor))

    # n以下の素数列挙
    n = 10**6
    print(f'number of primes less than {n} : {p.enumerate_prime(n)}')