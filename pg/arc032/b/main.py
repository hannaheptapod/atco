class DisjointSet:
    def __init__(self) -> None: self.parent, self.size = {}, {}

    def makeSet(self, set):
        for e in set: self.parent[e], self.size[e] = e, 1

    def Find(self, x):
        if self.parent[x] == x: return x

        self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]

    def Union(self, x, y):
        a, b = self.Find(x), self.Find(y)

        if a == b: return False

        if self.size[a] < self.size[b]: a, b = b, a

        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

    def issame(self, x, y): return self.Find(x) == self.Find(y)

    def getsize(self, x): return self.size[self.Find(x)]


def printSet(set, ds): return [ds.Find(i) for i in set]


N, M = map(int, input().split())

ds = DisjointSet()
cross = [i for i in range(N)]
ds.makeSet(cross)
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    ds.Union(a, b)

ans = len(set(printSet(cross, ds))) - 1
print(ans)
