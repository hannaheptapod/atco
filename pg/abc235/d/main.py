import sys
from collections import deque
sys.setrecursionlimit(10**9)

a, N = map(int, input().split())

G = [[] for _ in range(10**6)]
for x in range(1, 10**6):
    if a*x < 10**6: G[x].append(a*x)
    if x >= 10 and x%10: G[x].append(int(str(x%10) + str(x//10)))

dist = [-1]*(10**6)
dist[1] = 0

d = deque([1])
while d:
    v = d.popleft()

    for i in G[v]:
        if dist[i] != -1: continue
        
        dist[i] = dist[v] + 1
        d.append(i)

ans = dist[N]

print(ans)