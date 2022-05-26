from collections import deque

INF = 10**10
H, W = map(int, input().split())
s = [input() for _ in range(H)]

dist = [[INF]*W for _ in range(H)]
dist[0][0] = 1
deq = deque([(0, 0)])

while deq:
    i, j = deq.popleft()
    if (i, j) == (H-1, W-1): break
    if s[i][j] == '#': continue
    dij = dist[i][j]

    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if i+di < 0 or i+di >= H or j+dj < 0 or j+dj >= W or dist[i+di][j+dj] < INF: continue

        dist[i+di][j+dj] = dij + 1
        deq.append((i+di, j+dj))

sm = sum(int(s[i][j] == '.') for i in range(H) for j in range(W))
ans = max(sm - dist[-1][-1], -1)
print(ans)
