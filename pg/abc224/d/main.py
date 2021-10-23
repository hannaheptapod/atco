from collections import deque
from heapq import heappush, heappop
import math
import bisect

m = int(input())
r = [[] for _ in range(10)]
for _ in range(m):
    u, v = map(int, input().split())
    r[u].append(v)
    r[v].append(u)
p = list(map(int, input().split()))
va = '12345678'
d = deque()
d.append(''.join([str(pi) for pi in p]))

while d:
    v = d.popleft()
    if v != va: continue
    for i in range(10):
        if str(i) not in v: now = i
