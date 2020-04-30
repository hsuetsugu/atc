from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

data = P.copy()
data.sort()


for idx, i in enumerate(list(permutations(data, N))):
    if list(i) == P:
        a = idx
    if list(i) == Q:
        b = idx

print(abs(a-b))
