MOD = 998244353
N = int(input())

ans = pow(2, N, mod=MOD)
for x in range(2*N, N+1, -1):
    ans *= x
    ans %= MOD

print(ans)
