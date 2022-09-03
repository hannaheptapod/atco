N, M = map(int, input().split())

G = {i: [set(), set()] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    G[a][1].add(b)
    G[b][0].add(a)

print(G)
