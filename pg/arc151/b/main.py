MOD = 998244353


class FenwickTree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l, r):
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s


def main():
    N, M = map(int, input().split())
    P = list(map(int, input().split()))

    ft = FenwickTree(N+1)

    inv = [0]*N
    for i, p in enumerate(P):
        inv[i] = i - ft._sum(p+1)
        ft.add(p, 1)

    print(inv)


if __name__ == '__main__': main()
