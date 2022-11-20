from sys import stdin
import array


def main():
    MOD = 998244353
    C = 10**12

    N = int(stdin.readline())
    A = array.array('i', map(int, stdin.readline().split()))
    ord = list((ai, i) for i, ai in enumerate(A))
    ord.sort(reverse=True)

    fw = FenwickTree(N)
    d = array.array('i', [0]*N)
    for (ak, k) in ord:
        x = fw.sum(0, k)
        d[k] = ((k - x//C)*ak + x%C) % MOD
        fw.add(k, C+ak)

    ans = array.array('i', [0]*N)
    s = 0
    for i, (ai, di) in enumerate(zip(A, d)):
        s += (2*di + ai) % MOD
        ans[i] = (s*pow(pow(i+1, 2, MOD), MOD-2, MOD)) % MOD  # フェルマーの小定理
        # ans[i] = (s*pow(i+1, -2, MOD)) % MOD  # CPython3.8でこうするよりもPyPyで上のようにする方が速い

    print(*ans, sep='\n')


# 方針1 -> 座圧しないとTLE
'''
def main():
    MOD = 998244353
    M = 200000

    N = int(input())
    A = list(map(int, input().split()))

    fw1, fw2 = FenwickTree(M+1), FenwickTree(M+1)

    ans = [0]*N
    s = 0
    for i, x in enumerate(A):
        d = (fw1.sum(0, x+1)*x + fw2.sum(x+1, M+1)) % MOD
        s = (s + 2*d + x) % MOD
        ans[i] = (s*pow(i+1, -2, MOD)) % MOD
        fw1.add(x, 1)
        fw2.add(x, x)

    print(*ans, sep='\n')
'''


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


if __name__ == '__main__': main()
