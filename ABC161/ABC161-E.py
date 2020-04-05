# -*- coding: utf-8 -*-
'''
16 4 3
ooxxoxoxxxoxoxxo

output
11
16
'''

import numpy as np
import sys

N, K, C = map(int, input().split())
S = input()

oks = [idx for idx, i in enumerate(S) if i == 'o']
# print(oks)

temp = np.array(oks)
# 逆向きは反転させて、その向きで計算した上で日付を戻す
temp_reverse = (N - 1 - np.array(oks))[::-1]

# print(temp, temp_reverse)


def calc(data: np.ndarray, reverse: bool = False):
    count_dict = {}
    cnt = 0
    while True:
        idx = data[0]
        data = data[data > idx + C]

        if cnt <= K:
            if not reverse:
                count_dict[cnt + 1] = idx + 1
            else:
                count_dict[K - cnt] = N - 1 - idx + 1
        else:
            sys.exit()
        cnt += 1
        if len(data) == 0:
            break

    return count_dict


this = calc(temp)
reverse = calc(temp_reverse, reverse=True)

# print(this, reverse)
ans = list(set(this.values()) & set(reverse.values()))
ans.sort()
[print(i) for i in ans]

