N = int(input())

xyp = [list(map(int, input().split())) for _ in range(N)]

dist = [[0]*N for _ in range(N)]
for i in range(N):
    xi, yi, pi = xyp[i]
    for j in range(i+1, N):
        xj, yj, pj = xyp[j]
        dist[i][j] = -int(-(abs(xi-xj)+abs(yi-yj))//pi)
        dist[j][i] = -int(-(abs(xi-xj)+abs(yi-yj))//pj)

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], max(dist[i][k], dist[k][j]))

ans = min(max(di) for di in dist)
print(ans)
