INF = 10**9
N, M = map(int, input().split())

d = [[INF]*N for _ in range(N)]
for i in range(N): d[i][i] = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c

ans = 0
for k in range(N):
    nxt = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            nxt[i][j] = min(d[i][j], d[i][k]+d[k][j])

            if nxt[i][j] < INF: ans += nxt[i][j]
    
    d = nxt

print(ans)