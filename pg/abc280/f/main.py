from collections import defaultdict


def main():
    global N, M, edges
    N, M, Q = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    quers = [tuple(map(int, input().split())) for _ in range(Q)]

    dsu = DSU(N+1)

    for u, v, _ in edges: dsu.merge(u, v)


class DSU:
    def __init__(self, n):
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        x, y = self.leader(a), self.leader(b)
        if x == y: return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]: x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        assert 0 <= a < self._n
        if self.parent_or_size[a] < 0: return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a):
        assert 0 <= a < self._n
        return -self.parent_or_size[self.leader(a)]

    def groups(self):
        leader_buf = [self.leader(i) for i in range(self._n)]
        result = [[] for _ in range(self._n)]
        for i in range(self._n): result[leader_buf[i]].append(i)
        return [r for r in result if r != []]


def bellman_ford(s, g):
    d = [float('inf')]*(N+1)
    d[s] = 0

    for i in range(N):
        update = False
        for u, v, c in edges:
            if d[v] > d[u] + c:
                d[v] = d[u] + c
                update = True
            if d[u] > d[v] - c:
                d[u] = d[v] - c
                update = True
        if not update: break

        if i == N-1: return 'inf'

    return d[g]


if __name__ == '__main__': main()
