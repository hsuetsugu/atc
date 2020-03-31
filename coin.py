

"""
500: 2
100: 2
50: 2
X : 100
"""

# a = input()
# b = input()
# c = input()
# x = input()

x = 1200
a, b, c = 2, 2, 2

cnt = 0
if x == 50:
    print(1)
elif x < 500:
    print(x // 100 + 1)
else:
    print(5 + x // 500)