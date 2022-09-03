N = int(input())
G = {i: set() for i in range(N)}
for _ in range(N-1):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].add(v)
    G[v].add(u)
