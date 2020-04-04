
'''
UUUU?DDR?LLLL
1

UULL?
2
'''

import collections

S = input()
T = int(input())

c = collections.Counter(S)
# print(c)

N_x = c['R'] - c['L']
N_y = c['U'] - c['D']
N_z = c['?']

Z = abs(N_x) + abs(N_y)

if T == 1:
    print(N_z + Z)
else:
    # ? の数がZよりも小さい場合
    # print(f'Z:{Z}, N_z:{N_z}')
    if Z >= N_z:
        print(Z - N_z)
    else:
        temp = N_z - Z
        if temp % 2 == 1:
            print(1)
        else:
            print(0)
