
import sys
sys.setrecursionlimit(1000000)

n = int(input())


def calc(n, p):
    if n < p:
        return 0
    else:
        return n//p + calc(n//p, p)


if n % 2 == 1:
    print(0)
    sys.exit()

print(calc(n//2, 5))

