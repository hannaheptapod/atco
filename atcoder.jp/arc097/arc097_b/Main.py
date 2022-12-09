def main():
    N, M = map(int, input().split())
    P = tuple(map(int, input().split()))
    dic = {pi: i+1 for i, pi in enumerate(P)}
    dsu_p, dsu_q = DSU(N+1), DSU(N+1)
    for _ in range(M):
        x, y = map(int, input().split())
        dsu_p.merge(x, y)
        dsu_q.merge(dic[x], dic[y])

    ans = 0
    for g in dsu_p.groups()[1:]:
        for pi in g: ans += int(dsu_q.same(pi, dic[pi]))
    print(ans)


class DSU:
    def __init__(self, n):
        self._n=n
        self.parent_or_size=[-1] * n

    def merge(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        x, y=self.leader(a), self.leader(b)
        if x == y: return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]: x, y=y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y]=x
        return x

    def same(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        assert 0 <= a < self._n
        if self.parent_or_size[a] < 0: return a
        self.parent_or_size[a]=self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a):
        assert 0 <= a < self._n
        return -self.parent_or_size[self.leader(a)]

    def groups(self):
        leader_buf=[self.leader(i) for i in range(self._n)]
        result=[[] for _ in range(self._n)]
        for i in range(self._n): result[leader_buf[i]].append(i)
        return [r for r in result if r != []]


if __name__ == '__main__': main()
