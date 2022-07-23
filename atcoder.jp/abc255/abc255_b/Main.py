N, K = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))
pos = [list(map(int, input().split())) for _ in range(N)]

dist = [10**12]*N
for ax in A:
    dist[ax] = 0

    for i in range(N):
        if not dist[i]: continue

        dist[i] = min(dist[i], (pos[ax][0]-pos[i][0])**2 + (pos[ax][1]-pos[i][1])**2)

ans = max(dist)**0.5
print(ans)
