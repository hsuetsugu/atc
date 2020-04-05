# -*- coding: utf-8 -*-

'''
100000
'''

K = int(input())
c = 1

for i in range(K -1):
    str_c = list(str(c))
    str_c = [int(i) for i in str_c][::-1]

    keta = len(str_c)

    if set(str_c) == set([9]):
        c = c + 1
        continue

    for ket in range(keta):
        # 次の桁を見る
        if ket == keta - 1:
            str_c[ket] += 1

            for j in range(ket):
                # print(str_c)
                if str_c[ket - j] == 0:
                    str_c[ket - j - 1] = 0
                else:
                    str_c[ket - j - 1] = str_c[ket - j] - 1

            str_c = [str(i) for i in str_c][::-1]
            c = int(''.join(str_c))
            break

        if str_c[ket] == str_c[ket + 1] + 1:
            continue

        # 大きくできるところがあれば増やす
        if abs(str_c[ket] - str_c[ket + 1]) <= 1:
            if str_c[ket] < 9:
                str_c[ket] += 1
                for j in range(ket):
                    if str_c[ket - j] == 0:
                        str_c[ket - j - 1] = 0
                    else:
                        str_c[ket - j - 1] = str_c[ket - j] - 1
                str_c = [str(i) for i in str_c][::-1]
                c = int(''.join(str_c))
                break


print(c)

