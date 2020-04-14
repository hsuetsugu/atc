import math


class SegTree(object):
    """
    Segment Tree
    ある区間[p, q)（qは含まない）における各種統計量を効率的に求める
    """
    def __init__(self, func_type: str, data: list):

        self.func_type = func_type
        if self.func_type == 'min':
            self.ide_ele = float('inf')
        elif self.func_type == 'max':
            self.ide_ele = - float('inf')
        elif self.func_type == 'sum':
            self.ide_ele = 0
        elif self.func_type == 'multiply':
            self.ide_ele = 1
        elif self.func_type == 'gcd':
            self.ide_ele = 0

        n = len(data)
        num = 2 ** (n - 1).bit_length()
        self.seg = [self.ide_ele] * 2 * num

        for i in range(n):
            self.seg[i + num - 1] = data[i]
        for i in range(num - 2, -1, -1):
            self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

        self.num = num

    def segfunc(self, x, y):
        if self.func_type == 'min':
            return min(x, y)
        elif self.func_type == 'max':
            return max(x, y)
        elif self.func_type == 'sum':
            return x + y
        elif self.func_type == 'multiply':
            return x * y
        elif self.func_type == 'gcd':
            return math.gcd(x, y)

    def update(self, k, x):
        k += self.num - 1
        self.seg[k] = x
        while k:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2])

    def query(self, p, q):
        """区間[p, q)におけるsegfuncの値を求める
        >>> data = [1, 5, 2, 5, 1, 20, 15, 2, 10]
        >>> tree = SegTree('min', data)
        >>> tree.query(0,2)
        1
        """
        if q <= p:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q & 1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    data = [1, 5, 2, 5, 1, 20, 15, 2, 10]

    tree = SegTree('min', data)
    print(tree.query(1, 4))
    print(tree.query(5, 9))
    print(tree.query(0, 9))

    tree = SegTree('max', data)
    print(tree.query(1, 4))
    print(tree.query(5, 9))
    print(tree.query(0, 9))

    tree = SegTree('sum', data)
    print(tree.query(1, 4))
    print(tree.query(5, 9))
    print(tree.query(0, 9))

    tree = SegTree('gcd', data)
    print(tree.query(1, 4))
    print(tree.query(5, 7))
    print(tree.query(0, 9))
