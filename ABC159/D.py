# -*- coding: utf-8 -*-

'''
5
1 1 2 1 2
'''


N = int(input())
a = list(map(int, input().split()))

import collections

a_0 = a[1:]
first_val = a[0]
# print(a_0)

c = collections.Counter(a_0)
# print(c)

# a_0の同じ数の組み合わせを求める
cnt_0 = 0
for val in c.values():
    cnt_0 += int(val * (val-1) /2)
print(cnt_0)

# 減る分：もともとnだったのはn-1減って、
# 増える分：もともとNだったのはn増える

for i in a_0:
    if i == first_val:
        print(cnt_0)
    else:
        print(cnt_0 + c[first_val] - (c[i]-1))

