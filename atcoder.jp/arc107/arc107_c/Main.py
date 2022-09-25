MOD = 998244353


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


def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    ds, dt = DSU(N), DSU(N)
    for i in range(N-1):
        for j in range(i+1, N):
            fs, ft = True, True

            for k in range(N):
                if fs: fs = A[i][k] + A[j][k] <= K
                if ft: ft = A[k][i] + A[k][j] <= K
                if not fs and not ft: break

            if fs: ds.merge(i, j)
            if ft: dt.merge(i, j)

    fact = [1]*(N+1)
    for i in range(1, N+1): fact[i] = fact[i-1]*i % MOD

    ans = 1
    for g in ds.groups(): ans = ans*fact[len(g)] % MOD
    for g in dt.groups(): ans = ans*fact[len(g)] % MOD

    print(ans)


if __name__ == '__main__': main()
