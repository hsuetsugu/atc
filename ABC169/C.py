# -*- coding: utf-8 -*-
# C

import sys
from decimal import Decimal
from collections import defaultdict, deque
from heapq import heappush, heappop
import math
import bisect
input = sys.stdin.readline

# 再起回数上限変更
# sys.setrecursionlimit(1000000)

a, b = input().split()

print(int(Decimal(a) * Decimal(b)))


