from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0: return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)

        if x == y: return

        if self.parents[x] > self.parents[y]: x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x): return -self.parents[self.find(x)]

    def same(self, x, y): return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self): return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self): return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n): group_members[self.find(member)].append(member)
        return group_members

    def __str__(self): return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


N, M, E = map(int, input().split())
edges = [list(map(lambda x: min(int(x)-1, N), input().split())) for _ in range(E)]
Q = int(input())
X = [int(input())-1 for _ in range(Q)]

uf = UnionFind(N+1)
xs = set(X)
for i in range(E):
    if i not in xs: uf.union(*edges[i])

ans = [0]*Q
for i in range(Q-1, -1, -1):
    ans[i] = uf.size(N)-1
    uf.union(*edges[X[i]])

print(*ans, sep='\n')
