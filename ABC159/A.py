# -*- coding: utf-8 -*-

'''
2 1
'''

# n1 偶数
n1, n2 = map(int, input().split())

# 奇数＋奇数 /  偶数+偶数
print(int(n1 * (n1-1) / 2 + (n2 * (n2-1))/2))

