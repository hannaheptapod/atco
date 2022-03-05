from collections import deque

N, M = map(int, input().split())
MOD = 10**9 + 7

G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())

    G[a].append(b)
    G[b].append(a)

dist = [-1]*(N + 1)
cnt = [0]*(N + 1)
dist[1], cnt[1] = 0, 1

d = deque([1])
while d:
    now = d.popleft()

    for move in G[now]:
        if dist[move] >= 0:
            if dist[move] == dist[now]+1: cnt[move] = (cnt[move] + cnt[now])%MOD
            continue

        dist[move] = dist[now] + 1
        d.append(move)
        cnt[move] = cnt[now]%MOD

ans = cnt[N]%MOD

print(ans)
