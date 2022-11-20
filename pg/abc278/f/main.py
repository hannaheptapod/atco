from functools import reduce
from operator import xor


def main():
    N = int(input())
    S = [input() for _ in range(N)]

    dsu = DSU(N)
    graph = [set() for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if S[i][-1] == S[j][0]:
                graph[i].add(j)
                dsu.merge(i, j)
            if S[j][-1] == S[i][0]:
                graph[j].add(i)
                dsu.merge(j, i)

    groups = dsu.groups()
    grundy = [0]*len(groups)
    # Grundy数を計算したい

    ans = 'First' if reduce(xor, grundy) else 'Second'
    print(ans)


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


if __name__ == '__main__': main()
