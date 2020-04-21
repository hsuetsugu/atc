# -*- coding: utf-8 -*-

# ダイクストラでstartから各町についての最短時間、各町からstartまでの最短時間を求め、
# 残り時間で稼げる金額の最大値を求めれば良い

'''
2 2 5
1 3
1 2 2
2 1 1
'''

from Dijkstra import Dijkstra
import numpy as np

N, M, T = map(int, input().split())
A = list(map(int, input().split()))

g1 = Dijkstra(n=N)
g2 = Dijkstra(n=N)

for i in range(M):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    g1.add_edge(a, b, c, undirected=False)
    g2.add_edge(b, a, c, undirected=False)


dist1, prev1 = g1.run(0)
dist2, prev2 = g2.run(0)

dist = np.array(dist1) + np.array(dist2)
remain = np.ones(N) * T - dist

res = (remain * np.array(A))[1:].max()

print(max(res, 0))
