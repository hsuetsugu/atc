# -*- coding: utf-8 -*-
'''

'''

N, K = map(int, input().split())

x = N % K
print(min(x, abs(K-x)))

