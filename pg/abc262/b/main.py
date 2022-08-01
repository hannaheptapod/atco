from itertools import combinations

N, M = map(int, input().split())
graph = [[0]*N for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())

    graph[u][v] = graph[v][u] = 1

ans = 0
for a, b, c in combinations(range(N), 3):
    if graph[a][b]*graph[b][c]*graph[c][a]: ans += 1

print(ans)
