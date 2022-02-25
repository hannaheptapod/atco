from collections import deque

N, X, Y = map(int, input().split())

G = [[] for _ in range(N)]
for i in range(N-1):
    G[i].append(i+1)
    G[i+1].append(i)
G[X-1].append(Y-1)
G[Y-1].append(X-1)

cnt = [0]*(N-1)
for i in range(N):
    dist = [-1]*N
    dist[i] = 0

    d = deque([i])

    while d:
        v = d.popleft()

        for vj in G[v]:
            if dist[vj] != -1: continue

            dist[vj] = dist[v] + 1
            d.append(vj)
    
    for di in dist:
        if di: cnt[di-1] += 1

ans = [ci//2 for ci in cnt]

print(*ans, sep='\n')