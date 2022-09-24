import sys
from collections import deque
sys.setrecursionlimit(10**6)


def main():
    global X, Y, G
    N, X, Y = map(int, input().split())
    G = [set() for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        G[u].add(v)
        G[v].add(u)

    global ans, seen
    ans = deque()
    seen = [False]*(N+1)
    seen[X] = True
    dfs(X)

    print(*ans)


def dfs(u):
    if u == Y:
        ans.appendleft(u)
        return True

    for v in G[u]:
        if seen[v]: continue
        seen[v] = True
        if dfs(v):
            ans.appendleft(u)
            return True

    return False


if __name__ == '__main__': main()
