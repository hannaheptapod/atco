from collections import defaultdict
from bisect import bisect

N = 1<<20


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
    Q = int(input())
    ans = defaultdict(int)
    ft = FenwickTree(N)

    for _ in range(Q):
        t, x = map(int, input().split())
        h = x%N

        if t == 1:
            idx = ft[h:]
            if idx == N: idx = ft[h:]
            ft[idx] = N
            ans[idx] = x
        else: print(ans[h])


if __name__ == '__main__': main()
