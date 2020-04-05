# -*- coding: utf-8 -*-

# 回分
# 回分の判定は、文字列Sをリストで表現した場合、
# S == S[::-1]で判別できる

'''
akasaka

'''

import sys

S = input()
S = list(S)

if not S == S[::-1]:
    print('No')
    sys.exit()

newS = S[:int((len(S)-1)/2)]
if not newS == newS[::-1]:
    print('No')
    sys.exit()


newS = list(S)[int((len(S)+3)/2 - 1):]
if not newS == newS[::-1]:
    print('No')
    sys.exit()

print('Yes')




