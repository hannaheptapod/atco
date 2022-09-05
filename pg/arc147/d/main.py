import sys
sys.setrecursionlimit(10**6)
MOD = 998244353

N, M = map(int, input().split())


def pow(a, n):  # 要MOD
    if not n: return 1
    return a*pow(a, n-1)%MOD if n%2 else pow(a**2%MOD, n>>1)


ans = pow(N, M)*pow(M, N-1) % MOD
print(ans)
