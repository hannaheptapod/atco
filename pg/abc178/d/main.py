S = int(input())
MOD = 10**9 + 7

def comb(n, r):
    res = 1
    for i in range(r): res = res*(n - i)*pow(r - i, -1, mod=MOD) % MOD

    return res

ans = 0
for i in range(1, S//3 + 1):
    ans += comb(S - 2*i - 1, i - 1)
    ans %= MOD

print(ans)