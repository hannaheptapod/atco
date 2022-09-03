import sys
sys.setrecursionlimit(10**6)

N = int(input())
G = {i: set() for i in range(1, N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)

Q = int(input())
for _ in range(Q):
    u, k = map(int, input().split())

    seen = {i: False for i in range(1, N+1)}

    def dfs(s, t):
        if seen[s]: return -1
        seen[s] = True

        if not t: return s

        for v in G[s]:
            ret = dfs(v, t-1)
            if ret != -1: return ret
        else: return -1

    print(dfs(u, k))
