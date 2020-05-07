'''
3 3
1 2 5
2 3 10
1 3 9
'''

# number of nodes and vertexes
N, M = map(int, input().split())

# nodes
d = {}
d2 = {}
for i in range(N):
    d[i] = []
    d2[i] = {}

# set vertex information
for i in range(M):
    a, b, val = map(int, input().split())
    a, b, val = a-1, b-1, val
    d[a].append(b)
    d[b].append(a)
    d2[a][b] = val

print(d)
print(d2)