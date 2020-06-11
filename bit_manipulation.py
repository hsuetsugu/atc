# -*- coding: utf-8 -*-
# AとBの論理差をとりたい場合は A & ~B でOK

print('bit演算：シフト演算子、bit_length, population count')
for m in range(7, 10):
    print(m, bin(m), m.bit_length(), bin(m).count('1'))
    # bit_length()で桁数を取り出す
    # popcountは.count('1')で取れる

    # >>  で右シフト、 &1と合わせることで、任意の桁のビットを取り出すことができる
    for i in range(m.bit_length()):
        print(m >> i & 1, sep="", end="")
    print()


print('論理和')
print("12 | 2", bin(12), bin(2), bin(12 | 2), 12|2)
print("10 | 2", bin(10), bin(2), bin(10 | 2), 10|2)
