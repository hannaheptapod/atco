import sys
sys.setrecursionlimit(10**6)


class Node():
    def __init__(self):
        self.parent = -1
        self.children = []

    def __repr__(self): return f'Node({self.parent}, {self.children})'


N, Q = map(int, input().split())
T = [Node() for _ in range(N)]
P = list(map(int, input().split()))
for i in range(1, N):
    T[i].parent = P[i-1]-1
    T[P[i-1]-1].children.append(i)

for _ in range(Q):
    arr = [False]*N
    v = list(map(lambda x: int(x)-1, input().split()))[1:]
    for vi in v: arr[vi] = 1

    def dfs(v, f):
        rev = f != arr[v]
        cnt = int(rev)
        for u in T[v].children: cnt += dfs(u, f^rev)
        return cnt

    ans = dfs(0, 0)
    print(ans)
