MOD = 998244353

N = int(input())
fact = {0: 1}
for i in range(1, N**2+1): fact[i] = fact[i-1]*i % MOD


def comb(n, r): return fact[n] * pow(fact[r]*fact[n-r], -1, mod=MOD) % MOD


ans = N**2 * comb(N**2, 2*N-1) * fact[N-1]**2 * fact[(N-1)**2] % MOD
ans = (fact[N**2] - ans) % MOD
print(ans)
