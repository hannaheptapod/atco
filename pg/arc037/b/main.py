class DisjointSet:
    def __init__(self) -> None:
        self.parent = {}
        self.size = {}

    def makeSet(self, set):
        for e in set:
            self.parent[e] = e
            self.size[e] = 1

    def Find(self, x):
        if self.parent[x] == x: return x

        self.parent[x] = self.Find(self.parent[x])
        return self.parent[x]

    def Union(self, x, y):
        a = self.Find(x)
        b = self.Find(y)

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
ds.makeSet(list(range(1, N+1)))
