import sys
sys.setrecursionlimit(10**6)
MOD = 998244353

N, M = map(int, input().split())


def pow(a, n):
    if not n: return 1
    if n%2: return a*pow(a, n-1) % MOD
    else: return pow(a**2 % MOD, n>>1)


ans = pow(N, M)*pow(M, N-1) % MOD
print(ans)
