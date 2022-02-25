from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

ans = [0 for _ in range(N)]
ans[0] = 'Yes'
d = deque([1])

while d:
    v = d.popleft()
    for i in G[v]:
        if ans[i-1]: continue
        ans[i-1] = v
        d.append(i)

print(*ans, sep='\n')